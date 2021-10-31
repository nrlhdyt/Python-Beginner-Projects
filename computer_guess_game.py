import random

def computerGuess(x):
    low = 1
    high = x
    insertedNumb = ''
    while insertedNumb != 'c': #c is a right number
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        insertedNumb= input(f'Is {guess} too high (H), too low (L), or correct(C)').lower()
        if insertedNumb == 'h':
            high = guess - 1
        elif insertedNumb == 'l':
            low = guess +1
    print(f'Yeahh! Computer guess your number {guess}, correctly!')
computerGuess(10)