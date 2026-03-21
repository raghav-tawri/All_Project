# Write a function that takes two numbers and performs division. Use else block to print
# the result if no error occurs and finally block to print Execution completed.
def safe_division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"The result of dividing {num1} by {num2} is: {result}")
    finally:
        print("Execution completed.")

# 1 Create a function that converts a given input into integer. Use else block to print the
# converted value and finally block to print Conversion attempt finished.
def safe_integer_conversion(value):
    try:
        converted_value = int(value)
    except ValueError:
        print("Error: Invalid input. Cannot convert to integer.")
    else:
        print(f"The converted integer value is: {converted_value}")
    finally:
        print("Conversion attempt finished.")

# 1 Implement a function that calculates square of a number after converting input to float.
# Use else block to return the square and finally block to display Process done.
def safe_square_calculation(value):
    try:
        num = float(value)
        square = num ** 2
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    else:
        print(f"The square of {num} is: {square}")
    finally:
        print("Process done.")

# 1 Write a function that performs floor division of two numbers. Use else block to print
# quotient and finally block to print Function executed.
def safe_floor_division(num1, num2):
    try:
        quotient = num1 // num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"The floor division of {num1} by {num2} is: {quotient}")
    finally:
        print("Function executed.")

# 1 Create a function that finds reciprocal of a number. Use else block to print the
# reciprocal and finally block to print End of operation.
def safe_reciprocal(value):
    try:
        num = float(value)
        reciprocal = 1 / num
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    except ZeroDivisionError:
        print("Error: Reciprocal of zero is not defined.")
    else:
        print(f"The reciprocal of {num} is: {reciprocal}")
    finally:
        print("End of operation.")

# 1 Implement a function that multiplies two inputs after converting them into integers. Use
# else block to print product and finally block to print Multiplication tried.
def safe_multiplication(value1, value2):
    try:
        num1 = int(value1)
        num2 = int(value2)
        product = num1 * num2
    except ValueError:
        print("Error: Invalid input. Cannot convert to integer.")
    else:
        print(f"The product of {num1} and {num2} is: {product}")
    finally:
        print("Multiplication tried.")

# 1 Write a function that calculates percentage using marks and total marks. Use else
# block to print percentage and finally block to print Calculation finished.
def safe_percentage_calculation(marks, total_marks):
    try:
        marks = float(marks)
        total_marks = float(total_marks)
        percentage = (marks / total_marks) * 100
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    except ZeroDivisionError:
        print("Error: Total marks cannot be zero.")
    else:
        print(f"The percentage is: {percentage:.2f}%")
    finally:
        print("Calculation finished.")

# 1 Create a function that converts string input into float and prints half of it. Use else block
# for output and finally block for completion message.
def safe_half_calculation(value):
    try:
        num = float(value)
        half = num / 2
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    else:
        print(f"Half of {num} is: {half}")
    finally:
        print("Completion message.")

# 1 Implement a function that performs modulus operation. Use else block to print
# remainder and finally block to print Modulus attempt done.
def safe_modulus(num1, num2):
    try:
        remainder = num1 % num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"The modulus of {num1} and {num2} is: {remainder}")
    finally:
        print("Modulus attempt done.")

# 1 Write a function that calculates power of a number. Use else block to print result and
# finally block to print Power function executed.
def safe_power_calculation(base, exponent):
    try:
        result = base ** exponent
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"{base} raised to the power of {exponent} is: {result}")
    finally:
        print("Power function executed.")

# 1 Create a function that returns absolute value after converting input safely. Use else
# block to print absolute value and finally block to print Absolute check completed.
def safe_absolute_value(value):
    try:
        num = float(value)
        absolute_value = abs(num)
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    else:
        print(f"The absolute value of {num} is: {absolute_value}")
    finally:
        print("Absolute check completed.")

# 1 Implement a function that divides three numbers step by step. Use else block to print
# final result and finally block to print Division process ended.
def safe_stepwise_division(num1, num2, num3):
    try:
        intermediate_result = num1 / num2
        final_result = intermediate_result / num3
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: All inputs must be numbers.")
    else:
        print(f"The result of dividing {num1} by {num2} and then by {num3} is: {final_result}")
    finally:
        print("Division process ended.")

# 1 Write a function that converts input into integer and prints its double. Use else block for
# result and finally block for closing message.
def safe_double_calculation(value):
    try:
        num = int(value)
        double = num * 2
    except ValueError:
        print("Error: Invalid input. Cannot convert to integer.")
    else:
        print(f"The double of {num} is: {double}")
    finally:
        print("Closing message.")

# 1 Create a function that subtracts two numbers after safe conversion. Use else block to
# print difference and finally block to print Subtraction attempt finished.
def safe_subtraction(value1, value2):
    try:
        num1 = float(value1)
        num2 = float(value2)
        difference = num1 - num2
    except ValueError:
        print("Error: Invalid input. Cannot convert to float.")
    else:
        print(f"The difference between {num1} and {num2} is: {difference}")
    finally:
        print("Subtraction attempt finished.")

# 1 Implement a function that calculates average of two numbers. Use else block to print
# average and finally block to print Average calculation done.
def safe_average_calculation(num1, num2):
    try:
        average = (num1 + num2) / 2
    except TypeError:
        print("Error: Both inputs must be numbers.")
    else:
        print(f"The average of {num1} and {num2} is: {average}")
    finally:
        print("Average calculation done.")

# 1 Write a function that calculates square root after converting input to float. Use else
# block to print result and finally block to print Square root operation finished.
def safe_square_root_calculation(value):
    try:
        num = float(value)
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        square_root = num ** 0.5
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"The square root of {num} is: {square_root}")
    finally:
        print("Square root operation finished.")

# 1 Create a function that performs simple interest calculation. Use else block to print
# interest and finally block to print Interest calculation attempt done.
def safe_simple_interest_calculation(principal, rate, time):
    try:
        interest = (principal * rate * time) / 100
    except TypeError:
        print("Error: All inputs must be numbers.")
    else:
        print(f"The simple interest is: {interest}")
    finally:
        print("Interest calculation attempt done.")

# 1 Implement a function that divides a number by itself after safe conversion. Use else
# block to print result and finally block to print Self division completed.
def safe_self_division(value):
    try:
        num = float(value)
        if num == 0:
            raise ValueError("Cannot divide zero by itself.")
        result = num / num
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"The result of dividing {num} by itself is: {result}")
    finally:
        print("Self division completed.")

# 1 Write a function that finds remainder after safe integer conversion of inputs. Use else
# block to print remainder and finally block to print Remainder operation finished.
def safe_integer_remainder(value1, value2):
    try:
        num1 = int(value1)
        num2 = int(value2)
        remainder = num1 % num2
    except ValueError:
        print("Error: Invalid input. Cannot convert to integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The remainder of {num1} divided by {num2} is: {remainder}")
    finally:
        print("Remainder operation finished.")