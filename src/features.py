import json, random
from typing import List

class Player:
    def __init__(self, name: str, key: bool, player_position: List[str]):
        self.name = name
        self.key = key
        self.__x_position = player_position[1]
        self.__y_position = player_position[0]
    
    def set_position(self, position):
        self.__x_position = position[1]
        self.__y_position = position[0]

    def get_position(self):
        return [self.__y_position, self.__x_position]
    
    def set_key():
        pass

    def get_key():
        pass

def load():
    with open('clues.json') as f:
        clues = json.load(f)
    return clues

def get_random_clues():
    clue_data = load()
    return {
        (0, 1): random.choice(clue_data[0]['clues']), 
        (0, 3): random.choice(clue_data[1]['clues']),
        (1, 0): random.choice(clue_data[2]['clues']), 
        (1, 2): random.choice(clue_data[3]['clues']),
        (2, 1): random.choice(clue_data[4]['clues']), 
        (2, 3): random.choice(clue_data[5]['clues']),
        (3, 0): random.choice(clue_data[6]['clues'])
    }

class Grid:
    def __init__(self, player: Player, grid_size: int):
        self.grid = [[' 'for _ in range(grid_size)] for _ in range(grid_size)]
        self.player = player
        self.grid_height = len(self.grid)
        self.grid_width = len(self.grid[0])
        self.clues = get_random_clues()

    def move_player(self, player: Player, movement):
        current_position = player.get_position()

        new_y = current_position[0] + movement[0]
        new_x = current_position[1] + movement[1]

        if 0 <= new_y < self.grid_height and 0 <= new_x < self.grid_width:
            player.set_position([new_y, new_x])
            return True
        else:
            return False
        
    def print_grid(self, player_position):
        copy_grid = self.grid.copy()
        copy_grid[player_position[0]][player_position[1]] = self.player.name[0].upper()

        for row in copy_grid:
            print("", end="")
            for player in row:
                print("[ " + player + " ]", end="")
            print("")

        copy_grid[player_position[0]][player_position[1]] = ' '

    def message(self):
        current_position = self.player.get_position()
        if tuple(current_position) in self.clues:
            print("You have found a clue:")
            print(self.clues[tuple(current_position)])
        elif tuple(current_position) in key:
            self.player.key = True
            print("You have found the key! What does it open?")
        elif tuple(current_position) in exit_door and self.player.key == False:
            print("You have found the exit door! Hmm thats weird, it appears to be locked, you will need to find the key!.")
        elif tuple(current_position) in exit_door and self.player.key == True:
            print("You have found the exit door!  You use the key to open the door.")
            self.print_grid(self.player.get_position())
            print("You have won!")
            exit()
        else:
            print("You find nothing interesting.")

class Key:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False

    def is_at_position(self, x, y):
        print("You found the key! What does it open?")
        return self.x == x and self.y == y
        

class Door:
    def __init__(self, locked=True):
        self.locked = locked


class Entrance(Door):
    pass

class Exit(Door):
    pass

key = [(1, 3)]

exit_door = [(3, 2)]