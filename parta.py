import requests

def get_weather():
    """
    Fetches weather information from the wttr.in API based on user input.
    """
    city = input("Enter a city or location: ")
    url = f"https://wttr.in/{city}?format=%C+%t+%f"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.text.split()
        condition, temp_c, temp_f = weather_data[0], weather_data[1], weather_data[2]
        print(f"Weather in {city}: {condition}, {temp_c}C ({temp_f}F)")
        
        # Bonus: Add weather emoji
        emojis = {"Clear": "☀", "Cloudy": "☁", "Rain": "🌧", "Snow": "❄"}
        print(f"Emoji: {emojis.get(condition, '🌍')}")
    else:
        print("Failed to retrieve weather data.")


