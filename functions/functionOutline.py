'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''
from pickle import FALSE, TRUE

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def twoBoolean(booleanT, booleanF):
        if (booleanT and booleanF):
            True
        else: False
        return twoBoolean
x = TRUE
y = TRUE
twoBoolean(x,y)
    
print(twoBoolean(x,y))
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.

def gallons(cups):
    gallons = (1/16) * cups
    return cups
    
print(gallons(4))    

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

def gallons(cups)
    gallons = (1/16) * cups
    return cups
    
print(gallons(4))    
