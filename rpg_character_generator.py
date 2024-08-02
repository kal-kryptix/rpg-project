# RPG Character Generator
# Author: Starwalker18 (also known as Paincakes and Kal Kryptix)
# Allows users to create a fantasy character for a role-playing game.

import random

def roll_dice(num_dice, sides=6):
    # Roll `num_dice` dice with `sides` faces and return the total.
    return sum(random.randint(1, sides) for _ in range(num_dice))

def get_ability_points(ability_name, max_points):
    # Prompt the user to enter ability points within a valid range. (0-27 points)
    while True:
        try:
            points = int(input(f"Enter points for {ability_name} (0-{max_points}): ").strip())
            if 0 <= points <= max_points:
                return points
            else:
                print(f"Points must be between 0 and {max_points}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def allocate_points(abilities, total_points, randomize=False):
    # Allocate ability points to each ability, optional randomization
    points_allocation = {}
    remaining_points = total_points

    if randomize:
        # Randomly allocate points
        for ability in abilities:
            points = random.randint(0, remaining_points)
            points_allocation[ability] = points
            remaining_points -= points
        if remaining_points > 0:
            points_allocation[abilities[0]] += remaining_points
    else:
        # Manually allocate points
        for ability in abilities:
            print(f"Remaining points: {remaining_points}")
            points = get_ability_points(ability, remaining_points)
            points_allocation[ability] = points
            remaining_points -= points
        if remaining_points > 0:
            print(f"You have {remaining_points} points left unallocated. They will be assigned to the first ability.")
            first_ability = abilities[0]
            points_allocation[first_ability] += remaining_points

    return points_allocation

def choose_gender():
    # Prompt the user to choose a gender or select 'random' for a random gender.
    genders = ["male", "female", "nonbinary"]
    while True:
        choice = input(f"Choose gender ({', '.join(genders)}) or type 'random' for a random gender: ").strip().lower()
        if choice == 'random':
            gender = random.choice(genders)
            print(f"Randomly selected gender: {gender}")
            return gender
        elif choice in genders:
            return choice
        else:
            print("Invalid gender. Please choose from 'male', 'female', 'nonbinary' or type 'random'.")

def choose_race():
    # Prompt the user to choose a race or select 'random' for a random race.
    races = ["dwarf", "elf", "gnome", "human", "orc"]
    while True:
        race = input("Choose a race (dwarf, elf, gnome, human, orc) or type 'random' for a random race: ").strip().lower()
        if race == 'random':
            return random.choice(races)
        elif race in races:
            return race
        else:
            print("Invalid race. Please choose from 'dwarf', 'elf', 'gnome', 'human', 'orc', or type 'random'.")

combined_names = {
    ("male", "dwarf"): ["Thrain", "Gimli", "Dori", "Ori", "Bifur"],  # Inspired by Tolkien characters
    ("female", "dwarf"): ["Helga", "Frerin", "Dís", "Rósa", "Thrain"],  # Inspired by Tolkien characters
    ("male", "elf"): ["Aelar", "Galanor", "Kael", "Rondor", "Faelan"],  # Inspired by various fantasy characters
    ("female", "elf"): ["Lira", "Elenor", "Seraphina", "Nyssa", "Thalira"],  # Inspired by various fantasy characters
    ("male", "gnome"): ["Rix", "Bumble", "Fip", "Nix", "Wizzle"],  # Inspired by D&D 
    ("female", "gnome"): ["Pippa", "Luna", "Twinkle", "Fizz", "Dabble"],  # Inspired by D&D
    ("male", "human"): ["Arthas", "Uther", "Varian", "Turalyon", "Llane"], # Inspired by World of Warcraft characters
    ("female", "human"): ["Jaina", "Calia", "Sylvanas", "Tyrande", "Khadgar"], # Inspired by World of Warcraft characters
    ("male", "orc"): ["Krag", "Thrall", "Thorg", "Zug", "Brog"],  # Inspired by general fantasy and game sources (WoW)
    ("female", "orc"): ["Vara", "Grasha", "Ruk", "Zara", "Aggra"],  # Inspired by general fantasy and game sources (WoW)
    ("nonbinary", "dwarf"): ["Tarn", "Eldrin", "Bryn", "Fenn", "Torin"],  # A mix of fantasy names
    ("nonbinary", "elf"): ["Arin", "Lorien", "Dorian", "Tarian", "Zephyr"],  # A mix of fantasy names
    ("nonbinary", "gnome"): ["Rolo", "Fizz", "Wyn", "Tilly", "Zara"],  # A mix of fantasy names
    ("nonbinary", "human"): ["Riley", "Morgan", "Casey", "Avery", "Rowan"],  # A mix of fantasy names
    ("nonbinary", "orc"): ["Grim", "Korr", "Aza", "Jax", "Ryn"]  # A mix of fantasy names
}

def choose_name(gender, race):
    # Prompt the user to choose a name or select 'random' for a random name based on gender and race.
    names = combined_names.get((gender, race), [])
    
    while True:
        choice = input("Enter a name or type 'random' for a random name: ").strip()
        if choice.lower() == 'random':
            return random.choice(names)
        elif choice:
            return choice.capitalize()
        else:
            print("Invalid input. Please enter a name or type 'random'.")

def choose_class():
    # Prompt the user to choose a class or select 'random' for a random class.
    classes = ["warrior", "druid", "ranger", "rogue", "wizard"]
    while True:
        character_class = input("Choose a class (warrior, druid, ranger, rogue, wizard) or type 'random' for a random class: ").strip().lower()
        if character_class == 'random':
            return random.choice(classes)
        elif character_class in classes:
            return character_class
        else:
            print("Invalid class. Please choose from 'warrior', 'druid', 'ranger', 'rogue', 'wizard', or type 'random'.")

def choose_armor(character_class):
    # Return the type of armor based on the chosen class.
    if character_class == "ranger":
        armor_type = input("Choose armor type for ranger (leather or metal): ").strip().lower()
        while armor_type not in ["leather", "metal"]:
            print("Invalid choice. Please choose 'leather' or 'metal'.")
            armor_type = input("Choose armor type for ranger (leather or metal): ").strip().lower()
        return f"medium armor ({armor_type})"
    else:
        armor_classes = {
            "warrior": "heavy armor",
            "druid": "medium armor (non-metallic)",
            "rogue": "light or medium armor",
            "wizard": "no armor"
        }
        return armor_classes.get(character_class, "no armor")

def choose_weapons(character_class, randomize=False):
    # Prompt the user to choose weapons or randomly select weapons based on the class.
    weapons = {
        "warrior": ["greatsword", "shield", "sword", "dagger"],
        "ranger": ["shortbow", "longbow", "sword", "dagger"],
        "wizard": ["staff", "codex", "wand"],
        "rogue": ["shortbow", "dagger", "axe", "shortsword"],
        "druid": ["staff", "dagger", "mace"]
    }
    
    if character_class in weapons:
        available_weapons = weapons[character_class]
        print(f"Available weapons for {character_class}: {', '.join(available_weapons)}")
    
        # Special case for dual-wield weapons for rogues    
        if randomize:
            if character_class == "rogue":
                if random.choice([True, False]):
                    print("Randomly selected: Dual-wielding shortswords.")
                    return ["shortsword", "shortsword"]
                else:
                    return random.sample(available_weapons, 2)
            else:
                return random.sample(available_weapons, 2)
        
        if character_class == "rogue":
            print("Note: Rogues can either dual-wield shortswords or choose two different weapons. Dual-wielding shortswords means choosing two shortswords.")

        while True:
            choice = input(f"Choose 1 or 2 weapons from the above list (comma-separated): ").strip().lower().split(',')
            choice = [weapon.strip() for weapon in choice]
            
            if character_class == "rogue":
                if len(choice) == 2 and choice == ["shortsword", "shortsword"]:
                    print("You have chosen to dual-wield shortswords.")
                    return choice
                elif len(choice) == 2 and all(weapon in available_weapons for weapon in choice):
                    print("You have chosen two different weapons.")
                    return choice
                else:
                    print("Rogues can either dual-wield shortswords or choose two different weapons. Please choose again.")
            elif len(choice) == 1 and choice[0] in available_weapons or len(choice) == 2 and all(weapon in available_weapons for weapon in choice):
                return choice
            else:
                print("Invalid choices. Ensure you choose weapons from the list and no more than 2.")

def get_adventurers_kit():
    # Return the standard items included in the adventurer's kit.
    return ["Backpack", "Bedroll", "Mess Kit", "Rations (1 week)", "Tinderbox", "Torches (10)", "Waterskin", "50 feet of rope"]

def main():
    # Main function to create a character
    abilities = ["Strength", "Dexterity", "Intelligence", "Charisma"]
    total_points = 27  # Fixed number of ability points

    print("Welcome to Ethrendor, adventurer.")
    print("Please start the game by creating a character.")
    
    while True:
        # Choose a name
        gender = choose_gender()  # Get gender
        race = choose_race()  # Get race
        name = choose_name(gender, race)
        
        # Choose class
        character_class = choose_class()
        
        # Determine armor class based on character class
        armor = choose_armor(character_class)
        
        # Randomize weapons (optional)
        random_weapons = input("Would you like to randomly select weapons? (y/n): ").strip().lower() == 'y'
        weapons = choose_weapons(character_class, randomize=random_weapons)
        
        # Get the adventurer's kit
        adventurers_kit = get_adventurers_kit()
        
        # Randomize ability points (optional)
        random_abilities = input("Would you like to randomly allocate ability points? (y/n): ").strip().lower() == 'y'
        points_allocation = allocate_points(abilities, total_points, randomize=random_abilities)
        
        # Print character summary
        print(f"Character Summary:")
        print(f"Name: {name}")
        print(f"Gender: {gender.capitalize()}")
        print(f"Race: {race.capitalize()}")
        print(f"Class: {character_class.capitalize()}")
        print(f"Armor: {armor.capitalize()}")
        print(f"Weapons: {', '.join(weapon.capitalize() for weapon in weapons)}")
        print(f"Adventurer's Kit: {', '.join(adventurers_kit)}")
        print("Ability Points Allocation:")
        for ability, points in points_allocation.items():
            print(f"{ability.capitalize()}: {points}")
        
        while True:
            another = input("Character creation complete. Make another one? (y/n): ").strip().lower()
            if another in ('y', 'n'):
                if another == 'n':
                    print("Thank you for playing. Farewell, adventurer!")
                    return  # Exits the main function
                break  # Breaks inner loop to create another character
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
