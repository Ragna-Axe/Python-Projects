# game.py
import time
import random
from characters import Character
from rooms import level1_room1, move, monsters

current_room = level1_room1  # Initialize the current room globally

def move(current_room, direction):
    """
    Move the player to the next room based on the given direction.
    Args:
    - current_room (Room): The current room the player is in.
    - direction (str): The direction to move ('n', 's', 'w', 'e', 'u', 'd').
    Returns:
    - Room: The next room the player is moved to.
    """
    if direction in current_room.connections:
        return current_room.connections[direction]
    else:
        print("Just keep swimming.")
        return current_room
    
def combat(player, monster):
    print(f"A wild {monster['name']} appears!")

    while player.health > 0 and monster['health'] > 0:
        choice = player.combat_options()

        if choice == "1":
            player_attack = random.randint(5, 20)
            print(f"\nYou strike the {monster['name']} with {player_attack} damage.")
            monster['health'] -= player_attack
        elif choice == "2":
            print(f"You dodge the {monster['name']}'s attack.")
        else:
            print("Invalid choice. Please choose 1 or 2.")

        if monster['health'] <= 0:
            print(f"You defeated the {monster['name']}!\n")
            player.level_up()
            return True

        monster_attack = random.randint(8, 15)
        print(f"The {monster['name']} retaliates with {monster_attack} damage.")
        player.health -= monster_attack
        print(f"Your health: {player.health}\n")

    print(f"You were defeated by the {monster['name']}. Game over.")
    return False

def enter_room(current_room):
    print(f"You are in {current_room.name}. {current_room.description}")

    if current_room.monster_encounter:
        if combat(player, 50):  # Adjust the monster_health parameter as needed
            current_room.enter_next()
    else:
        next_move = current_room.enter_next()

    def combat_options(self):
        print("Combat Options:")
        print("1. Strike the monster")
        print("2. Dodge the monster's attack")

        choice = input("Choose your action (1 or 2): ")
        return choice
    
def show_character_info():
    print(f"\nCharacter Information:")
    print(f"Name: {player.name}")
    print(f"Race: {player.race}")
    print(f"Sex: {player.sex}")
    print(f"Class: {player.character_class}")
    print(f"Health: {player.health}\n")
    
def create_character():
    print("Let's create your character.")

    # Character Name
    name = input("Enter your character's name: ")

    # Character Race
    races = ['Orc', 'Human', 'Elf', 'Dwarf']
    print(f"Choose your character's race: {', '.join(races)}")
    race = input().capitalize()
    while race not in races:
        print("Invalid choice. Please choose from the provided races.")
        race = input().capitalize()

    # Character Sex
    print("Choose your character's sex: Female or Male")
    sex = input().capitalize()
    while sex not in ['Female', 'Male']:
        print("Invalid choice. Please choose Female or Male.")
        sex = input().capitalize()

    # Character Class
    classes = ['Warrior', 'Mage', 'Paladin', 'Ranger']
    print(f"Choose your character's class: {', '.join(classes)}")
    character_class = input().capitalize()
    while character_class not in classes:
        print("Invalid choice. Please choose from the provided classes.")
        character_class = input().capitalize()

    return Character(name, race, sex, character_class)

def world_setting():
    print("Welcome to the mysterious world of magic and monsters.")
    # Implement details about different regions, challenges, and creatures

def culture_clash():
    print("You, a modern-day adventurer, find yourself in a serious and magical world.")
    print("The locals might find your laid-back demeanor unusual.")
    # Implement culture clash elements here

def humor_and_adventure():
    print("Embark on a journey filled with humor, political intrigue, and adventure.")
    # Implement humorous dialogues, political events, and adventurous scenarios

def unique_challenges(current_room):
    """
    Introduce unique challenges and encounters based on the current room.
    Args:
    - current_room (Room): The current room the player is in.
    """
    if current_room.monster_encounter:
        monster_type = current_room.monster_encounter
        if monster_type in monsters:
            monster = monsters[monster_type]
            print(f"You encounter a {monster['name']}! Get ready for battle.")
            if combat(player, monster):
                print(f"You defeated the {monster['name']}!\n")
    elif current_room.monster_encounter == "cannibals":
        cannibals = {"name": "Cannibals", "health": 40, "attack_name": "Cannibal Bite"}
        print("You encounter a group of cannibals! Prepare for battle.")
        if combat(player, cannibals):
            print("You defeated the cannibals!\n")
    elif current_room.monster_encounter == "cultists":
        cultists = {"name": "Cultists", "health": 30, "attack_name": "Cultist Curse"}
        print("A cultist ritual is taking place. They notice you and attack!")
        if combat(player, cultists):
            print("You disrupted the cultist ritual and emerged victorious!\n")
    elif current_room.monster_encounter == "wizards":
        wizards = {"name": "Wizards", "health": 50, "attack_name": "Wizard's Fireball"}
        print("A group of wizards challenges you to a magical duel!")
        if combat(player, wizards):
            print("You outsmarted the wizards and won the magical duel!\n")
    elif current_room.monster_encounter == "random_monster":
        random_monster = {"name": "Random Monster", "health": random.randint(30, 60), "attack_name": "Surprise Attack"}
        print("A random monster appears! Brace yourself for a surprise attack.")
        if combat(player, random_monster):
            print("You defeated the random monster!\n")


def funny_trap():
    """
    Introduce a funny trap and add some humor to the game.
    """
    print("Oops! You stepped on a banana peel. The ground is slippery!")
    print("You start sliding uncontrollably but manage to regain balance.")
    print("Luckily, it was just a funny trap, and you emerge unharmed.")

def enter_room(current_room):
    print(f"You are in {current_room.name}. {current_room.description}")

    if current_room.monster_encounter:
        unique_challenges(current_room)
        current_room.enter_next()
    elif current_room.name == "Level 2, Room 3":
        funny_trap()
        current_room.enter_next()
    else:
        current_room.enter_next()


def character_progression(player):
    print("Embark on a journey of self-discovery and power progression.")
    player.acquire_evil_powers()
    # Implement a progression system combining cultivation and LitRPG elements

def loot_and_exploration():
    print("Explore the world, discover hidden treasures, and unravel the mysteries.")
    # Implement loot system and exploration mechanics

def introduction():
    print("Welcome to Dragons Breath Adventure Game!")
    time.sleep(1)
    world_setting()
    culture_clash()

def main():
    introduction()

    # Create Character
    global player
    player = create_character()

    # Initial room (adjust this based on your game logic)
    current_room = level1_room1

    while True:
        show_character_info()
        next_room = enter_room(current_room)
        unique_challenges(current_room)
        character_progression(player)
        humor_and_adventure()
        loot_and_exploration()
        # Update the current_room based on player's choice or game logic
        current_room = move(current_room, next_room)

if __name__ == "__main__":
    main()
