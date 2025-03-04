import requests

def get_weather(city):
    # URL for the weather data, using the format you mentioned
    url = f"https://wttr.in/{city}?format=%C|%t|%f"
    
    try:
        # Request the weather data from the API
        print(f"Requesting weather data for: {city}")  # Debugging line
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Print the raw response for debugging
            print(f"Raw API Response: {response.text}")  # Print raw response to debug
            
            # Split the response by the delimiter "|"
            data = response.text.split("|")
            
            # Check if we got the expected number of data parts
            if len(data) == 3:
                weather_condition = data[0].strip()
                temp_c = data[1].strip()
                temp_f = data[2].strip()

                # Basic emoji mapping for weather conditions
                emojis = {
                    "Clear": "☀️", "Sunny": "☀️", "Cloudy": "☁️",
                    "Partly cloudy": "⛅", "Rain": "🌧️", "Showers": "🌦️",
                    "Thunderstorm": "⛈️", "Snow": "❄️", "Fog": "🌫️"
                }
                # Get emoji for the weather condition, default to "🌍" if not found
                emoji = emojis.get(weather_condition, "🌍")

                # Display the weather information in a user-friendly format
                print(f"\nWeather for {city.title()}:")
                print(f"🌦️ Condition: {weather_condition} {emoji}")
                print(f"🌡️ Temperature: {temp_c}°C ({temp_f}°F)")
            else:
                print("❌ Unexpected response format. Raw data:")
                print(response.text)  # Show the raw response when the format doesn't match
        else:
            print(f"❌ Couldn't fetch weather data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching data: {e}")

# Get the city from the user and fetch the weather
city = input("Enter a city: ")
get_weather(city)
