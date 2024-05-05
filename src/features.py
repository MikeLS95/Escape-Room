import json, random

class Clue:
    def __init__(self):
        self.clues = ['0,1', '0,3', '1,0', '1,2', '2,1', '2,3', '3,0']

    with open('clues.json') as f:
        clues = json.load(f)
        c0 = clues[0]
        print(f"{random.choice(c0['clues'])}")


class Key:
    def __init__(self):
        pass

class Door:
    def __init__(self):
        pass

class Entrance(Door):
    pass

class Exit(Door):
    pass