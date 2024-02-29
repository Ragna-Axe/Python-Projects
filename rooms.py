class Room:
    def __init__(self, name, description, connections, monster_encounter=None):
        self.name = name
        self.description = description
        self.connections = connections
        self.monster_encounter = monster_encounter if monster_encounter else None  # Ensure it's initialized even if None

    def enter_next(self):
        print("Choose your next move (n/s/w/e/u/d/quit): ")
        next_move = input().lower()
        if next_move == 'quit':
            print("Thanks for playing. Goodbye!")
            quit()
        return move(self, next_move)


    
# Define monsters with names, health, and attack names
monsters = {
    "goblin": {"name": "Goblin", "health": 30, "attack_name": "Goblin Punch"},
    "ogre": {"name": "Ogre", "health": 50, "attack_name": "Ogre Smash"},
    "ghost": {"name": "Ghost", "health": 40, "attack_name": "Spooky Specter"},
    "dragon": {"name": "Dragon", "health": 80, "attack_name": "Dragon Breath"},
}

# Define rooms with random monster encounters
level1_room1 = Room("Level 1, Room 1", "a dimly lit cavern with glowing crystals", {"e": "level1_room2", "s": "level2_room"}, ["goblin", "skeleton", "spider"])
level1_room2 = Room("Level 1, Room 2", "a room filled with ancient tomes and magical artifacts", {"w": "level1_room1", "e": "level1_room3"}, ["ogre", "rat", "bat"])
level1_room3 = Room("Level 1, Room 3", "a hidden chamber with a mystical portal", {"w": "level1_room2", "s": "level2_room2"}, ["ghost", "zombie", "slime"])

level2_room1 = Room("Level 2, Room 1", "a forest with talking trees and enchanted creatures", {"n": "level1_room1", "e": "level2_room2", "s": "level3_room1"}, ["ogre", "rat", "bat"])
level2_room2 = Room("Level 2, Room 2", "a spooky graveyard with restless spirits", {"w": "level2_room1", "e": "level2_room3"}, ["ghost", "zombie", "slime"])
level2_room3 = Room("Level 2, Room 3", "a cave with bioluminescent fungi and ancient inscriptions", {"w": "level2_room2", "s": "level3_room2"}, ["goblin", "skeleton", "spider"])

level3_room1 = Room("Level 3, Room 1", "a city of magical beings with bustling markets", {"n": "level2_room1", "e": "level3_room2", "s": "level4_room1"}, ["harpy", "centaur", "gargoyle"])
level3_room2 = Room("Level 3, Room 2", "an underwater grotto with merfolk and hidden treasures", {"w": "level3_room1", "e": "level3_room3"}, ["kraken", "siren", "sea serpent"])
level3_room3 = Room("Level 3, Room 3", "a volcano summit with fire elementals and molten rocks", {"w": "level3_room2", "s": "level4_room2"}, ["fire_elemental", "magma_hound", "lava_spider"])

level4_room1 = Room("Level 4, Room 1", "a celestial observatory with floating islands", {"n": "level3_room1", "e": "level4_room2", "s": "level5_room1"}, ["dragon", "griffin", "pegasus"])
level4_room2 = Room("Level 4, Room 2", "a desert oasis with mythical creatures and hidden treasures", {"w": "level4_room1", "e": "level4_room3"}, ["manticore", "sphinx", "sand_worm"])
level4_room3 = Room("Level 4, Room 3", "a snowy tundra with ice giants and frozen artifacts", {"w": "level4_room2", "s": "level5_room2"}, ["ice_giant", "frost_drake", "snow_owl"])

level5_room1 = Room("Level 5, Room 1", "an otherworldly dimension with shifting landscapes", {"n": "level4_room1", "e": "level5_room2"}, ["shadow_dragon", "chimera", "banshee"])
level5_room2 = Room("Level 5, Room 2", "a cosmic library with knowledge beyond mortal comprehension", {"w": "level5_room1", "s": "exit"}, ["elder_god", "void_specter", "astral_wyrm"])

# Define the final boss for the exit room
exit_room = Room("Exit", "the exit room", {}, ["Eragon", "Dragon King"])


# Define rooms
level1_room1 = Room("Level 1, Room 1", "a dimly lit cavern with glowing crystals", {"e": "level1_room2", "s": "level2_room1"})
level1_room2 = Room("Level 1, Room 2", "a room filled with ancient tomes and magical artifacts", {"w": "level1_room1", "e": "level1_room3"})
level1_room3 = Room("Level 1, Room 3", "a hidden chamber with a mystical portal", {"w": "level1_room2", "s": "level2_room2"})

level2_room1 = Room("Level 2, Room 1", "a forest with talking trees and enchanted creatures", {"n": "level1_room1", "e": "level2_room2", "s": "level3_room1"})
level2_room2 = Room("Level 2, Room 2", "a spooky graveyard with restless spirits", {"w": "level2_room1", "e": "level2_room3"})
level2_room3 = Room("Level 2, Room 3", "a cave with bioluminescent fungi and ancient inscriptions", {"w": "level2_room2", "s": "level3_room2"})

level3_room1 = Room("Level 3, Room 1", "a city of magical beings with bustling markets", {"n": "level2_room1", "e": "level3_room2", "s": "level4_room1"})
level3_room2 = Room("Level 3, Room 2", "an underwater grotto with merfolk and hidden treasures", {"w": "level3_room1", "e": "level3_room3"})
level3_room3 = Room("Level 3, Room 3", "a volcano summit with fire elementals and molten rocks", {"w": "level3_room2", "s": "level4_room2"})

level4_room1 = Room("Level 4, Room 1", "a celestial observatory with floating islands", {"n": "level3_room1", "e": "level4_room2", "s": "level5_room1"})
level4_room2 = Room("Level 4, Room 2", "a desert oasis with mythical creatures and hidden treasures", {"w": "level4_room1", "e": "level4_room3"})
level4_room3 = Room("Level 4, Room 3", "a snowy tundra with ice giants and frozen artifacts", {"w": "level4_room2", "s": "level5_room2"})

level5_room1 = Room("Level 5, Room 1", "an otherworldly dimension with shifting landscapes", {"n": "level4_room1", "e": "level5_room2"})
level5_room2 = Room("Level 5, Room 2", "a cosmic library with knowledge beyond mortal comprehension", {"w": "level5_room1", "s": "exit"})
exit_room = Room("Exit", "the exit room", {})

# Set initial room
current_room = level1_room1

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
        print("I don't think this is the direction you are looking for.")
        return current_room