from math import *
import os
import sys
import re
import numpy as np

"""
This function is called by calculate if algebraic expression
is found. This will test a bunch of values for x an y. 

Specifically it tests 0 to 1000 with a step size of 0.5

Nothing is returned because all display output is done in the function
"""
def solve(formula):
    print(formula)
    alg_expression = re.search(r'^\(?\d+[xy]?([-+/*]\(?\d+[xy]?\)?)*=\d+$', formula)

    if not bool(alg_expression):
        print("Invalid Algebraic Expression")
        print("x and y are only valid variables")
        print("x and y must both be on left side of equation only")
        print("left side must be one number")
        return

    alg_expression = alg_expression[0]

    right_side = re.search(r'=\d+', alg_expression)
    right_side = right_side[0][1:]
    print("Right side = " + str(eval(right_side)))

    left_side = re.sub(r'=\d+', '', alg_expression)
    print("Left side = " + str(left_side))

    pi_expression = re.search('pi', left_side) #Search for pi in the expression
    if bool(pi_expression):
        left_side = re.sub('pi', "3.14", left_side) # If pi is found, replace it in the expression with a number

    x_match = re.search('x', left_side) #Search for 'x' in the expression
    y_match = re.search('y', left_side) # Search for a y in the expression

    if bool(y_match): # Runs if y was found in string
        if bool(x_match): # Runs if x was found in string with y in it
            for i in np.linspace(0,1000,2000): # Iterates i with step size 0.5 from 0 to 20000 (tests these numbers for y)
                y_replace = '*' + str(i)
                y_test = re.sub('y', y_replace, left_side) # Replace y with current value of i in expression that will be tested

                for j in np.linspace(0,1000,2000): # Iterates j with step size 0.5 from 0 to 20000 (tests these numbers for x)
                    replacement = '*' + str(j) # Replacement string for equation with test number
                    x_test = re.sub('x', replacement, y_test) # Replace x with current value of i in expression that will be tested

                    if (eval(x_test)+0.5 > eval(right_side)) and (eval(x_test)-0.5 < eval(right_side)): # Test if expression reduces to within one step size of the right side
                        format_y= "{:.2f}".format(i) # Formats the numbers to only display two decimal places
                        format_x = "{:.2f}".format(j) # Formats the numbers to only display two decimal places
                        print("Estimated solution is x=" + format_y + " y=" + format_x) # Display solution with float numbers truncated
                        return (format_x, format_y) # Return values are for test purposes
            print("Unable to solve equation")
        else:
            for i in np.linspace(0,1000,2000):
                replacement = '*' + str(i) # Replacement string for equation with test number
                y_test = re.sub('y', replacement, left_side)
                if (eval(y_test)+0.5 > eval(right_side)) and (eval(y_test)-0.5 < eval(right_side)):
                    format_float = "{:.2f}".format(i)
                    print("Estimated solution is y=" + format_float)
                    return (0, format_float)
            print("Unable to solve equation")
    elif bool(x_match):
        for i in np.linspace(0,1000,2000):
            replacement = '*' + str(i) # Replacement string for equation with test number
            x_test = re.sub('x', replacement, left_side)
            if (eval(x_test)+0.5 > eval(right_side)) and (eval(x_test)-0.5 < eval(right_side)):
                    format_float = "{:.2f}".format(i)
                    print("Estimated solution is x=" + format_float)
                    return (format_float, 0) 
        print("Unable to solve equation")

"""
This function is the primary driver of the calculator.
It detects if it is a methematical expression or algebraic expression
and then calls the proper solver to return a solution

All printing handled directly in calculate and solve so nothing is returned 
by either function

"""
def calculate(raw_string):
    words = raw_string.split() # Process string by splitting into list of inputted words using spaces as delimitter

    if len(words) < 1: # if no words, do nothing and alert user
        print("Illegal Formula Entered")
        return
    
    if(words[0] == "solve" or words[0] == "Solve"): # Check if input is algebraic expression to solve
        solve(words[1]) # Call algebraic solver function
        return
    expression = words[0] # Assume first split word is a math expression otherwise invalid

    pi_expression = re.search('pi', expression) #Search for pi in the expression
    if bool(pi_expression):
        expression = re.sub('pi', "3.14", expression) # If pi is found, replace it in the expression with a number
        # print(expression)

    math_expression = re.search(r'^\(?\d+(.\d+)?([-+/*]\(?\d+(.\d+)?\)?)*$', expression)
    

    if not bool(math_expression): # If no legal mathematical expression is entered, alert user and return
        print("Illegal Formula Entered")
        return

    print(eval(math_expression[0]))
    return eval(math_expression[0])
    

    
"""
The main function that will run when the program is called from a terminal window
This contains the main loop that runs until user terminates the program
"""
if __name__ == "__main__":
    # Check platform and call correct command to clear window
    if sys.platform != "win32": 
        os.system('clear')
    else:
        os.system('cls')

    print("Welcome to my Calculator\n")

    while(True): # Main loop of program
        print("\nEnter one of the following:")
        print(" - A mathematical expression i.e. \"(2*2)/4\"")
        print(" - A mathematical expression using pi i.e. \"2*pi\"")
        print(" - An algebraic equation i.e. \"Solve 2x+2=4\"\n")

        raw_string = input("What is your problem?\n") #Prompt the user for a problem to solve
        calculate(raw_string) # Call calculate function to process input and return proper output

