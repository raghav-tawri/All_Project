# 1. Sum of two numbers
def get_sum(a, b):
    return a + b

# 2. Square of a number
def get_square(n):
    return n ** 2

# 3. Cube of a number
def get_cube(n):
    return n ** 3

# 4. Even or Odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
# 5. Factorial
def get_factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# 6. Larger of two numbers
def get_larger(a, b):
    return a if a > b else b

# 7. Smallest of three numbers
def get_smallest(a, b, c):
    return min(a, b, c)
# 8. Reverse a number
def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

# 9. Sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 10. Palindrome check
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 11. Count digits
def count_digits(n):
    return len(str(abs(n)))


# 12. Prime number check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 13. Product of two numbers
def get_product(a, b):
    return a * b

# 14. Remainder
def get_remainder(a, b):
    return a % b
# 15. Sum from 1 to n
def sum_up_to_n(n):
    return (n * (n + 1)) // 2

# 16. Multiplication table
def print_table(n):
    return [n * i for i in range(1, 11)]
# 17. Power (a raised to b)
def get_power(a, b):
    return a ** b
# 18. Last digit
def get_last_digit(n):
    return abs(n) % 10

# 19. First digit
def get_first_digit(n):
    return int(str(abs(n))[0])

# 20. Absolute difference
def get_absolute_difference(a, b):
    return abs(a - b)