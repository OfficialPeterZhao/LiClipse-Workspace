'''
Objective: The Objective of this program is to quiz the user on basic high school
trivia. The tasks to complete are:
Ask the user each of the following questions:
    1) What is the powerhouse of the cell?
        A) mitochondria B) nucleus C) ribosome
    2) How many states comprise the United States?
        A) 13 B) 45 C) 50
    3) In y = mx + b, what does m stand for?
        A) slope B) output C) I don't understand math
    4) In English, a person, place or thing is called:
        A) verb B) adjective C) noun
The user should input a letter for each question. (A, B, or C)
Check the users answer, if it is correct print "Correct", else it should print "Incorrect, the correct answer is [insert]"
Additionally, the program should track how many questions the user got correct and at the end give them a score out of 4. And give them a percentage.
@author: Peter Zhao
'''

score = 0

Question_1 = print("What is the powerhouse of the cell?\n(a) mitochondria\n(b) nucleus\n(c) ribosome")

answer_1 = "a"

answer = input("Answer: ")

if (answer.lower() == answer_1):
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

Question_2 = print("How many states comprise the United States?\n(a) 13\n(b) 45\n(c) 50")

answer_2 = "c"

answer = input("Answer: ")

if (answer.lower() == answer_2):
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
    
Question_3 = print("In y = mx + b, what does m stand for?\n(a) slope\n(b) output\n(c) I don't understand math")

answer_3 = "a"

answer = input("Answer: ")

if answer.lower() == answer_3:
    print("correct")
    score = score + 1
else: print("Incorrect")

Question_4 = print("In English, a person, place or thing is called:\n(a) verb\n(b) adjective\n(c) noun")

answer_4 = "c"

answer = input("Answer: ")
if answer.lower() == answer_4:
    print("correct")
    score = score + 1
else: print("Incorrect")

p = score/4

print("You got a " + str(score) + "/4 or in other words a " + str(p*100) + "%")
