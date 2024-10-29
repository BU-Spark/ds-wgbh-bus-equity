# Arrival and Departure Data Cleaning Pipeline

This README provides an overview of the `arrival_depart_data_cleaning_pipeline.py` script, which is designed to process and clean bus arrival and departure data.

## Overview

The script performs the following main tasks:
1. Loads raw arrival and departure data
2. Cleans and reformats the data
3. Processes the data for specific route IDs
4. Calculates available bus departure times
5. Saves the cleaned data to a CSV file

## Key Features

- Handles missing values
- Reformats date and time variables
- Filters data for specific route IDs
- Calculates available bus departure times using parallel processing
- Utilizes multi-threading for improved performance

## Usage

To run the script, use the following command:
```python
python arrivale_depar_data_cleaning_pipeline.py \
    --data_path ../raw_data/MBTA_Bus_Arrival_Departure_Times_2022/MBTA-Bus-Arrival-Departure-Times_2022-08.csv \
    --output_path ../cleaned_data/cleaned_MBTA-Bus-Arrival-Departure-Times_2022-08.csv
```
