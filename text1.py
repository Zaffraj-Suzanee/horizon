import requests
import pandas as pd

# Call the new API
url = "https://weather-api167.p.rapidapi.com/api/weather/forecast"
querystring = {
    "place": "London,GB",  # Change this to your desired city and country (e.g., Colombo)
    "cnt": "3",            # Number of forecast entries (3 in this case)
    "units": "standard",   # Temperature units (standard is Kelvin)
    "type": "three_hour",  # Forecast type (3-hour forecast)
    "mode": "json",        # Response format (JSON)
    "lang": "en"           # Language for the response
}

headers = {
    "Accept": "application/json",
    "x-rapidapi-host": "weather-api167.p.rapidapi.com",
    "x-rapidapi-key": "6e6c9f9879msh1b2771c071a94d4p1edef1jsn5f942bee9876"
}

# Make the request to the API
response = requests.get(url, headers=headers, params=querystring)

# Check the response
if response.status_code == 200:
    weather_data = response.json()
    print("✅ Weather data fetched successfully!")

    # Use pandas to display the forecast data
    # Assuming the response has a 'list' key for forecast details
    #(adapt this to your API response structure)
    if 'list' in weather_data:
        forecast_data = weather_data['list']
        df = pd.DataFrame(forecast_data)
        print("\n🌦️ Weather Forecast:")
        print(df)

        # Additional info
        print("\n📊 Number of records:", len(df))
        print("🧾 Columns:", list(df.columns))
    else:
        print("❌ No forecast data available.")
else:
    print("❌ Failed to fetch data. Error code:", response.status_code)