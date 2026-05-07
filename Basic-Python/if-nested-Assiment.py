# 1. Write a program using nested if to check whether a number is positive,
# negative, or zero, and if positive, also check whether it is even or odd.
n=8
if n ==0:
    print("The number is Zero")
elif n>0:
    if n%2==0:
        print("It is an Even positive number")
    else:
        print("It's an Odd positive number")
else:
    print("It's an Negative number")
# 2. Write a program using nested if to find the greatest among three numbers.
a=9
b=7
c=6
if(a>b and a>c):
    print(f"{a} is largest")
elif(b>a and b>c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
# 3. Write a program using nested if to check whether a student has passed or
# failed, and if passed, assign a grade based on marks.
marks=80
if (marks>33):
    print("Passed")
    if(marks>90):
        print("Grade A+")
    elif(marks>80):
        print("Grade B-")
    elif(marks>70):
        print("Grade B+")
    elif(marks>60):
        print("Grade B-")
    elif(marks>50):
        print("Grade C")
    elif(marks>40):
        print("Grade D")
    else:
        print("Grade E")
else:
    print("Fail")
# 4. Write a program using nested if to check whether a person is eligible to
# vote, and if eligible, check whether they are a first-time voter.
age=18
if(age>=18):
    print("Can vote")
else:
    print("Can't Vote")
# 5. Write a program using nested if to check whether a number is divisible by
# 5, and if yes, check whether it is also divisible by 10.
number=30
if(number%5==0):
    print("Number is divisible by 5")
    if(number%10==0):
        print("Number is also divisible by 10")
else:
    print("It is not divisible by 5")
# 6. Write a program using nested if to check whether a character is an
# alphabet, and if it is an alphabet, check whether it is a vowel or consonant.
strs="s"
vowel=['a','e','i','o','u']
if(strs.isalpha()):
    print("It is an alphabet")
    if(strs in vowel):
        print("It's is also an Vowel")
else:
    print("It's not an alphabet")
# 7. Write a program using nested if to check whether a person is eligible for a
# job based on age, and if eligible, check whether they have the required
# qualification.
age=25
qualification="Bachelors"
if(age>=18 and age<=60):
    print("Eligible for job")
    if(qualification=="Bachelors" or qualification=="Masters"):
        print("Has required qualification")
    else:
        print("Doesn't have required qualification")
else:
    print("Not eligible for job")

# 8. Write a program using nested if to check whether a number is greater than
# 50, and if yes, check whether it is also greater than 100.
num=120
if(num>50):
    print("Number is greater than 50")
    if(num>100):
        print("Number is also greater than 100")
else:
    print("Number is not greater than 50")
# 9. Write a program using if-elif-else to check whether a number is positive,
# negative, or zero.
n=0
if n ==0:
    print("The number is Zero")
elif n>0:
    print("The number is Positive")
else:    
    print("The number is Negative")
# 10. Write a program using elif to assign grades based on marks:
# A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
marks=85
if(marks>90):
    print("Grade A")
elif(marks>80):
    print("Grade B")
elif(marks>70):
    print("Grade C")
elif(marks>60):
    print("Grade D")
else:
    print("Grade F")
# 11. Write a program using elif to check whether a given day number (1–7)
# corresponds to Monday–Sunday.
day=3
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
elif(day==6):
    print("Saturday")
elif(day==7):
    print("Sunday")
else:
    print("Invalid day number")
# 12. Write a program using elif to find the largest among three numbers.
a=9
b=7
c=6
if(a>b and a>c):
    print(f"{a} is largest")
elif(b>a and b>c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest")    
# 13. Write a program using elif to check whether a year is a leap year or not.
year=2020
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:    
    print("It is not a leap year")
# 14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or
# Senior.
age=25
if(age>=0 and age<=12):
    print("Child")
elif(age<=19):
    print("Teen")
elif(age<=59):
    print("Adult")
elif(age>=60):
    print("Senior")
else:
    print("Invalid age")
# 15. Write a program using elif to check whether a character is a vowel, consonant,
# digit, or special character.
char='@'
vowel=['a','e','i','o','u']
if(char.isalpha()):
    if(char in vowel):
        print("It is a vowel")
    else:
        print("It is a consonant")
elif(char.isdigit()):
    print("It is a digit")
else:
    print("It is a special character")
# 16. Write a program using elif to build a simple calculator for +, -, *, and /.
num1=10
num2=5
operator='+'
if(operator=='+'):  
    print(f"{num1} + {num2} = {num1+num2}")
elif(operator=='-'):
    print(f"{num1} - {num2} = {num1-num2}")
elif(operator=='*'):    
    print(f"{num1} * {num2} = {num1*num2}")
elif(operator=='/'):
    if(num2!=0):
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
# 17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
# none of them.
num=15
if(num%2==0):
    print("Number is divisible by 2")
elif(num%3==0):
    print("Number is divisible by 3")
elif(num%5==0):
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 2, 3, or 5")
# 18. Write a program using elif to convert a numeric month value (1–12) into the month
# name.
month=4
if(month==1):
    print("January")
elif(month==2):   
    print("February")
elif(month==3):
    print("March")
elif(month==4):
    print("April")
elif(month==5):
    print("May")
elif(month==6):
    print("June")
elif(month==7):
    print("July")
elif(month==8):
    print("August")
elif(month==9):
    print("September")
elif(month==10):
    print("October")
elif(month==11):
    print("November")
elif(month==12):
    print("December")
else:
    print("Invalid month number")
# 19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
# Scalene.
side1=5
side2=5
side3=5
if(side1==side2==side3):
    print("Equilateral triangle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("Isosceles triangle")
else:    
    print("Scalene triangle")
# 20. Write a program using elif to determine the season based on month number.
month=4
if(month in [12, 1, 2]):
    print("Winter")
elif(month in [3, 4, 5]):
    print("Spring")
elif(month in [6, 7, 8]):
    print("Summer")
elif(month in [9, 10, 11]):
    print("Autumn")
else:
    print("Invalid month number")

# 21. Write a program using elif to calculate electricity bill based on unit ranges.
units=150
if(units<=100):
    bill=units*5
elif(units<=200):
    bill=100*5 + (units-100)*7
elif(units<=300):
    bill=100*5 + 100*7 + (units-200)*10
else:
    bill=100*5 + 100*7 + 100*10 + (units-300)*15
print(f"Electricity bill: {bill}")

# 22. Write a program using elif to check whether a number is one-digit, two-digit,
# three-digit, or more.
num=123
if(num>=0 and num<=9):
    print("One-digit number")
elif(num>=10 and num<=99):
    print("Two-digit number")
elif(num>=100 and num<=999):
    print("Three-digit number")
else:    
    print("More than three-digit number")
# 23. Write a program using elif to check the result of a student: Distinction, First
# Class, Second Class, Pass, or Fail.
marks=85
if(marks>=90):
    print("Distinction")
elif(marks>=75):
    print("First Class")
elif(marks>=60):
    print("Second Class")
elif(marks>=33):
    print("Pass")
else:    
    print("Fail")
# 24. Write a program using elif to convert percentage into grade category.
percentage=85
if(percentage>=90):
    print("Grade A")
elif(percentage>=80):
    print("Grade B")
elif(percentage>=70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
elif(percentage>=50):
    print("Grade E")
else:    
    print("Grade F")
# 25. Write a program using elif to check traffic light action based on color input.
color="Green"
if(color=="Red"):
    print("Stop")
elif(color=="Yellow"):
    print("Ready")
elif(color=="Green"):
    print("Go")
else:   
    print("Invalid traffic light color")
# 26. Write a program using elif to classify temperature as Cold, Moderate, or Hot.
temperature=30
if(temperature<15):
    print("Cold")
elif(temperature<=25):
    print("Moderate")
else:    
    print("Hot")
# 27. Write a program using elif to check whether a number is prime, composite, or
# neither.
num=17
if(num>1):
    for i in range(2, num):
        if(num%i==0):
            print("Composite")
            break
    else:
        print("Prime")
else:
    print("Neither prime nor composite")

# 28. Write a program using elif to check the type of input number: zero, positive even,
# positive odd, or negative.
num=-5
if(num==0):
    print("Zero")
elif(num>0):
    if(num%2==0):
        print("Positive even")
    else:
        print("Positive odd")
else:    
    print("Negative")