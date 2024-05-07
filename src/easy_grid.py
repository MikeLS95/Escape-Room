from features import Player, Grid
import functions
import sys


class EscapeRoom:
    def __init__(self, name, start_position):
        self.name = name
        self.player = Player(name, False, start_position)
        self.grid = Grid(self.player, 4)

    def launch(self):
        while True:
            user_choice = functions.main_menu()
            if user_choice == '1':
                EscapeRoom.run(self)
            elif user_choice == '2':
                print("Thanks for playing!")
                sys.exit(0)
            else:
                if not user_choice == 1 or 2:
                    print("Please enter number 1 or 2.")
                if not user_choice.isnumeric():
                    print("Invalid choice. Please select a valid choice.")

    def run(self):
        while True:
            self.grid.print_grid(self.player.get_position())

            direction = input(
                "Where would you like to move (up, down, left, right, 'menu' to return to main menu)?: ").lower()

            movement = {
                "up": [-1, 0],
                "down": [1, 0],
                "left": [0, -1],
                "right": [0, 1],
                "menu": functions.main_menu()
            }.get(direction)

            if not movement:
                print("-------------------------")
                print("That was not a direction!")
                print("-------------------------")
                continue

            if not self.grid.move_player(self.player, movement):
                print("----------------------------")
                print("You must remain in the grid!")
                print("----------------------------")

            self.grid.message()


# Usage
game = EscapeRoom("Mike", [0, 0])
game.launch()

