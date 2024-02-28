
import time
import random

class Character:
    def __init__(self, name, race, sex, character_class):
        self.name = name
        self.race = race
        self.sex = sex
        self.character_class = character_class
        self.health = 100
        self.level = 1
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.magic = 10

    def level_up(self):
        print("Congratulations! You leveled up!")
        self.level += 1
        stat_gain_percentage = 5

        # Increase all stats by 5%
        self.strength = int(self.strength * (1 + stat_gain_percentage / 100))
        self.health = 100  # Restore health to full
        self.dexterity = int(self.dexterity * (1 + stat_gain_percentage / 100))
        self.intelligence = int(self.intelligence * (1 + stat_gain_percentage / 100))
        self.magic = int(self.magic * (1 + stat_gain_percentage / 100))

def introduction():
    print("Welcome to Dragons Breath Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious land. Create your character and explore.")

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

def show_character_info():
    print(f"\nCharacter Information:")
    print(f"Name: {player.name}")
    print(f"Race: {player.race}")
    print(f"Sex: {player.sex}")
    print(f"Class: {player.character_class}")
    print(f"Health: {player.health}\n")

def fight_monster():
    print("You encounter a fierce monster!")

    # Simulate a simple fight
    monster_health = random.randint(10, 50)
    print(f"The monster has {monster_health} health.")

    while player.health > 0 and monster_health > 0:
        print("Choose your action:")
        print("1. Strike the monster")
        print("2. Dodge the monster's attack")

        user_choice = input("Enter your choice (1 or 2): ")

        if user_choice == "1":
            # Player chooses to strike the monster
            player_attack = random.randint(5, 20)
            print(f"\nYou attack the monster for {player_attack} damage.")
            monster_health -= player_attack
            if monster_health <= 0:
                print("You defeated the monster!\n")
                player.level_up()
                return True
        elif user_choice == "2":
            # Player chooses to dodge the monster's attack
            monster_attack = random.randint(5, 10)
            print(f"\nYou attempt to dodge the monster's attack.")
            dodge_success = random.choice([True, False])
            if dodge_success:
                print("You successfully dodge the attack!")
            else:
                print(f"The monster hits you for {monster_attack} damage.")
                player.health -= monster_attack
                print(f"Your health: {player.health}\n")
        else:
            print("Invalid choice. Please enter 1 to strike or 2 to dodge.")

    print("You were defeated by the monster. Game over.")
    return False


def enter_room():
    print(f"You are in {current_room.name}. {current_room.description}")

    if current_room.monster_encounter():
        if fight_monster():
            current_room.enter_next()
    else:
        current_room.enter_next()

def move(direction):
    if direction in current_room.connections:
        return globals()[current_room.connections[direction]]

    print("Invalid direction. Try again.")
    return current_room

class Room:
    def __init__(self, name, description, connections, monster_encounter=None):
        self.name = name
        self.description = description
        self.connections = connections
        self.monster_encounter = monster_encounter

    def enter_next(self):
        print("Choose your next move (n/s/w/e/u/d/quit): ")
        next_move = input().lower()
        if next_move == 'quit':
            print("Thanks for playing. Goodbye!")
            quit()
        return move(next_move)

# Define monsters
def monster_encounter():
    monsters = ["Goblin", "Skeleton", "Orc", "Troll"]
    return random.choice(monsters) == "Goblin"

# Define rooms
level1_room1 = Room("Level 1, Room 1", "a dimly lit room", {"e": "level1_room2"}, monster_encounter)
level1_room2 = Room("Level 1, Room 2", "a room with a strange portal", {"w": "level1_room1", "e": "level1_room3"}, monster_encounter)
level1_room3 = Room("Level 1, Room 3", "a room with a hidden door", {"w": "level1_room2", "d": "level2_room1"}, monster_encounter)

level2_room1 = Room("Level 2, Room 1", "a room with a magical pool", {"u": "level1_room3", "e": "level2_room2"}, monster_encounter)
level2_room2 = Room("Level 2, Room 2", "a room with ancient artifacts", {"w": "level2_room1", "e": "level2_room3"}, monster_encounter)
level2_room3 = Room("Level 2, Room 3", "a room with a mysterious statue", {"w": "level2_room2", "d": "level3_room1"}, monster_encounter)

level3_room1 = Room("Level 3, Room 1", "a room with a glowing crystal", {"u": "level2_room3", "e": "level3_room2"}, monster_encounter)
level3_room2 = Room("Level 3, Room 2", "a room with swirling mist", {"w": "level3_room1", "e": "level3_room3"}, monster_encounter)
level3_room3 = Room("Level 3, Room 3", "a room with a massive door", {"w": "level3_room2", "d": "level4_room1"}, monster_encounter)

level4_room1 = Room("Level 4, Room 1", "a room with echoes", {"u": "level3_room3", "e": "level4_room2"}, monster_encounter)
level4_room2 = Room("Level 4, Room 2", "a room with strange markings", {"w": "level4_room1", "e": "level4_room3"}, monster_encounter)
level4_room3 = Room("Level 4, Room 3", "a room with a dark portal", {"w": "level4_room2", "d": "level5_room1"}, monster_encounter)

level5_room1 = Room("Level 5, Room 1", "a room with mystical symbols", {"u": "level4_room3", "e": "level5_room2"}, monster_encounter)
level5_room2 = Room("Level 5, Room 2", "a room with glowing orbs", {"w": "level5_room1", "e": "level5_room3"}, monster_encounter)
level5_room3 = Room("Level 5, Room 3", "a room with a powerful artifact", {"w": "level5_room2", "d": "exit"}, monster_encounter)

exit_room = Room("Exit", "the exit room", {}, None)

# Set initial room
current_room = level1_room1

def main():
    introduction()

    # Create Character
    global player
    player = create_character()

    while True:
        show_character_info()
        enter_room()

if __name__ == "__main__":
    main()
