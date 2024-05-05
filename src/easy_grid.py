grid = [[' ' for _ in range(4)] for _ in range(4)]

player_position = [0, 0]

movement = [0, 0]

# remove this before you finish
name = "Player"

# add this back in later, removed now so its faster for testing the app
# name = input("Enter your character name: ")

# Below comment out code is where I want clues to be
# clue = [(0, 1)][(0, 4)][(1, 0)][(1, 2)]

clue = [(0, 1), (2, 3), (1, 2), (3, 0), (2, 0), (0, 3)]

def print_grid(grid, player_position):
    grid[player_position[0]][player_position[1]] = name[0].upper()

    for row in grid:
        print("", end="")
        for element in row:
            print("[ " + element + " ]", end="")
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
    print_grid(grid.copy(), player_position, clue)

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
        print("You have found a clue")

