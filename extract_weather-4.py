import requests
import pandas as pd
from datetime import datetime

API_KEY = "8b1ddcf977e12b370637a0dcd4d2051c"
cities = ['Lagos', 'Accra', 'Nairobi', 'London']
weather_data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        record = {
            'city_name': data['name'],
            'country': data['sys']['country'],
            'latitude': data['coord']['lat'],
            'longitude': data['coord']['lon'],
            'temperature_c': data['main']['temp'],
            'feels_like_c': data['main']['feels_like'],
            'temp_min_c': data['main']['temp_min'],
            'temp_max_c': data['main']['temp_max'],
            'humidity': data['main']['humidity'],
            'pressure_hpa': data['main']['pressure'],
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description'],
            'wind_speed_ms': data['wind']['speed'],
            'clouds_percent': data['clouds']['all'],
            'timestamp': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
        
        weather_data.append(record)
        print(f"OK: {city}")
        
    except Exception as e:
        print(f"ERROR {city}: {e}")

df = pd.DataFrame(weather_data)
print("\n" + "="*70)
print(df)
print("="*70)

df.to_csv('current_weather_4cities.csv', index=False)
print("\nSaved: current_weather_4cities.csv")
