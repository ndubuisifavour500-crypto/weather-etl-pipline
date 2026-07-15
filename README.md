# Weather Data ETL Pipeline

## Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline that collects real-time weather data from multiple cities, cleans and structures it, and performs basic analysis. The pipeline showcases data engineering fundamentals critical for roles in monitoring & evaluation and data analytics at international development organizations.

**Author:** Ndubuisi Favour Adaku  
**Organization:** AnalystLab Africa - Batch B (Week 7)  
**Date:** July 2026

---

## Data Source

**OpenWeather API** (https://openweathermap.org/api)

- Free tier API for current weather data
- Real-time meteorological information
- Coverage: Global cities
- Cities analyzed: Lagos (Nigeria), Accra (Ghana), Nairobi (Kenya), London (UK)

---

## ETL Process

### 1. **Extract (Task 1)**
- Connected to OpenWeather API using Python `requests` library
- Retrieved current weather data for 4 cities
- Extracted fields: temperature, humidity, pressure, wind speed, weather conditions, coordinates
- Output: Raw JSON data → `current_weather_4cities.csv`

### 2. **Transform (Task 2)**
- Loaded raw CSV into Pandas DataFrame
- Data cleaning operations:
  - Standardized column naming (snake_case)
  - Validated data types (float, int, string)
  - Handled missing values (filled with 0)
  - Sorted data by temperature (descending)
  - Rounded numerical values to 2 decimals
  - Added extraction timestamp
- Reduced dataset from 15 columns to 11 key columns
- Output: Clean dataset → `weather_data_cleaned.csv`

### 3. **Load (Task 3)**
- Stored transformed data in CSV format (CSV chosen for simplicity and portability)
- File saved: `weather_data_cleaned.csv`
- Ready for immediate analysis and sharing

### 4. **Analysis (Task 4)**
- **Temperature Analysis:** Compared temperatures across 4 cities
- **Humidity Analysis:** Identified highest humidity (Accra: 81%)
- **Weather Patterns:** Categorized conditions (Rain vs. Clouds)
- **Wind Speed:** Calculated averages and identified windiest city
- **Perceived Temperature:** Analyzed "feels like" vs. actual temperature

---

## Key Findings

| Metric | Finding |
|--------|---------|
| **Hottest City** | Lagos (27.59°C) |
| **Coolest City** | London (22.55°C) |
| **Highest Humidity** | Accra (81%) |
| **Windiest City** | Accra (4.96 m/s) |
| **Average Temperature** | 24.91°C |
| **Weather Split** | 50% Rain, 50% Clouds |

### Key Insights:
1. **Tropical vs. Temperate:** African cities (Lagos, Accra, Nairobi) average 25.7°C vs. London at 22.55°C
2. **Humidity Correlation:** West African cities (Lagos, Accra) show high humidity with rain conditions
3. **Perceived Heat:** Lagos feels 3.38°C warmer than actual temperature due to humidity
4. **Weather Stability:** London and Nairobi show stable cloud cover; Lagos and Accra experiencing active precipitation

---

## Tools Used

| Tool | Purpose |
|------|---------|
| **Python 3.12** | Core programming language |
| **Pandas** | Data manipulation and transformation |
| **Requests** | API integration and HTTP requests |
| **OpenWeather API** | Weather data source |

---

## Project Files

```
weather-etl-pipeline/
├── README.md                          # Project documentation
├── extract_weather.py                 # Task 1: API extraction script
├── transform_weather.py               # Task 2: Data transformation script
├── analyze_weather.py                 # Task 4: Data analysis script
├── current_weather_4cities.csv        # Raw extracted data
├── weather_data_cleaned.csv           # Transformed & loaded data
└── demo_video_link.txt                # Screen recording link
```

---

## How to Reproduce

### Prerequisites
```bash
pip install pandas requests
```

### Step 1: Extract Data
```bash
python extract_weather.py
```
Fetches current weather for 4 cities from OpenWeather API.

### Step 2: Transform Data
```bash
python transform_weather.py
```
Cleans and structures the extracted data.

### Step 3: Analyze Data
```bash
python analyze_weather.py
```
Generates insights and summary statistics.

---

## Key Learnings

✅ **API Integration:** Successfully connected to real-world APIs for data retrieval  
✅ **Data Cleaning:** Hands-on experience with handling raw data before analysis  
✅ **Pandas Proficiency:** DataFrame manipulation, filtering, and transformations  
✅ **ETL Best Practices:** Modular script design, error handling, and documentation  
✅ **Real-World Relevance:** Understanding data pipelines critical for M&E work at organizations like FAO/WFP

---

## Future Improvements

- [ ] Automate data collection at hourly intervals
- [ ] Store data in SQLite database for historical tracking
- [ ] Create visualization dashboard (matplotlib/seaborn)
- [ ] Add weather forecast data (next 5 days)
- [ ] Implement error logging and retry mechanisms
- [ ] Deploy as scheduled cloud function (Google Cloud Functions)

---

## Professional Application

This pipeline demonstrates core competencies for M&E roles at international development organizations:

- **Data Collection:** Automated, reliable data gathering from external sources
- **Data Quality:** Cleaning and validation workflows
- **Analysis-Ready Format:** Transforming raw data into actionable insights
- **Documentation:** Clear processes for reproducibility and knowledge transfer

---

## Contact & Attribution

**Project:** Week 7 - Data Pipelines & Automation  
**Organization:** AnalystLab Africa  
**Batch:** B (June - August 2026)  

---

*Last updated: July 14, 2026*
