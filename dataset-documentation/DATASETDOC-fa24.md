### ***Project Information***
**Project Name:**  
WGBH Impact and Equity: Boston Bus Equity  

**GitHub Repository Link:**  
https://github.com/BU-Spark/ds-wgbh-bus-equity/tree/main

**Google Drive Folder Link:**  
https://drive.google.com/drive/u/6/folders/1Elwtx3occkEM6suEBdBMlYV4TkGH8SQV

**Project Description and Goals:**  
This project examines MBTA bus system performance from 2019 to 2022, focusing on ridership, travel times, delays, and equity. Its goals are to assess service trends and disparities, especially in Environmental Justice (EJ) communities, to support data-driven improvements for policymakers and MBTA. The insights aim to enhance service quality, equity, and sustainability for Boston residents.

**Client for the Project:**  
Paul Singer, Senior Editor, Equity & Justice at GBH News.

**Client Contacts:**  
- **Name:** Paul Singer  
  **Email:** paul_singer@wgbh.org  

**Class Name:**  
DS701: BU Spark! Practicum Course in Data Science  

---

### ***Dataset Information***

**Data Sets Used:**  
- MBTA Bus Ridership by Trip, Season, Route/Line, and Stop (2016–2022)  
- MBTA Arrival and Departure Data (2018–2024)  
- MBTA 2023 System-Wide Passenger Survey  
- Livable Streets Report  

**Data Dictionary Link:**  
https://mbta-massdot.opendata.arcgis.com/datasets/1bd340b39942438685d8dcdfe3f26d1a/about
https://mbta-massdot.opendata.arcgis.com/datasets/MassDOT::mbta-2023-system-wide-passenger-survey-data/about
https://mbta-massdot.opendata.arcgis.com/datasets/MassDOT::mbta-bus-ridership-by-trip-season-route-line-and-stop/about

For more about how datasets are cleaned, please direct to the utils/data_cleaning branch.

**Keywords/Tags:**  
Domains: Civic Tech, Transportation, Equity Analysis  
Tags: MBTA, Ridership Trends, Bus Delays, Environmental Justice  

---

#### **Motivation**  
- **Purpose:** Evaluate MBTA bus performance and equity for Boston residents.  
- **Task:** Identify disparities and inform policy decisions.  
- **Gap Addressed:** The need for comprehensive public transport performance insights for EJ communities.

---

#### **Composition**  
- **Instances Represented:** Passenger trips and bus operations.  
- **Formats:** Tabular data (e.g., ridership statistics, bus departure times).  
- **Instance Count:** Dependent on dataset specifics (e.g., daily trip data).  
- **Completeness:** Sampling includes seasonal trends but may omit entire-year data. Some datasets focus on Fall months (e.g., 2019 and 2022).

---

#### **Preprocessing**  
- Addressed discrepancies in ridership and adjusted metrics.  
- Handled missing values and outliers in arrival/departure times.  
- Added variables like `available_bus_depart_time` for improved accuracy in wait-time analysis.  

**Transformations:**  
- Aggregated ridership data and refined delay metrics for analysis.
- Data cleaning to remove some missing values.

**Access to Raw Data:**  
Please direct to the Top-level readme about how data are accessed.

**Code for Preprocessing:**  
Please direct to the Top-level readme about how data are preprocessed.

---

#### **Uses**
- **Tasks Completed:** Analyzed ridership, delays, disparities, and EJ impacts.  
- **Future Tasks:** Explore correlations with additional datasets (e.g., census data).  
- **Dataset Limitations:** Seasonal focus limits year-round applicability.

**Prohibited Uses:**  
For external use of the project repo, please contact BU Spark! for more information.

---

#### **Distribution**  
- **Access Type:** This project aims to provide insight into public about MBTA's equity, please contact senior editor Paul Singer (paul_singer@wgbh.org) for access.

---

#### **Maintenance**  
- For future extensions or maintenance of the project repo, please contact BU Spark! for more information.

---

#### **Other Details**  
- Recommendations for extending the dataset include integrating longitudinal surveys and expanding demographic overlays for broader analysis.
