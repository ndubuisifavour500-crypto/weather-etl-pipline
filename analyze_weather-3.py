import pandas as pd

# Load cleaned data
df = pd.read_csv('weather_data_cleaned.csv')

print("="*70)
print("WEATHER DATA ANALYSIS - 4 CITIES")
print("="*70)

print("\n📊 Dataset Overview:")
print(df[['city_name', 'country', 'temperature_c', 'humidity', 'weather_main']])

print("\n" + "="*70)
print("KEY FINDINGS:")
print("="*70)

# 1. Temperature comparison
print("\n1️⃣ TEMPERATURE COMPARISON:")
print(f"   Hottest City: {df.loc[df['temperature_c'].idxmax(), 'city_name']} ({df['temperature_c'].max()}°C)")
print(f"   Coolest City: {df.loc[df['temperature_c'].idxmin(), 'city_name']} ({df['temperature_c'].min()}°C)")
print(f"   Average Temp: {df['temperature_c'].mean():.2f}°C")

# 2. Humidity
print("\n2️⃣ HUMIDITY ANALYSIS:")
highest_humidity_idx = df['humidity'].idxmax()
print(f"   Highest Humidity: {df.loc[highest_humidity_idx, 'city_name']} ({df.loc[highest_humidity_idx, 'humidity']}%)")
print(f"   Average Humidity: {df['humidity'].mean():.1f}%")

# 3. Weather conditions
print("\n3️⃣ WEATHER CONDITIONS:")
weather_counts = df['weather_main'].value_counts()
for weather, count in weather_counts.items():
    cities = df[df['weather_main'] == weather]['city_name'].tolist()
    print(f"   {weather}: {', '.join(cities)}")

# 4. Wind analysis
print("\n4️⃣ WIND SPEED:")
print(f"   Windiest City: {df.loc[df['wind_speed_ms'].idxmax(), 'city_name']} ({df['wind_speed_ms'].max():.2f} m/s)")
print(f"   Average Wind: {df['wind_speed_ms'].mean():.2f} m/s")

# 5. Feels like temperature
print("\n5️⃣ PERCEIVED TEMPERATURE (Feels Like):")
print(f"   Lagos feels {df.loc[0, 'feels_like_c'] - df.loc[0, 'temperature_c']:.2f}°C warmer than actual")
print(f"   Max 'Feels Like': {df['feels_like_c'].max():.2f}°C in {df.loc[df['feels_like_c'].idxmax(), 'city_name']}")

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print("""
✅ Lagos is the hottest (27.59°C) with tropical humidity (79%)
✅ Nairobi is the coolest (23.62°C) with dry conditions
✅ 2 cities (Lagos, Accra) experiencing rain
✅ 2 cities (Nairobi, London) have clear/cloudy skies
✅ Accra has highest humidity at 81% - very humid conditions
✅ Wind speeds generally low across all cities (2-5 m/s)
""")

print("="*70)
