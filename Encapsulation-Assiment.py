# 1. Create a class Person with a private variable __name. Create methods to set and get the name.
class Person:
    def __init__(self):
        self.__name = None
    def sets(self,value):
        self.__name=value
    def gets(self):
        print(f"The name of Person is {self.__name}")
obj1=Person()
obj1.sets("Alice")
obj1.gets()
# 2. Create a class BankAccount with private variable __balance. Add methods deposit(amount), withdraw(amount), and get_balance().
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print("amount deposited")
    def withdraw(self,amount):
        self.__balance=self.__balance-amount
        print("amount withraw")
    def get_balance(self):
        print(f"your courrent balance is {self.__balance}")
obj2=BankAccount()
obj2.deposit(1000)
obj2.withdraw(500)
obj2.get_balance()
# 3. Create a class Student with private variable __marks. Add methods to assign and display marks
class Student:
    def __init__(self):
        self.__marks=None
    def set_marks(self,marks):
        if marks>0:
            self.__marks=marks
        else:
            print("marks can't be negative")
    def get__marks(self):
        print("marks of student is ",self.__marks)
obj3=Student()
obj3.set_marks(85)
obj3.get__marks()      
# only if marks are greater than 0.
# 4. Create a class Employee with private variable __salary. Add methods to set salary, increase salary by percentage, and get salary.
class Employee:
    def __init__(self):
        self.__salary=None
    def set_salary(self,salary):
        self.__salary=salary
    def inc_salary(self,percentage):
        increment=(percentage/100)*self.__salary
        self.__salary=self.__salary+increment
    def get_salary(self):
        print(f"The salary is {self.__salary}")
obj4=Employee()
obj4.set_salary(50000)
obj4.inc_salary(10)
obj4.get_salary()
# 5. Create a class Temperature with private variable __celsius. Add methods to set temperature and convert it to Fahrenheit.
class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius
    def set_celsius(self, value):
        if value < -273.15:
            print("Temperature can't be zero -273.15C.")
        else:
            self.__celsius = value
    def get_celsius(self):
        return self.__celsius
    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
obj5=Temperature()
obj5.set_celsius(25)
print(f"Celsius: {obj5.get_celsius()}°C")
print(f"Fahrenheit: {obj5.to_fahrenheit()}°F")   
# 6. Create a class Mobile with private variable __price. Add methods to set price (not negative) and get price.
class Mobile:
    def __init__(self):
        self.__price=None
    def set_price(self,price):
        if price>0:
            self.__price=price
        else:
            print("price can't be negative")
    def get_price(self):
        print(f"price is {self.__price}")
obj6=Mobile()
obj6.set_price(15000)
obj6.get_price()
# 7. Create a class Car with private variable __speed. Add methods set_speed(speed <= 200) and get_speed().
class Car:
    def __init__(self,speed=0):
        self.__speed=speed
    def set_speed(self,speed):
        if speed<=200:
            self.__speed=speed
        else:
            print("speed can't be more than 200")
    def get_speed(self):
        print(f"price is {self.__speed}")
obj7=Car()
obj7.set_speed(150)
obj7.get_speed()
    
# 8. Create a class LoginSystem with private variable __password. Add methods to set and validate password.
# Attempting to access the private variable directly (will raise an AttributeError or a name mangling issue depending on context)
# print(login.__password) 
# The actual "private" variable name in Python is name-mangled to _LoginSystem__password
# print(login._LoginSystem__password) # This would work, but is against the convention of "private" variables
class LoginSystem:
    def __init__(self):
        self.__password=None
    def set_password(self,password):
        self.__password=password
    def validate_password(self,tryvalue):
        if self.__password==tryvalue:
            print("validation success")
        else:
            print("validation fail")
log=LoginSystem()
log.set_password("bcd boys")
print("login validation :-",log.validate_password("new value"))
print("login validation :-",log.validate_password("bcd boys"))
try:
    print(log.__password)
except AttributeError as e:
    print(f"Caught expected error: {e}")
print(f"Accessed via mangling: {log._LoginSystem__password}")

# 9. Create a class Product with private variable __quantity. Add methods to add stock, reduce stock (not below 0), and check quantity.
class Product:
    def __init__(self):
        self.__quantity=0
    def add_stock(self,new_stock):
        self.__quantity=self.__quantity+new_stock
    def reduce_stock(self,reduction):
        if (self.__quantity-reduction>0):
            self.__quantity=self.__quantity-reduction
        else:
            print("It can't be negative")
    def check_quantity(self):
        print(f"The quantity of stock is :- {self.__quantity}")
obj8=Product()
obj8.add_stock(100)
obj8.reduce_stock(30)
obj8.check_quantity()
# 10. Create a class VotingSystem with private variable __age. Add methods to set age and check if user can vote (>=18).
class VotingSystem:
    def __init__(self):
        self.__age = None
    def set_age(self,age):
        if age > 0:
            self.__age=age
        else:
            print("Age must be a positive")
    def can_vote(self):
        if self.__age >= 18:
            return True
        else:
            return False
user1 = VotingSystem()
user1.set_age(20)
if user1.can_vote():
    print("User is eligible")
else:
    print("User is not eligible")

