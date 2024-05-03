import grid

# while True:
#     print(grid.fourByFour)
#     move = input('Where do you want to move? Up, Down, Left or Right? \n> ').lower()
#     if move == 'Right':
#         if spaceEmpty:
#             print('Theres nothing here')

# print(grid.vector[0])

# four_by_four = [['  ' for _ in range(4)] for _ in range(4)]

# position = [1, 1]

# movement = [1, 0]

# def move_in_grid(position, movement, four_by_four):
#     grid_height = len(four_by_four)
#     grid_width = len(four_by_four[0])

#     new_y = position[0] + movement[0]
#     new_x = position[1] + movement[1]

#     if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
#         position[0] = new_y
#         position[1] = new_x
#         return True
#     else:
#         return False
    
# if move_in_grid(position, movement, four_by_four):
#     print("You moved to:", position)
# else:
#     print("You can't move there")

def print_grid(four_by_four, object_position):
    four_by_four[object_position[0]][object_position[1]] = 'P'

    print("+" + "---" * 3 + "+" for _ in range(len(four_by_four[0])))

    for row in four_by_four:
        print("[  ]", end="")
        for element in row:
            print(" " + element + " ", end="")
        print("[  ]")

    print("+" + "---" * 3 + "+" for _ in range(len(four_by_four[0])))

    four_by_four[object_position[0]][object_position[1]] = ' '

def move_object(object_position, movement, four_by_four):
    grid_height = len(four_by_four)
    grid_width = len(four_by_four[0])

    new_y = object_position[0] + movement[0]
    new_x = object_position[1] + movement[1]

    if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
        object_position[0] = new_y
        object_position[1] = new_x
        return True
    else:
        return False
    
four_by_four = [[' ' for _ in range(4)] for _ in range(4)]

object_position = [1, 1]

movement = [1, 0]

if move_object(object_position, movement, four_by_four):
    print_grid(four_by_four.copy(), object_position)
else:
    print("You can't move there")