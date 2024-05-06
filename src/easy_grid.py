from features import Player, Grid

start_position = [0, 0]

name = 'Player'

def run():
    player = Player('Mike', False, start_position)
    fourbyfour = Grid(player, 4, [0, 0])

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
    
        fourbyfour.message()

run()
    