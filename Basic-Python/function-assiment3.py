# Map – Coding Questions
# 1 Write a program that takes a list of integers and uses map to return a new list containing the
# square of each number.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)
# 2 Given a list of temperatures in Celsius, use map to convert them into Fahrenheit. (Formula: F =
# (C × 9/5) + 32)
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
# 3 Take a list of strings and use map to convert each string into its uppercase form.
strings = ["hello", "world", "python"]
uppercase = list(map(lambda s: s.upper(), strings))
print(uppercase)
# 4 Given a list of numbers, use map with a lambda function to add 10 to each element and print
# the updated list.
numbers = [1, 2, 3, 4, 5]
updated = list(map(lambda x: x + 10, numbers))
print(updated)
# 5 Write a program that takes two lists of equal length and uses map to return a list containing the
# sum of corresponding elements.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)

# Filter – Coding Questions
# 1 Given a list of integers, use filter to create a new list containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# 2 Write a program that takes a list of numbers and filters out all numbers greater than 50.
numbers = [10, 60, 30, 80, 20]
filtered = list(filter(lambda x: x <= 50, numbers))
print(filtered)
# 3 Given a list of strings, use filter to return only those strings whose length is greater than 5.
strings = ["hello", "world", "python"]
long_strings = list(filter(lambda s: len(s) > 5, strings))
print(long_strings)
# 4 Write a program to filter out all negative numbers from a given list using filter and lambda.
numbers = [1, -2, 3, -4, 5]
positive_numbers = list(filter(lambda x: x >= 0, numbers))
print(positive_numbers)
# 5 Given a list of integers, use filter to extract only numbers that are divisible by both 2 and 3.
numbers = [6, 12, 18, 24, 30]
divisible_by_6 = list(filter(lambda x: x % 6 == 0, numbers))
print(divisible_by_6)

# Higher Order Functions – Coding Questions
# 1 Write a function calculate that takes another function and a number as arguments and applies
# that function to the number.
def calculate(func, num):
    return func(num)
def square(x):
    return x ** 2
result = calculate(square, 5)
print(result)
# 2 Create a function operation that accepts two numbers and a function (like add, multiply) and
# returns the result after applying the function.
def operation(num1, num2, func):
    return func(num1, num2)
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
result_add = operation(3, 4, add)
result_multiply = operation(3, 4, multiply)
print(result_add)
print(result_multiply)
# 3 Write a function power_generator that returns another function which calculates the cube of a
# number.
def power_generator():
    def cube(x):
        return x ** 3
    return cube
cube_function = power_generator()
print(cube_function(3)) 
# 4 Create a function apply_twice that takes a function and a number, and applies the function two
# times on the number.
def apply_twice(func, num):
    return func(func(num))
def increment(x):
    return x + 1
result = apply_twice(increment, 5)
print(result)
# 5 Write a function choose_function that takes a string argument ('double' or 'triple') and returns a
# corresponding function to multiply a number.
def choose_function(option):
    if option == 'double':
        return lambda x: x * 2
    elif option == 'triple':
        return lambda x: x * 3
    else:
        return None
double_func = choose_function('double')
triple_func = choose_function('triple')
print(double_func(5))
print(triple_func(5))

# Decorators – Coding Questions
# 1 Write a decorator that prints 'Function started' before execution and 'Function ended' after
# execution of any function.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper
# 2 Create a decorator that measures and prints the execution time of a function.
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
# 3 Write a decorator that checks whether the input number to a function is positive; if not, it should
# print an error message.
def positive_input_decorator(func):
    def wrapper(num):
        if num <= 0:
            print("Error: Input must be a positive number.")
            return None
        return func(num)
    return wrapper
# 4 Create a decorator that logs the arguments passed to a function before calling it.
def log_arguments_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper
# 5 Write a decorator that allows a function to be executed only once; on subsequent calls it should
# print 'Function already executed'.
def execute_once_decorator(func):
    executed = False
    def wrapper(*args, **kwargs):
        nonlocal executed
        if not executed:
            executed = True
            return func(*args, **kwargs)
        else:
            print("Function already executed")
    return wrapper