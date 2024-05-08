from features import Player, Grid
import menu
import sys


class EscapeRoom:
    def __init__(self):
        self.name = self.get_player_name()
        self.start_position = [0, 0]
        self.player = Player(self.name, False, self.start_position)
        self.grid = Grid(self.player, 4)
        self.running = False

    def get_player_name(self):
        player_name = input("What is your characters name? ")
        return player_name.strip()

    def _menu(self):
        user_choice = menu.main_menu()
        if user_choice == '1':
            self.running = True
        elif user_choice == '2':
            print("Thanks for playing!")
            sys.exit(0)
        else:
            raise InvalidMenuChoice("Please enter number 1 or 2.")

    def run(self):
        while True:
            if not self.running:
                try:
                    self._menu()
                except InvalidMenuChoice as e:
                    print(e)
                    continue

            self.grid.print_grid(self.player.get_position())

            direction = input(
                "Where would you like to move? ('up', 'down', 'left', 'right' or 'menu' to return to main menu): ").lower()

            if direction == "menu":
                self.running = False
                continue
            else:
                movement = {
                    "up": [-1, 0],
                    "down": [1, 0],
                    "left": [0, -1],
                    "right": [0, 1]
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

                result = self.grid.message()

                if result == 'game_over':
                    self.player.set_position(self.start_position)
                    self.running = False
                    print("Game over! Thanks for playing!")


class InvalidMenuChoice(Exception):
    pass


# Usage
game = EscapeRoom()
game.run()
