import requests
import sys
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        pokemon_data = response.json()
        
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python pokemon_scanner.py <pokemon_name>")
        sys.exit(1)
    
    pokemon_name = sys.argv[1]
    
    data = fetch_pokemon_data(pokemon_name)
    
    if data:
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()

