import requests

def menu():
    """
    Menu system for interacting with the Dog CEO API. It allows users to:
    1. Get a random dog image
    2. Get a list of all dog breeds
    3. Get a random image of a specific dog breed
    """
    # Display menu options to the user
    print("Choose an option:")
    print("1. Get a random dog image")  # Option to get a random dog image
    print("2. Get a list of dog breeds")  # Option to get a list of all dog breeds
    print("3. Get a random image of a specific breed")  # Option to get a random image of a specific breed
    
    # Take user input for their choice
    choice = input("Enter choice (1/2/3): ")

    # Option 1: Get a random dog image
    if choice == "1":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        # Check if the API response is successful (status code 200)
        if response.status_code == 200:
            # Print the URL of the random dog image
            print("Random Dog Image URL:", response.json()["message"])

    # Option 2: Get a list of all dog breeds
    elif choice == "2":
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        # Check if the API response is successful (status code 200)
        if response.status_code == 200:
            # Get the list of dog breeds from the API response and display them
            breeds = response.json()["message"].keys()
            print("Dog Breeds:", ", ".join(breeds))

    # Option 3: Get a random image of a specific breed
    elif choice == "3":
        breed = input("Enter a breed name (e.g., bulldog): ")  # Ask the user for a breed
        # Request a random image for the specified breed
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        # Check if the API response is successful (status code 200)
        if response.status_code == 200:
            # Print the URL of the random breed image
            print(f"Random {breed} image:", response.json()["message"])
        else:
            # If the breed was not found, inform the user
            print("Breed not found.")

    # If the user inputs an invalid choice
    else:
        print("Invalid choice. Try again.")

# Main entry point to run the program
if __name__ == "__main__":
    menu()  # Call the menu function to start the Dog Image API interaction
