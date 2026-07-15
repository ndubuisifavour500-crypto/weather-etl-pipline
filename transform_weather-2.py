import pandas as pd
from datetime import datetime

# Load current weather data (4 cities)
df = pd.read_csv('current_weather_4cities.csv')

print("="*70)
print("WEATHER DATA TRANSFORMATION")
print("="*70)

print("\n📊 Original data:")
print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
print(df)

# TRANSFORM: Basic cleaning
print("\n" + "="*70)
print("CLEANING & TRANSFORMING...")
print("="*70)

# 1. Add extraction timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df['extracted_at'] = timestamp

# 2. Select only useful columns for analysis
columns_to_keep = [
    'city_name', 'country', 'temperature_c', 'feels_like_c', 
    'humidity', 'pressure_hpa', 'weather_main', 'weather_description',
    'wind_speed_ms', 'clouds_percent', 'extracted_at'
]

df_clean = df[columns_to_keep].copy()

# 3. Round temperature to 2 decimals
df_clean['temperature_c'] = df_clean['temperature_c'].round(2)
df_clean['feels_like_c'] = df_clean['feels_like_c'].round(2)
df_clean['wind_speed_ms'] = df_clean['wind_speed_ms'].round(2)

# 4. Handle missing values (fill with 0 for numeric, 'Unknown' for text)
df_clean = df_clean.fillna(0)

# 5. Sort by temperature (highest first)
df_clean = df_clean.sort_values('temperature_c', ascending=False).reset_index(drop=True)

print("\n✅ Cleaned data:")
print(df_clean)

# LOAD: Save to CSV
output_file = 'weather_data_cleaned.csv'
df_clean.to_csv(output_file, index=False)
print(f"\n✅ Saved: {output_file}")

print("\n" + "="*70)
print("TRANSFORMATION COMPLETE!")
print("="*70)
