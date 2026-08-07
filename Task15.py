# Simple Linear Regression Prediction
"""Problem Statement:
Write a Python program that:

Takes bias (b0) from the user.
Takes weight (b1) from the user.
Takes input (x) from the user.
Calculates the predicted output using: y = b0 + b1 * x
Display the predicted output."""


# task15.py

b0 = float(input("Enter Bias (b0): "))
b1 = float(input("Enter Weight (b1): "))
x = float(input("Enter Input (x): "))

y = b0 + (b1 * x)

print("Predicted Output =", y)