"""Write a Python program that takes two numbers from the user and performs division.

Handle these errors:

If the user enters 0 as the denominator, display "Cannot divide by zero".
If the user enters text instead of a number, display "Invalid input".
Otherwise, display the result."""


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")