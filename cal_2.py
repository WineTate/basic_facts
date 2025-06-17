import math

# Get the expression from the user
expression = input("Enter a math expression: ")

# Use eval() to evaluate the expression
try:
    result = eval(expression)
    print("Result:", result)
except (NameError, TypeError, SyntaxError) as e:
    print("Invalid expression:", e)
except ZeroDivisionError:
    print("Cannot divide by zero.")