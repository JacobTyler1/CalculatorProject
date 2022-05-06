from console_calculator import *

"""
Testing mathematical expressions
"""
test_expressions = ["2*2", "(2*2)*2", "3*(3+4)", "3*pi+2", "2.2*5.6"]
answers_expressions = [4, 8, 21, 11.42, 12.32]

for i in range(len(test_expressions)):
    print("Test " + str(i) + ": " + test_expressions[i])
    result = calculate(test_expressions[i])
    assert result == answers_expressions[i], f"Expected {answers_expressions[i]}, got {result}"
    print("PASS")

