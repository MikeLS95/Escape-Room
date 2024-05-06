from features import Player, Grid

class Game:
  def __init__(self, name, start_position):
    self.name = input("Name your character!")
    self.player = Player(name, False, start_position)
    self.grid = Grid(self.player, 4)

  def run(self):
    while True:
      self.grid.print_grid(self.player.get_position())

      direction = input("Where would you like to move? (up, down, left, right): ").lower()

      movement = {
          "up": [-1, 0],
          "down": [1, 0],
          "left": [0, -1],
          "right": [0, 1],
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
game = Game("Mike", [0, 0])
game.run()
