import easygrid
import curses

name = input("Enter your character name: ")

def print_grid(grid, object_position):
    grid[object_position[0]][object_position[1]] = name[0].upper()

    for row in grid:
        print("", end="")
        for element in row:
            print("[ " + element + " ]", end="")
        print("")

    grid[object_position[0]][object_position[1]] = ' '

def move_object(object_position, movement, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    new_y = object_position[0] + movement[0]
    new_x = object_position[1] + movement[1]

    if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
        object_position[0] = new_y
        object_position[1] = new_x
        return True
    else:
        return False
    
grid = [[' ' for _ in range(4)] for _ in range(4)]

object_position = [0, 0]

movement = [0, 0]

while True:
    print_grid(grid.copy(), object_position)

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
        print("You must remain in the grid!")
        continue

    if not move_object(object_position, movement, grid):
        print("You must remain in the grid!")