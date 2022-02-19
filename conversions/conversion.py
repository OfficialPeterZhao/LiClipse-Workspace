'''
Objective: The Objective is to make a program that can complete different conversions. The tasks to complete are:
Have the user input a number of miles.
Convert the number of miles to yards, feet, and inches.
Print out the conversions with a simple statement:
EX: 
"[mileInt] converts to [feetInt] feet."
"[mileInt] converts to [yardInt] yards."

@author: Peter
'''
miles = int(input("Provide a number of miles: "))


yards = miles * 1760


print(str(miles) + " miles" + " converts to " + str(yards) + " yards.") 


feet = miles * 5280


print(str(miles) + " miles" + " converts to " + str(feet) + " feet.")


inches = miles * 63360


print(str(miles) + " miles" + " converts to " + str(inches) + " inches.")

