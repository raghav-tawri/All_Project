# 1. Write a Python program that takes an integer as input and checks whether the
# number is greater than zero, even, and divisible by 3. Print an appropriate
# message depending on whether all conditions are satisfied.
num=int(input("Enter an integer: "))
if num > 0:
    if num % 2 == 0:
        if num % 3 == 0:
            print("The number is greater than zero, even, and divisible by 3.")
        else:
            print("The number is greater than zero and even, but not divisible by 3.")
    else:
        print("The number is greater than zero but not even.")
else:
    print("The number is not greater than zero.")
# 2. Write a Python program that takes a number as input and checks whether it lies
# outside the range 10 to 50 (that is, less than 10 or greater than 50).
num=int(input("Enter a number: "))
if num < 10 or num > 50:
    print("The number lies outside the range 10 to 50.")
else:
    print("The number lies within the range 10 to 50.") 
# 3. Write a Python program that accepts a person’s age and checks whether the
# person is eligible to vote (age ≥ 18) and not a senior citizen (age < 60).
age=int(input("Enter your age: "))
if age >= 18 and age < 60:
    print("You are eligible to vote and not a senior citizen.")
elif age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not eligible to vote.")
# 4. Write a Python program that accepts a year as input and checks whether it is a
# valid leap year using all leap year rules (divisible by 4, not divisible by 100 unless
# divisible by 400).
year=int(input("Enter a year: "))
if(year%4==0) and (year%100!=0 or year%400==0):
    print("It is a leap year")
else:    
    print("It is not a leap year")
# 5. Write a Python program that accepts a single character and checks whether it is an
# alphabet and also a vowel.
chares=input("Enter a single character: ")
vowels=['a','e','i','o','u']
char=chares.lower()
if char.isalpha():
    print("It is an alphabet")
    if char in vowels:
        print("It is also a vowel")
    else:
        print("It is not a vowel")
else:    
    print("It is not an alphabet")
# 6. Write a Python program that checks whether a number is divisible by 4 or divisible
# by 6, but not divisible by both at the same time.
num=int(input("Enter a number: "))
if (num % 4 == 0 or num % 6 == 0) and not (num % 4 == 0 and num % 6 == 0):
    print("The number is divisible by 4 or 6, but not both.")
else:    
    print("The number does not satisfy the condition.")
# 7. Write a Python program that accepts marks of three subjects and checks whether
# the student has passed in all subjects, assuming the pass mark is 40 in each
# subject.
marks1=int(input("Enter marks for subject 1: "))
marks2=int(input("Enter marks for subject 2: "))
marks3=int(input("Enter marks for subject 3: "))
if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
    print("The student has passed in all subjects.")
else:   
    print("The student has not passed in all subjects.")
# 8. Write a Python program that checks whether a given password is valid by verifying
# conditions such as minimum length and presence of required characters.
password=input("Enter a password: ")
if len(password) >= 8:
    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        print("The password is valid.")
    else:
        print("The password must contain both letters and digits.")
else:    
    print("The password must be at least 8 characters long.")
# 9. Write a Python program that checks whether a number lies between 100 and 999
# (inclusive) and is also an even number.
num=int(input("Enter a number: "))
if num >= 100 and num <= 999 and num % 2 == 0:
    print("The number lies between 100 and 999 and is an even number.")
else:   
    print("The number does not satisfy the condition.")
# 10. Write a Python program that checks whether a given character is neither a digit
# nor a special character, meaning it must be an alphabet.
char=input("Enter a character: ")
if char.isalpha():
    print("The character is an alphabet.")
else:    
    print("The character is not an alphabet.")
# 11. Write a Python program that checks whether a given temperature lies within a
# comfortable range, where both lower and upper limits are predefined.
temperature=float(input("Enter the temperature: "))
lower_limit=20.0
upper_limit=30.0
if temperature >= lower_limit and temperature <= upper_limit:
    print("The temperature is within the comfortable range.")
else:    
    print("The temperature is outside the comfortable range.")
# 12. Write a Python program that checks whether a number is divisible by 2, 3, or 5,
# and prints exactly which condition(s) the number satisfies.
num=int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is divisible by 2.")
if num % 3 == 0:
    print("The number is divisible by 3.")
