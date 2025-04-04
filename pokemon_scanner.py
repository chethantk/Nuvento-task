import requests
import sys
import json

# Function to fetch data for a given Pokemon
def fetch_pokemon_data(pokemon_name):
    # URL for the PokéAPI with the given Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        
        # Parse the JSON response
        pokemon_data = response.json()
        
        # Extract relevant data
        data = {
            "name": pokemon_data["name"],
            "base_experience": pokemon_data["base_experience"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
        }
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Main function to handle command-line argument and display the data
def main():
    # Check if the user passed a Pokémon name as an argument
    if len(sys.argv) != 2:
        print("Usage: python pokemon_scanner.py <pokemon_name>")
        sys.exit(1)
    
    pokemon_name = sys.argv[1]
    
    # Fetch Pokémon data
    data = fetch_pokemon_data(pokemon_name)
    
    if data:
        # Print the output in JSON format
        print(json.dumps(data, indent=4))

# Run the script
if __name__ == "__main__":
    main()

