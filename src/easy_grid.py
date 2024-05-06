import json, random
from features import Player, Grid

grid = [[' ' for i in range(4)] for i in range(4)]

start_position = [0, 0]

movement = [0, 0]

name = 'Player'

key = [(1, 3)]

exit_door = [(3, 2)]

def run():
    player = Player('Mike', False, start_position)
    fourbyfour = Grid(player, 4)

    while True:
        fourbyfour.print_grid(player.get_position())

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
            print("-------------------------")
            print("That was not a direction!")
            print("-------------------------")
            continue

        if not fourbyfour.move_player(player, movement):
            print("----------------------------")
            print("You must remain in the grid!")
            print("----------------------------")
    
        message(grid)

run()
    