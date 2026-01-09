# Task 1 : check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

# Task 2: Sum of all number from 1 to 50 using for loop
total_sum = 0
for i in range(1, 51):
    total_sum += i
print("Sum of all numbers from 1 to 50 is:", total_sum)