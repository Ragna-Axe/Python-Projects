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

    def acquire_evil_powers(self):
        print("You feel a surge of dark energy as evil powers start to manifest.")
        # Implement the acquisition of evil powers here

def move(current_room, direction):
    if direction in current_room.connections:
        return current_room.connections[direction]
    else:
        print("Invalid move. Try again.")
        return current_room
