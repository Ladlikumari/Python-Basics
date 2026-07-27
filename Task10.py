# Write a Python program to sort a list of numbers in ascending order using the Bubble Sort algorithms

# Bubble Sort Program

numbers = [64, 34, 25, 12, 22, 11, 90]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)