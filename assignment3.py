#Task 1 : Factorial of a number
num = int(input("Enter a number to find its factorial: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"The factorial of {num} is {factorial(num)}")

#Task 2: Using math module for calculations
import math
num2 = float(input("Enter a number: "))
print(f"The square root of {num2} is {math.sqrt(num2)}")
print(f"The sine of {num2} is {math.sin(num2)}")
print(f"The natural logarithm of {num2} is {math.log(num2)}")