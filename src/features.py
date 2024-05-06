import json, random

# class Clue:
#     def __init__(self):
#         self.clues = ['0,1', '0,3', '1,0', '1,2', '2,1', '2,3', '3,0']

#     with open('clues.json') as f:
#         clues = json.load(f)
#         c0 = clues[0]
#         print(f"{random.choice(c0['clues'])}")

class Inventory:
    def __init__(self, items=[]):
        self.items = items

    def transfer(self, to_inv):
        to_inv.items += self.items
        self.items = []

class Player:
    def __init__(self, name: str, items=[]):
        self.name = name
        self.inv = Inventory(items)

    def get_inventory(self):
        return self.inv.__dict__

class Key:
    def __init__(self, x=1, y=3):
        self.x = x
        self.y = y
        self.picked_up = False

    def is_at_position(self, x, y):
        print("You have found a key!")
        return self.x == x and self.y == y

class Door:
    def __init__(self, locked=True):
        self.locked = locked


class Entrance(Door):
    pass

class Exit(Door):
    pass