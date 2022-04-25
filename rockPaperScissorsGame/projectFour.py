'''
Objective: The Objective of this program is to make a Rock, Paper, Scissors game for the user to play against the computer. 

@author: Peter Zhao
'''

import random

keepPlaying = True


while(keepPlaying):
    print("Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit")
    
    userScore = 0
    cpuScore = 0

    while(userScore < 2 and cpuScore < 2):
        userChoice = input("Please choose(Rock, Paper, Scissors): ").lower()
        cpulist = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(cpulist)
        print("CPU Choice: " + str(cpuChoice))

        if((userChoice == "rock" and cpuChoice == "scissors") or (userChoice == "paper" and cpuChoice == "rock") or (userChoice == "scissors" and cpuChoice == "paper")):
            userScore = userScore + 1
            print("User: " + str(userScore) + " CPU: " + str(cpuScore)) 
        elif((userChoice == "rock" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "scissors")):
            cpuScore = cpuScore + 1   
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))    
        elif((userChoice == "rock" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "scissors")):
                print("Draw")
                print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        elif (userChoice == "q"):
            break
            keepPlaying = False
        else:
            print("Not an option try again")     
    print("Thanks for playing")
    
    if(userScore == 2):
        print("You won!") 
    
    elif(cpuScore == 2):
        print("CPU won!")
        
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))