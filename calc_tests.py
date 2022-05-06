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

"""
Testing algebra solver
"""

test_formulas = ["2x*2=4", "2*(2+2)*2x=32", "2x+2y=20"]
answer_formulas = [(1, 0), (2, 0), (10, 0)]

for i in range(len(test_formulas)):
    print("Test " + str(i) + ": " + test_formulas[i])
    result = solve(test_formulas[i])
    # Test will round to nearest int and compare with expected int values
    assert (int(float(result[0])), int(float(result[1]))) == answer_formulas[i], f"Expected {answer_formulas[i][0]} and {answer_formulas[i][1]}, got {result[0]} and {result[1]}"
    print("PASS")

