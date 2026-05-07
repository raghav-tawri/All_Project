# Take a name from the user and print Hello, <name>.
name=input("Enter your name: ")
print(f"Hello, {name}!")
# ● Take two numbers as input and print their sum.
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print(f"The sum is: {num1 + num2}")

# ● Take a number and print You entered <number>.
num=float(input("Enter a number: "))
print(f"You entered {num}.")

# ● Take first name and last name and print them in one line.
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print(f"{first_name} {last_name}")


# ● Take age and print Your age is <age>.
age=int(input("Enter your age: "))
print(f"Your age is {age}.")


# ● Take two numbers and print their difference.
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print(f"The difference is: {num1 - num2}")

# ● Take a city name and print Welcome to <city>.
city=input("Enter a city name: ")
print(f"Welcome to {city}.")


# ● Take a number and print its square.
num=float(input("Enter a number: "))
print(f"The square of {num} is {num**2}.")

# ● Take two values and print them in reverse order.
value1=input("Enter the first value: ")
value2=input("Enter the second value: ")
print(f"Values in reverse order: {value2} {value1}")
# ● Take a string and print it three times in separate lines.
string=input("Enter a string: ")
print(string)
print(string)
print(string)
# ● Take length and width and print Area is <area>.
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length*width
print(f"Area is {area}.")

# ● Take a name and a course and print Name: <name>, Course: <course>.
name=input("Enter your name: ")
course=input("Enter your course: ")
print(f"Name: {name}, Course: {course}.")

# ● Take a number and print Double of <number> is <result>.
num=float(input("Enter a number: "))
double=num*2
print(f"Double of {num} is {double}.")

# ● Take a word and print its first and last character.
word=input("Enter a word: ")
if len(word) > 0:
    print(f"First character: {word[0]}, Last character: {word[-1]}")
else:    
    print("You entered an empty string.")
# ● Take two numbers and print their product.
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print(f"The product is: {num1 * num2}")
# ● Take a sentence and print it in a new line with You said: before it.
sentence=input("Enter a sentence: ")
print(f"You said: {sentence}")
# ● Take a number and print Number entered: <number>.
sentence=input("Enter a sentence: ")
print(f"You said: {sentence}")
num=float(input("Enter a number: "))
print(f"Number entered: {num}.")
# ● Take three values and print them in one line separated by space.
value1=input("Enter the first value: ")
value2=input("Enter the second value: ")
value3=input("Enter the third value: ")
print(f"{value1} {value2} {value3}")
# ● Take a name and print each character on a new line.
name=input("Enter your name: ")
for char in name:
    print(char)
# ● Take a number and print Square is <result>.
num=float(input("Enter a number: "))
print(f"Square is {num**2}.")