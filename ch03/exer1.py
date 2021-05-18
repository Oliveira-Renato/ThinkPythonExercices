#3.1. Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    #print(len(add_space(s)))#display the length 
    print(add_space(s))

def add_space(sp):
    for x in range(70-5):
        sp = ' '+ sp #adding space
        x += 1
    return sp

right_justify('monty')