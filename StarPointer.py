picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

for row in picture:
    for i in row:
        if (i == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')