import pyfiglet

def main_menu():
    ascii_banner = pyfiglet.figlet_format("ESCAPE ROOM!")
    print(ascii_banner)
    print("1. Select your grid size")
    print("2. Exit application")
    choice = input("Enter your choice: ")
    return choice