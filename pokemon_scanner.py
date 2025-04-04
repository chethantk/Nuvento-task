import requests
import sys
import json

def get_pokemon_details(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(json.dumps({"error": "Pokémon not found"}))
        return

    data = response.json()
    result = {
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
    }

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Please provide a Pokémon name"}))
    else:
        get_pokemon_details(sys.argv[1])

