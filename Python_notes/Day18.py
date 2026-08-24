#Recursive(factorial)
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
#recursion limit
import sys
sys.setrecursionlimit(2000)
#Pass by value
def modify_value(num):
    num += 10 # This creates a new local variable
    print("Inside function:", num)
x = 5
modify_value(x)
print("Outside function:", x)
#Pass by reference
def modify_list(lst):
    lst.append(4) # Modifies the original list
numbers = [1, 2, 3]

modify_list(numbers)
print(numbers)