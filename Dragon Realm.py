#The Dragon game
#The first use of \n makes a new line but dont space before theres a space in the chat 

import random
import time

def displayIntro():
    print ('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly \nand will share his treasure with you. The other dragon \nis greedy and hungry, and will eat you on sight.''')

print ()

def chooseCave(): # This is just a condition it wont do anything until it sees the thing again
    cave = ' ' #createas a new variable called cave and stores a blank string in it
    while cave != '1' and cave != '2': #if one says hi or anything besides 1 or 2 it will repeat itself instead of giving error
        print ('Which cave will you go into? (1 or 2)') # The idea here is to make this false which moves on to the next block which is return
        cave = input ()

    return cave # returns right back up the variable of cave to redo? Returns the answer to line 44

def checkCave (chosenCave): #The chosen cave that is called a parameter which is a local varible that is used by the function's code
    #so whatever is in the value of chosen cave is assigned inside checkcave
    print ('You have approach the cave...')
    time.sleep (2)
    print ('It is dark and spooky...')
    time.sleep (2)
    print ('A large dragon jumps out in front of you! He opens his jaws and...')
    print ()
    time.sleep (2)

    friendlyCave = random.randint (1, 2) # so this returns the integer 

    if chosenCave == str(friendlyCave): #thats why you have to do str so you can compare string with string
        #Could also change the chosenCave into an int to compare int to int cant compare int to str
        print ('Gives you his trasure!')
    else:
        print ('Gobbles you down in one bite!')

playAgain= 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chosenNumber = chooseCave () # without this function it wont let the player choose the number
                                  #so be sure to make a varible to use its parameter and match up with checkcave
    checkCave (chosenNumber) # bc you have a value assigned to chosen number, now check cave will appear in mind thatt the number chosen is represented

    print ('Do you want to play again? (yes or no)')
    playAgain = input ()
    
 
    
