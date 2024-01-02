import random

player = {
    "Name": "Player",
    "Level": 1,
    "Experience": 0,
    "Materials": {
        "wood": 0,
        "stone": 0,
        "gold": 0
    }
}

# What type of monsters do I want
monsters = [
    {"name": "Goblin", "level": 1, "experience": 20},
    {"name": "Orc", "level": 2, "experience": 50},
    {"name": "Dragon", "level": 5, "experience": 200}
]

# Function for gathering materials
def gatherMaterials():
    material = random.choice(["wood", "stone", "gold"])
    player["Materials"][material] += 1
    print(f"You gathered 1 {material}")

# Simple fight function
def fightMonsters():
    selected_monster = random.choice(monsters)
    print(f"A wild {selected_monster['name']} appeared")
    if player["Level"] >= selected_monster["level"]:
        print(f"{player['Name']} defeated a {selected_monster['name']}")
        player["Experience"] += selected_monster["experience"]
        print(f"You gained {selected_monster['experience']} experience points!")
    else:
        print(f"The monster is too strong. {player['Name']} runs away before being spotted")

def LevelUp():
    if player['Experience'] >= 100 * player['Level']:
        player['Level'] += 1
        player['Experience'] = 0
        print(f"Congratulations! You've reached level {player['Level']}!")

if __name__ == "__main__":
    print("Welcome to the simple RPG")
    
    player['Name'] = input("Enter a name: ")
    
    while True:
        print("\nOptions:")
        print("1. Gather materials")
        print("2. Fight monster")
        print("3. Check player info")
        print("4. Exit")
        
        choices = input("Enter your choice: ")
        if choices == "1":
            gatherMaterials()
        elif choices == "2":
            fightMonsters()
            LevelUp()
        elif choices == "3":
            print(f"Name: {player['Name']}")
            print(f"Level: {player['Level']}")
            print(f"Experience: {player['Experience']}")
            print(f"Materials:")
            for material, amount in player['Materials'].items():
                print(f"{material.capitalize()}: {amount}")
        elif choices == "4":
            print(f"Exiting the game. See you next time {player['Name']}")
            break
        else:
            print("Invalid choice, try again")