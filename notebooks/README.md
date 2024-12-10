# README: How to Load Datasets

This guide explains how to load and manage the datasets `cleaned_2019-01-03_data.csv` and `cleaned_2022-01_data.csv` for the Boston MBTA Bus Equity project. Follow the instructions below to set up file paths, filter files, and load data into a combined DataFrame.

## File Path Configuration
### Define the File Directory
Ensure all relevant datasets for 2019 and 2022 are stored in the same directory. Replace `...` in the following code with your local directory path:

```python
# Set the file directory path
file_directory = r"..."
```

### List and Filter Files
Run the following code to list all files in the directory and filter for datasets containing `2019` and `2022`:

```python
# List of all files in the directory
all_files = os.listdir(file_directory)

# Filter files for the relevant datasets
data_files_2019 = [file for file in all_files if "2019" in file and file.endswith('.csv')]
data_files_2022 = [file for file in all_files if "2022" in file and file.endswith('.csv')]

# Sort files by month order for loading
data_files_2019.sort()
data_files_2022.sort()

print("2019 files:", data_files_2019)
print("2022 files:", data_files_2022)
```

## Load Datasets
### Option 1: Load Individual Files
If you are working with specific datasets (e.g., `cleaned_2019-01-03_data.csv` and `cleaned_2022-01_data.csv`), use the following code:

```python
# Load datasets
import pandas as pd

df_2019 = pd.read_csv('C:\\Users\\Huihao Xing\\Documents\\临时文件\\G1\\DS 701\\Project\\Dataset\\cleaned_2019-01-03_data.csv', parse_dates=['service_date'])
df_2022 = pd.read_csv('C:\\Users\\Huihao Xing\\Documents\\临时文件\\G1\\DS 701\\Project\\Dataset\\cleaned_2022-01_data.csv', parse_dates=['service_date'])
```
Make sure to replace the paths above with your local file paths.

### Option 2: Load Multiple Files Dynamically
To load and concatenate multiple datasets for 2019 and 2022, use the function below:

```python
import os

# Function to load and concatenate multiple files into a single DataFrame
def load_data(files, file_directory):
    df_list = []
    for file in files:
        file_path = os.path.join(file_directory, file)
        # Parsing 'service_date' as datetime while loading the file
        df = pd.read_csv(file_path, parse_dates=['service_date'])
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

# Load datasets for 2019 and 2022
data_2019 = load_data(data_files_2019, file_directory)
data_2022 = load_data(data_files_2022, file_directory)

# Add 'Year' column for distinction
data_2019['Year'] = 2019
data_2022['Year'] = 2022

# Combine both years into one DataFrame
df = pd.concat([data_2019, data_2022], ignore_index=True)

print("Data for 2019 and 2022 loaded and combined.")
```

## Notes
- Ensure all required libraries (`pandas`, `os`) are installed.
- Confirm that the `service_date` column is present in all datasets to avoid errors during parsing.
- Replace all placeholder paths (`...`) with your local directory paths.
- For performance optimization, verify the integrity of datasets before concatenating them.

With these steps, you should be able to load, clean, and combine the datasets for analysis. For additional questions, please refer to project documentation or contact the team lead.

