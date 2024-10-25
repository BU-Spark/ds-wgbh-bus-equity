import time
import numpy as np
import pandas as pd
from tqdm import tqdm
import warnings
import concurrent.futures
import itertools
from tqdm.contrib.concurrent import thread_map
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)

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
    temp = df.query("service_date == @s_date and route_id == @r_id and direction_id == @dire and stop_id == @s_id")
    
    if temp.empty:
        return pd.DataFrame()
    temp["available_bus_depart_time"] = get_available_bus_departure_time(temp)
    return temp

if __name__ == "__main__":
    for month in ["01", "02"]:
        file_name = f"2022-{month}"
        filter_route_ids = [
            '22', '29', '15', '45', '28', '44', 
            '42', '17', '23', '31', '26', '111',
            '24', '33', '14'
            ]
        df = pd.read_csv(f"arrdep_{file_name}_simplecleaned.csv")
        print(df.head())
        print(df.columns)
        df = df.query("route_id in @filter_route_ids")
        df["scheduled_datetime"] = pd.to_datetime(df["scheduled_datetime"])
        df["actual_datetime"] = pd.to_datetime(df["actual_datetime"])
        
        service_dates = df.service_date.unique()
        route_ids = df.route_id.unique()
        directions = df.direction_id.unique()
        stop_ids = df.stop_id.unique()
        print(df.shape[0])
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
        data.to_csv(f"./cleaned_{file_name}_data.csv", index=False)

        print("Finished processing and saved to CSV.")
        time.sleep(60)