if num % 5 == 0:
    print("The number is divisible by 5.")
if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print("The number is not divisible by 2, 3, or 5.")

# 13. Write a Python program that checks whether a person is eligible for a loan, based
# on conditions such as minimum age and minimum monthly income.
age=int(input("Enter your age: "))
income=float(input("Enter your monthly income: "))
if age >= 21 and income >= 30000:
    print("You are eligible for a loan.")
else:    
    print("You are not eligible for a loan.")
# 14. Write a Python program that checks whether a string is not empty and also has a
# length greater than 8 characters.
string=input("Enter a string: ")
if string and len(string) > 8:
    print("The string is not empty and has a length greater than 8 characters.")
else:
    print("The string is either empty or does not have a length greater than 8 characters.")
# 15. Write a Python program that accepts three sides of a triangle and checks whether
# the triangle is a right-angled triangle.
side1=float(input("Enter the length of side 1: "))
side2=float(input("Enter the length of side 2: "))
side3=float(input("Enter the length of side 3: "))
sides = sorted([side1, side2, side3])
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triangle is a right-angled triangle.")
else:    
    print("The triangle is not a right-angled triangle.")
# 16. Write a Python program that accepts a student’s percentage and classifies the
# performance as excellent, very good, good, average, or poor.
percentage=float(input("Enter the percentage: "))
if percentage >= 90:
    print("Excellent")
elif percentage >= 75:
    print("Very good")
elif percentage >= 60:
    print("Good")
elif percentage >= 40:
    print("Average")
else:    
    print("Poor")
# 17. Write a Python program that takes a number and determines whether it is positive
# even, positive odd, negative even, negative odd, or zero.
num=int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative even")
    else:
        print("Negative odd")
else:    
    print("Zero")
