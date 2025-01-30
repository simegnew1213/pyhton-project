#1  Write a program in Python to generate Fibonacci series for a given number? 
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
fib_series = []
while len(fib_series) < n:
    fib_series.append(a)
    a, b = b, a + b
print("Fibonacci Series:")
print(fib_series)
#2  Write a program in Python to compute whether the given integer Number is a Palindrome
num = int(input("Enter an integer: "))
if str(num) == str(num)[::-1]:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")
#3 Write a Python Program to convert a given decimal number to its corresponding Binary Number.
decimal_num = int(input("Enter a decimal number: "))
binary_num = bin(decimal_num).replace("0b", "")
print(f"Binary equivalent of {decimal_num}: {binary_num}")   
#4Write a Python program to convert a given Binary Number to its Equivalent Decimal number.
binary_num = input("Enter a binary number: ")
decimal_num = int(binary_num, 2)
print(f"Decimal equivalent of {binary_num}: {decimal_num}")
#5 Write a Python Program to compute Pythagorean triplets up to a given maximum value. 
max_val = int(input("Enter the maximum value: "))
triplets = []
for a in range(1, max_val + 1):
    for b in range(a, max_val + 1):
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= max_val:
            triplets.append((a, b, int(c)))
print("Pythagorean Triplets:")
print(triplets)
#6  Write a Python program to compute the Highest Common Factor (HCF) of two numbers. 
# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compute HCF using Euclidean algorithm
x, y = num1, num2
while y:
    x, y = y, x % y

# Output
print(f"HCF of {num1} and {num2}: {x}")