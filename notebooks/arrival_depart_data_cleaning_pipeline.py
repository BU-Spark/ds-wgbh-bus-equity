import argparse
import concurrent.futures
import itertools
import os
import time
import warnings
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm 
from tqdm.contrib.concurrent import thread_map
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)

FOLDER = os.path.join('..', 'dataset-documentation', 'raw_data')
FILTE_ROUTE_IDS = [
    '22', '29', '15', '45', '28', '44', 
    '42', '17', '23', '31', '26', '111',
    '24', '33', '14'
]


def drop_missing_values(df):
    print(df.isna().sum() / df.shape[0])
    df = df.dropna(subset=['half_trip_id', 'time_point_id', 'time_point_order', 'actual'])
    df = df.reset_index(drop=True)

    return df


def reformat_date_vars(df):
    df['service_date'] = pd.to_datetime(df['service_date'].str.slice(0, 10))
    scheduled_is_next_day = (df['actual'].notna() & df['scheduled'].str.startswith('1900-01-02')).astype(int)
    actual_is_next_day =  (df['actual'].notna() & df['actual'].str.startswith('1900-01-02')).astype(int) 

    df['scheduled'] = pd.to_datetime(df['scheduled'], format = '%Y-%m-%d %H:%M:%S.000')
    df['scheduled'] = df['scheduled'].dt.strftime('%H:%M:%S')
    df['scheduled'] = pd.to_datetime(df['scheduled'], format='%H:%M:%S').dt.time.astype(str)
    df['scheduled_datetime'] = pd.to_datetime(df['service_date'].astype(str) + ' ' + df['scheduled'])
    timedelta_adjustment = pd.to_timedelta(scheduled_is_next_day, unit='d')
    df['scheduled_datetime'] += timedelta_adjustment

    df['actual'] = pd.to_datetime(df['actual'], format = '%Y-%m-%d %H:%M:%S.000')
    df['actual'] = df['actual'].dt.strftime('%H:%M:%S')
    df['actual'] = pd.to_datetime(df['actual'], format='%H:%M:%S').dt.time.astype(str)
    df['actual_datetime'] = pd.to_datetime(df['service_date'].astype(str) + ' ' + df['actual'])
    timedelta_adjustment = pd.to_timedelta(actual_is_next_day, unit='d')
    df['actual_datetime'] += timedelta_adjustment

    return df


def get_available_bus_departure_time(df):
    act_depart_time = df.sort_values("actual_datetime").actual_datetime
    available_bus_departure_time = []
    for i in range(df.shape[0]):
        try:
            available_bus_departure_time.append(
                # search for the first actual departure time later than scheduled departure time
                act_depart_time[act_depart_time >= df["scheduled_datetime"].iloc[i]].iloc[0]
            )
        except: # when there is no bus actual departure time later than the scheduled departure time
            available_bus_departure_time.append(None)
    return available_bus_departure_time


def process_combination(args):
    s_date, r_id, dire, s_id, df = args
    temp = df.query("service_date == @s_date and route_id == @r_id and direction == @dire and stop_id == @s_id")
    
    if temp.empty:
        return pd.DataFrame()
    temp["available_bus_depart_time"] = get_available_bus_departure_time(temp)
    return temp
    

def main(file_name, output_name):
    data = pd.read_csv(
        os.path.join(
            FOLDER,
            file_name
        )
    )
    print(data.head())
    if 'earliness' in data.columns:
        data = data.drop('earliness', axis = 1)
        print("Remove arrliness var")
    
    data = drop_missing_values(data)
    print("Drop missing values")
    data = reformat_date_vars(data)
    print("Reformat date vars")
    data.to_csv(f"arrdep_{output_name}_simplecleaned.csv", index = False)
    print(data.head())
    data = data.query("route_id in @FILTER_ROUTE_IDS")
    
    service_dates = data.service_date.unique()
    route_ids = data.route_id.unique()
    directions = data.direction.unique()
    stop_ids = data.stop_id.unique()
    combinations = list(itertools.product(service_dates, route_ids, directions, stop_ids))
    
    results = []
    with tqdm(total=len(combinations), desc="Processing Combinations") as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            future_results = executor.map(
                process_combination, 
                [(s_date, r_id, dire, s_id, df) for s_date, r_id, dire, s_id in combinations]
                )
            for result in future_results:
                results.append(result)
                pbar.update(1)
    data = pd.concat(results, axis=0)
    output_path = os.path.join(
        FOLDER,
        f"cleaned_{output_name}_data.csv"
    )
    data.to_csv(output_path, index=False)
    print("Save cleaned data")

if __name__ == "__main__":

    for file in os.listdir(os.path.join(FOLDER, "MBTA Bus Arrival Departure Times 2019")):
        file_name = os.path.join("MBTA Bus Arrival Departure Times 2019", file)
        output_name = file[27:34]
        print(output_name)
        main(file_name, output_name)
        time.sleep(10)