"""Task 19: Even or Odd

Create a function check_even_odd(num) that:

Prints "Even" if the number is even.
Prints "Odd" if the number is odd.

Example:

Input: 15
Output: Odd"""


def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even_odd(15)