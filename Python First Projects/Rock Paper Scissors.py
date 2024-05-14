import random #input library random from python.org

def pickOne(): #make a definition to input the info
    pick = input(f'Press (R) for Rock, (P) for Paper, and (S) for scissors: ').lower() #user input the choice
    compy = random.choice(['r', 'p', 's']) #varibale for random choice by computer
    if pick == compy:
        print('Computer :' ,compy, 'It\'s a tie!!')
    elif win(pick, compy):
        print('Computer : ' ,compy, ' You won!')
    else:
        print('Computer : ' ,compy, ' You Lost!!')

def win(player, opponent): #another definition
    if (player == 'r'and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
pickOne()
