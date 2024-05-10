from features import Player, Grid
import menu
import sys
import time


class EscapeRoom:
    # This is the main class for the game.  Includes all the functions for running the Escape
    def __init__(self):
        self.name = self.get_player_name()
        self.start_position = [0, 0]
        self.player = Player(self.name, False, self.start_position)
        self.grid = Grid(self.player, 4)
        self.running = False # Makes the default of the running command set to False, making it so whenever the player leaves the game, the run function will exit the while loop.  Allows for a reset of the game after exiting to menu.
        
    # This is how you determine the name of your character.  The first letter of this name will be placed into the grid and moved using the direction input and the movement variable. 
    def get_player_name(self):
        player_name = input("What is your characters name?: ")
        return player_name

    # Allows players to input their menu option and then either navigates to the game or to the exit message and closes the application.  
    # Followup code for menu is in menu.py, where the banner and options are printed.
    def _menu(self):
        user_choice = menu.main_menu()
        if user_choice == '1':
            self.running = True
        elif user_choice == '2':
            print("Thanks for playing!")
            sys.exit(0)
        # Error handling for if something other than '1' or '2' is entered by the user.
        else:
            raise InvalidMenuChoice("Please enter number 1 or 2.")

    # This is the main code for running the game.
    def run(self):
        while True:
            if not self.running:
                try:
                    self._menu()
                # Prints error message for if something other than '1' or '2' is entered by the user.
                except InvalidMenuChoice as e:
                    print(e)
                    continue
            # Accesses the Grid class to print out the grid.  Accesses the Player class to get the current player position.
            self.grid.print_grid(self.player.get_position())

            # Prints the options for movement around the grid and returning to the menu.  Converts the player input into lowercase, for if the user inputs upper case.
            direction = input(
                "Where would you like to move? ('up', 'down', 'left', 'right' or 'menu' to return to main menu): ").lower()

            # If input "menu" is entered, sets running to False, which will reset the grid.
            if direction == "menu":
                self.player.set_position(self.start_position)
                self.player.key = False
                self.running = False
                print("Returning to menu, thanks for playing!")
                time.sleep(2)
                continue
            # When the user inputs a movement, the input is passed to .get(direction) and then printed onto the updated grid
            else:
                movement = {
                    "up": [-1, 0],
                    "down": [1, 0],
                    "left": [0, -1],
                    "right": [0, 1]
                }.get(direction)

                # if input entered is not "up", "down", "left", "right" or "menu", then the invalid input message is printed.
                if not movement:
                    print("-------------------------")
                    print("That was not a direction!")
                    print("-------------------------")
                    continue

                # If the player tries to move out of the grid, the invalid movement message is printed.
                if not self.grid.move_player(self.player, movement):
                    print("----------------------------")
                    print("You must remain in the grid!")
                    print("----------------------------")
                # Handled above two errors manually for a better user experience.


                # Gets a message from the Grid class and prints out the message according to where the player is currently positioned on the grid.
                result = self.grid.message()

                # If the player has the key and has moved to the exit door, the game is completed and the 'game_over' message is displayed.  A message is printed, the key is set back to false and the run function is reset.
                if result == 'game_over':
                    self.player.set_position(self.start_position)
                    self.player.key = False
                    self.running = False
                    print("Game over! Thanks for playing!")

# Raised when a player inputs something other than 1 or two after being prompted with menu options on the main menu
class InvalidMenuChoice(Exception):
    pass

# Usage for the run function inside of the EscapeRoom class
game = EscapeRoom()
game.run()
