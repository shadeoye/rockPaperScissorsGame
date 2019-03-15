import random


def winner(play, comp):
    if play == comp:
        print('DRAW!')
    elif play == 'r' and comp == 'p':
        print('computer wins')
    elif play == 'r' and comp == 's':
        print('you win1')
    elif play == 'p' and comp == 'r':
        print('you win2')
    elif play == 'p' and comp == 's':
        print('computer wins')
    elif play == 's' and comp == 'r':
        print('computer wins')
    else:
        print('you win3')

for x in range(10):
    player = input('rock (r), paper (p) or scissors (s)?')
    computer = random.choice('rps')
    print(computer)
    winner(player,computer)
else:
    print("You've played this game enough, move on")
        
