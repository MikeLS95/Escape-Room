import json, random
# from features import Player, Key

grid = [[' ' for _ in range(4)] for _ in range(4)]

player_position = [0, 0]

movement = [0, 0]

# remove this before you finish
name = 'Player'

# add this back in later, removed now so its faster for testing the app
# name = input("Enter your character name: ")

# [ 0,0 S][ 0,1 C][ 0,2  ][ 0,3 C]
# [ 1,0 C][ 1,1  ][ 1,2 C][ 1,3 K]
# [ 2,0  ][ 2,1 C][ 2,2  ][ 2,3 C]
# [ 3,0 C][ 3,1  ][ 3,2 E][ 3,3  ]
# S = start 
# C = clue
# K = key
# E = exit

empty = [(0, 2), (1, 1), (2, 0), (2,2), (3, 1), (3, 3)]

key = [(1, 3)]

def load():
    with open('clues.json') as f:
        clues = json.load(f)
    return clues

clue_data = load()

clue = {
    (0, 1): random.choice(clue_data[0]['clues']), 
    (0, 3): random.choice(clue_data[1]['clues']),
    (1, 0): random.choice(clue_data[2]['clues']), 
    (1, 2): random.choice(clue_data[3]['clues']),
    (2, 1): random.choice(clue_data[4]['clues']), 
    (2, 3): random.choice(clue_data[5]['clues']),
    (3, 0): random.choice(clue_data[6]['clues'])
}

def print_grid(grid, player_position):
    grid[player_position[0]][player_position[1]] = name[0].upper()

    for row in grid:
        print("", end="")
        for player in row:
            print("[ " + player + " ]", end="")
        print("")

    grid[player_position[0]][player_position[1]] = ' '

def move_object(player_position, movement, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    new_y = player_position[0] + movement[0]
    new_x = player_position[1] + movement[1]

    if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
        player_position[0] = new_y
        player_position[1] = new_x
        return True
    else:
        return False

while True:
    print_grid(grid.copy(), player_position)

    direction = input("Where would you like to move? (up, down, left, right): ").lower()

    if direction == "up":
        movement = [-1, 0]
    elif direction == "down":
        movement = [1, 0]
    elif direction == "left":
        movement = [0, -1]
    elif direction == "right":
        movement = [0, 1]
    else:
        print("----------------------------------")
        print("I dont think that was a direction!")
        print("----------------------------------")
        continue

    if not move_object(player_position, movement, grid):
        print("----------------------------")
        print("You must remain in the grid!")
        print("----------------------------")


    if tuple(player_position) in clue:
        print("You have found a clue:")
        print(clue[tuple(player_position)])
    elif tuple(player_position) in empty:
        print("You notice nothing interesting in this square.")
    elif tuple(player_position) in key:
        print("You have found the key!")
