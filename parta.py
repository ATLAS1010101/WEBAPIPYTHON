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

def menu():
    """
    Menu system for Part B: Using a unique API (Example: Dog CEO API for random dog images).
    """
    print("Choose an option:")
    print("1. Get a random dog image")
    print("2. Get a list of dog breeds")
    print("3. Get a random image of a specific breed")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            print("Random Dog Image URL:", response.json()["message"])
    
    elif choice == "2":
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        if response.status_code == 200:
            breeds = response.json()["message"].keys()
            print("Dog Breeds:", ", ".join(breeds))
    
    elif choice == "3":
        breed = input("Enter a breed name (e.g., bulldog): ")
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        if response.status_code == 200:
            print(f"Random {breed} image:", response.json()["message"])
        else:
            print("Breed not found.")
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    print("Part A: Weather API")
    get_weather()
    print("\nPart B: Dog Image API")
    menu()
