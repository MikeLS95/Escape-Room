import pyfiglet


def main_menu():
    # Prints the banner generated from the module pyfiglet.
    ascii_banner = pyfiglet.figlet_format("ESCAPE ROOM")
    print(ascii_banner)  # Using the default banner from pyfiglet.
    print("1. Play 4x4 Grid")  # Option for playing the 4x4 grid.
    print("2. Exit application")  # Option for exiting the game.
    choice = input("Enter your choice: ")
    return choice
