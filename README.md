# WGBH Impact and Equity: Boston Bus Equity (Fall 2024 Project)

## Overview
This repository contains all code, data, and documentation for the **Boston Bus Equity** project, conducted in partnership with **Paul Singer**, Senior Editor, Equity & Justice at **GBH News**. This project, part of BU’s DS701 practicum course, aims to explore the impact of MBTA bus performance on Boston residents, examining service disparities and trends across different neighborhoods. The analysis will help inform news stories on the accessibility and equity of Boston’s public transportation system.

## Project Summary
This project aims to deliver a detailed analysis of the Massachusetts Bay Transportation Authority (MBTA) bus performance in 2019 and 2022. The main focus is to compare the ridership and reliability data for each bus route between the two years. This study will identify any areas where bus service could be improved to better meet community needs. By analyzing the performance for each route, this report can inform data-driven decision-making for policymakers and MBTA to enhance overall transit system performance to better serve Boston residents and communities. 

## Key Questions
What is the ridership per bus route?
What are the end-to-end travel times for each bus route in the city?
On average, how long does an individual have to wait for a bus (on time vs. delayed)?
What is the average delay time of all routes across the entire city?
What is the average delay time of the target bus routes (22, 29, 15, 45, 28, 44, 42, 17, 23, 31, 26, 111, 24, 33, 14 - from Livable Streets report)?
Are there disparities in the service levels of different routes (which lines are late more often than others)?

## Repository Structure
- **dataset-documentation/**: Documentation and preliminary data cleaning notes.
- **notebooks/**: Jupyter notebooks for data analysis and visualization, including the latest work on answering base project questions.
- **utils/data_cleaning/**: Python scripts for data cleaning and pre-processing.
- **.github/workflows/**: GitHub Actions for CI/CD and code quality checks.
- **requirements.txt**: Python dependencies for project setup.
- **README.md**: Project overview and repository navigation guide (this file).

## Datasets 

- The datasets for this project are listed below. 

- Ridership
- Fall 2019 https://mbta-massdot.opendata.arcgis.com/datasets/47bbf5047f0646fbae11ef3ed8ccea47_0/explore?filters=eyJzZWFzb24iOlsiRmFsbCAyMDE5Il19 
- Fall 2022 https://mbta-massdot.opendata.arcgis.com/datasets/47bbf5047f0646fbae11ef3ed8ccea47_0/explore?filters=eyJzZWFzb24iOlsiRmFsbCAyMDIyIl19 

- Reliability
- 2019 Bus Departure/Arrival Times https://mbta-massdot.opendata.arcgis.com/datasets/1bd340b39942438685d8dcdfe3f26d1a/about 
- 2022 Bus Departure/Arrival Times https://mbta-massdot.opendata.arcgis.com/datasets/ef464a75666349f481353f16514c06d0/about 


## Getting Started
### Prerequisites
- Python 3.8 or above
- Required libraries are listed in `requirements.txt`.