# 18. Write a Python program that calculates an electricity bill using slab-wise unit
# charges and prints the total bill amount.
units=float(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
print(f"Total electricity bill: {bill}")

# 19. Write a Python program that determines the tax slab of a person based on their
# annual income.
tax=float(input("Enter your annual income: "))
if tax <= 250000:
    print("No tax")
elif tax <= 500000:
    print("5% tax")
elif tax <= 1000000:
    print("20% tax")
else:    
    print("30% tax")
# 20.Write a Python program that accepts a day number (1–7) and determines whether it
# is a weekday or weekend.
day=int(input("Enter a day number (1-7): "))
if day in [1, 2, 3, 4, 5]:
    print("It is a weekday.")
else:
    print("It is a weekend.")
# 21. Write a Python program that checks a user’s internet data usage and categorizes it
# as low usage, medium usage, or high usage.
data_usage=float(input("Enter your internet data usage in GB: "))
if data_usage < 5:
    print("Low usage")
elif data_usage < 15:
    print("Medium usage")
else:    
    print("High usage")
# 22.Write a Python program that calculates the final payable amount after applying
# different discount slabs based on the purchase amount.
purchase_amount=float(input("Enter the purchase amount: "))
if purchase_amount < 100:
    discount = 0
elif purchase_amount < 500:
    discount = 0.05 * purchase_amount
elif purchase_amount < 1000:
    discount = 0.10 * purchase_amount
else:    
    discount = 0.15 * purchase_amount
print(f"Final payable amount after discount: {purchase_amount - discount}")
# 23.Write a Python program that accepts a BMI value and categorizes it as
# underweight, normal, overweight, or obese.
bmi=float(input("Enter your BMI value: "))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:    
    print("Obese")
# 24.Write a Python program that accepts a month number and prints the
# corresponding season (summer, rainy, or winter).
month=int(input("Enter a month number (1-12): "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:    
    print("Invalid month number")
# 25. Write a Python program that determines a student’s exam result category,
# considering pass marks and a small grace-marks rule.
marks=float(input("Enter the marks obtained: "))
pass_marks=40
grace_marks=5
if marks >= pass_marks:
    print("Pass")
elif marks >= pass_marks - grace_marks:
    print("Pass with grace marks")
else:    
    print("Fail")
# 26.Write a Python program that simulates a login system, first checking whether the
# username exists and then checking whether the password is correct.
username=input("Enter your username: ")
password=input("Enter your password: ")
stored_username="user123"
stored_password="pass123"   
if username == stored_username:
    if password == stored_password:
        print("Login successful.")
    else:
        print("Incorrect password.")
else:    
    print("Username does not exist.")

# 27. Write a Python program that simulates an ATM withdrawal system, where the
# program checks account balance, minimum balance requirement, and withdrawal
# amount.
account_balance=float(input("Enter your account balance: "))
withdrawal_amount=float(input("Enter the withdrawal amount: "))
minimum_balance=1000
if withdrawal_amount > account_balance:
    print("Insufficient funds.")
elif account_balance - withdrawal_amount < minimum_balance:
    print("Cannot withdraw. Minimum balance requirement not met.")
else:    
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. Remaining balance: {account_balance}")
# 28.Write a Python program that checks whether a student is eligible for admission,
# based on academic marks and an entrance test score.
academic_marks=float(input("Enter your academic marks: "))
entrance_test_score=float(input("Enter your entrance test score: "))
if academic_marks >= 75 and entrance_test_score >= 80:
    print("You are eligible for admission.")
else:    
    print("You are not eligible for admission.")
# 29.Write a Python program that first checks whether three given sides form a valid
# triangle, and if valid, determines the type of triangle.
side1=float(input("Enter the length of side 1: "))
side2=float(input("Enter the length of side 2: "))
side3=float(input("Enter the length of side 3: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
    else:    
        print("Scalene triangle")
else:    
    print("The sides do not form a valid triangle.")
# 30.Write a Python program that checks whether a student qualifies for a scholarship,
# considering marks, family income, and category.
marks=float(input("Enter your marks: "))
family_income=float(input("Enter your family income: "))
category=input("Enter your category (general, OBC, SC/ST): ")
if marks >= 85 and family_income < 500000:
    if category == "general":
        print("You qualify for a scholarship.")
    elif category == "OBC":
        print("You qualify for a scholarship with OBC benefits.")
    elif category == "SC/ST":
        print("You qualify for a scholarship with SC/ST benefits.")
    else:    
        print("Invalid category.")
else:    
    print("You do not qualify for a scholarship.")
# 31. Write a Python program that determines whether an employee is eligible for a
# bonus, based on performance rating and years of service.
performance_rating=float(input("Enter your performance rating (1-5): "))
years_of_service=int(input("Enter your years of service: "))
if performance_rating >= 4.5 and years_of_service >= 5:
    print("You are eligible for a bonus.")
else:    
    print("You are not eligible for a bonus.")
# 32.Write a Python program that validates a mobile number, checking its length and
# starting digit.
mobile_number=input("Enter your mobile number: ")
if len(mobile_number) == 10 and mobile_number[0] in ['6', '7', '8', '9']:
    print("The mobile number is valid.")
else:    
    print("The mobile number is invalid.")  
# 33.Write a Python program that validates password strength, checking multiple
# conditions such as length, digits, and special characters.
password=input("Enter a password: ")
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in "!@#$%^&*()-_+=" for char in password):
    print("The password is strong.")
else:    
    print("The password is weak. It must be at least 8 characters long and contain letters, digits, and special characters.")
# 34.Write a Python program that simulates an online shopping checkout, checking
# product availability and user wallet balance.
product_available=True
wallet_balance=float(input("Enter your wallet balance: "))
product_price=float(input("Enter the product price: "))
if product_available:
    if wallet_balance >= product_price:
        print("Checkout successful. Product purchased.")
    else:    
        print("Insufficient wallet balance. Please add funds.")
else:    
    print("Product is not available.")
# 35. Write a Python program that determines whether a vehicle is allowed on the road,
# based on fuel type and government rules.
fuel_type=input("Enter the fuel type of your vehicle (petrol, diesel, electric): ")
if fuel_type == "electric":
    print("Your vehicle is allowed on the road.")
elif fuel_type in ["petrol", "diesel"]:
    print("Your vehicle is allowed on the road, but consider switching to electric for environmental benefits.")
else:    
    print("Invalid fuel type.")