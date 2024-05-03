print('[ P ] [   ] [   ] [   ]')
print('[   ] [   ] [   ] [   ]')
print('[   ] [   ] [   ] [   ]')
print('[   ] [   ] [   ] [   ]')

move = input('Where do you want to move? Up, Down, Left or Right? ')


if move == 'Up':
    print('You cannot move into a wall')
elif move == 'Down':
    print('[   ] [   ] [   ] [   ]')
    print('[ P ] [   ] [   ] [   ]')
    print('[   ] [   ] [   ] [   ]')
    print('[   ] [   ] [   ] [   ]')

