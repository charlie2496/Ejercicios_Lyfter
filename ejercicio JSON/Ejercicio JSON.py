import json


def read_pokemones(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        pokemones = json.load(file)
    return pokemones


def get_pokemones_data():
    name=input("Enter the name of the Pokémon: ")
    pokemon_type=input("Enter the type of the Pokémon: ")
    level=int(input("Enter the level of the Pokémon: "))
    weight_kg=float(input("Enter the weight of the Pokémon in kg: "))
    is_shiny=input("Is the Pokémon shiny? (yes/no): ").lower() == 'yes'
    held_item=input("Enter the held item of the Pokémon: ")

    if held_item == "":
        held_item = None
    skills = input(
        "Enter the skills of the Pokémon (comma-separated): ").split(',')
    
    hp=int(input("Enter the HP of the Pokémon: "))
    attack=int(input("Enter the attack of the Pokémon: "))
    defense=int(input("Enter the defense of the Pokémon: "))
    sp_attack=int(input("Enter the special attack of the Pokémon: "))
    sp_defense=int(input("Enter the special defense of the Pokémon: "))
    speed=int(input("Enter the speed of the Pokémon: "))

    return (
        name,
        pokemon_type,
        level,
        weight_kg,
        is_shiny,
        held_item,
        skills,
        hp,
        attack,
        defense,
        sp_attack,
        sp_defense,
        speed
    )


def create_pokemon(
        name,
        pokemon_type,
        level,
        weight_kg,
        is_shiny,
        held_item,
        skills,
        hp,
        attack,
        defense,
        sp_attack,
        sp_defense,
        speed
    ):
    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
    }
    return new_pokemon

filename = 'Lista de pokemones.json'
pokemones = read_pokemones(filename)
pokemon_data = get_pokemones_data()
new_pokemon = create_pokemon(*pokemon_data)
pokemones.append(new_pokemon)
save_pokemones(filename, pokemones)

print("Pokémon added successfully!")

