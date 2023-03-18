picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for outeritem in picture:
    #  print(outeritem)
    for item in outeritem:
        if item == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
