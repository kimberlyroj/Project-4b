# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 1/28/2021
# Description: A function that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence
def Fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fib(num - 1) + Fib(num - 2)
num = int(input("Enter an integer: "))
print(Fib(num))