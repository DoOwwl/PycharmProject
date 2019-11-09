#Here is my first take at Rock Paper Sissor game
import random
import time
import sys

playerScore = 0
computerScore = 0

print('Welcome to ROCK PAPER SCISSOR!')
time.sleep(1)
print('''
The rules are as follows:
Type: 
r for rocks
p for paper
s for scissor
b for the score board
q for quit
*The game will keep going until you quit''')
time.sleep(5)
print()
print('Please enter your response now.')

choices = ['r','p','s']
while True:
    userChoice = input().lower()
    computerChoice = random.choice(choices)

    if computerChoice == userChoice[0]:
        print ('It is a tie!')
    elif computerChoice == 'r' and userChoice[0] == 'p':
        print ('You won!')
        playerScore += 1
        time.sleep(1)
    elif computerChoice == 'p' and userChoice[0] == 's':
        print ('You won!')
        playerScore += 1
        time.sleep(1)
    elif computerChoice == 's' and userChoice[0] == 'r':
        print ('You won!')
        playerScore += 1
        time.sleep(1)
    elif computerChoice == 'r' and userChoice[0] == 's':
        print ('You lost!')
        computerScore += 1
        time.sleep(1)
    elif computerChoice == 'p' and userChoice[0] == 'r':
        print ('You lost!')
        computerScore += 1
        time.sleep(1)
    elif computerChoice == 's' and userChoice[0] == 'p':
        print ('You lost!')
        computerScore += 1
        time.sleep(1)
    elif userChoice[0] == 'q':
        print ('Thank you for playing')
        sys.exit()
    elif userChoice[0] == 'b':
        print ('Player Score: '+ str(playerScore))
        print ('Computer Score: ' + str(computerScore))

