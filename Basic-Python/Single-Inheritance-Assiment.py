# 1. Vehicle → Car
# Vehicle: brand, speed. Car: fuel_type. Use super(). Display all.
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Car(Vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type
    def display(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h, Fuel Type: {self.fuel_type}")
car1=Car("Toyota",120,"Petrol")
car1.display()
# 2. Person → Teacher
# Person: name, age. Teacher: subject. Use super(). Display all.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")
teacher1=Teacher("Mr. Smith",40,"Mathematics")
teacher1.display()
# 3. Employee → Manager
# Employee: emp_id, salary. Manager: department. Use super().
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
class Manager(Employee):
    def __init__(self,emp_id,salary,department):
        super().__init__(emp_id,salary)
        self.department=department
    def display(self):
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}, Department: {self.department}")
manager1=Manager("E123",50000,"Sales")
manager1.display()
# 4. Product → Electronics
# Product: name, price. Electronics: warranty_years. Use super().
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self,name,price,warranty_years):
        super().__init__(name,price)
        self.warranty_years=warranty_years
    def display(self):
        print(f"Product Name: {self.name}, Price: ${self.price}, Warranty: {self.warranty_years} years")
electronic1=Electronics("Smartphone",699,2)
electronic1.display()
# 5. Animal → Dog
# Animal: name, species. Dog: breed. Use super().
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def display(self):
        print(f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}")
dog1=Dog("Buddy","Canine","Golden Retriever")
dog1.display()
# 6. Account → SavingsAccount
# Account: account_number, balance. SavingsAccount: interest_rate. Use super().
class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
class SavingsAccount(Account):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%")
savings1=SavingsAccount("A123",1000,5)
savings1.display()
# 7. User → Admin
# User: username, email. Admin: permissions. Use super().
class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
class Admin(User):
    def __init__(self,username,email,permissions):
        super().__init__(username,email)
        self.permissions=permissions
    def display(self):
        print(f"Username: {self.username}, Email: {self.email}, Permissions: {self.permissions}")
admin1=Admin("admin_user","admin@example.com",["read","write","delete"])
admin1.display()
# 8. Book → Ebook
# Book: title, author. Ebook: file_size. Use super().
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class Ebook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size=file_size
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB")
ebook1=Ebook("The Great Gatsby","F. Scott Fitzgerald",2)
ebook1.display()
# 9. Appliance → WashingMachine
# Appliance: brand, power. WashingMachine: capacity. Use super().
class Appliance:
    def __init__(self,brand,power):
        self.brand=brand
        self.power=power
class WashingMachine(Appliance):
    def __init__(self,brand,power,capacity):
        super().__init__(brand,power)
        self.capacity=capacity
    def display(self):
        print(f"Brand: {self.brand}, Power: {self.power} W, Capacity: {self.capacity} kg")
washing_machine1=WashingMachine("LG",2000,7)
washing_machine1.display()
# 10. Shape → Circle
# Shape: color. Circle: radius. Use super().
class Shape:
    def __init__(self,color):
        self.color=color
class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
    def display(self):
        print(f"Color: {self.color}, Radius: {self.radius} cm")
circle1=Circle("Red",5)
circle1.display()
# 11. Device → Laptop
# Device: name, price. Laptop: ram. Use super().
class Device:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Laptop(Device):
    def __init__(self,name,price,ram):
        super().__init__(name,price)
        self.ram=ram
    def display(self):
        print(f"Device Name: {self.name}, Price: ${self.price}, RAM: {self.ram} GB")
laptop1=Laptop("MacBook Pro",1299,16)
laptop1.display()
# 12. Food → Fruit
# Food: name, calories. Fruit: vitamin_content. Use super().
class Food:
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
class Fruit(Food):
    def __init__(self,name,calories,vitamin_content):
        super().__init__(name,calories)
        self.vitamin_content=vitamin_content
    def display(self):
        print(f"Food Name: {self.name}, Calories: {self.calories} kcal, Vitamin Content: {self.vitamin_content}")
fruit1=Fruit("Apple",95,"Vitamin C")
fruit1.display()
# 13. Company → Startup
# Company: name, location. Startup: funding_amount. Use super().
class Company:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class Startup(Company): 
    def __init__(self,name,location,funding_amount):
        super().__init__(name,location)
        self.funding_amount=funding_amount
    def display(self):
        print(f"Company Name: {self.name}, Location: {self.location}, Funding Amount: ${self.funding_amount}")
startup1=Startup("Tech Innovators","Silicon Valley",5000000)
startup1.display()
# 14. Movie → WebSeries
# Movie: title, duration. WebSeries: number_of_seasons. Use super().
class Movie:
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
class WebSeries(Movie):
    def __init__(self,title,duration,number_of_seasons):
        super().__init__(title,duration)
        self.number_of_seasons=number_of_seasons
    def display(self):
        print(f"Title: {self.title}, Duration: {self.duration} minutes, Number of Seasons: {self.number_of_seasons}")
web_series1=WebSeries("Stranger Things",50,4)
web_series1.display()
# 15. Bank → Loan
# Bank: name, branch. Loan: loan_amount. Use super().
class Bank:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
class Loan(Bank):
    def __init__(self,name,branch,loan_amount):
        super().__init__(name,branch)
        self.loan_amount=loan_amount
    def display(self):
        print(f"Bank Name: {self.name}, Branch: {self.branch}, Loan Amount: ${self.loan_amount}")
loan1=Loan("ABC Bank","Downtown",100000)
loan1.display()
# 16. Course → OnlineCourse
# Course: course_name, duration. OnlineCourse: platform. Use super().
class Course:
    def __init__(self,course_name,duration):
        self.course_name=course_name
        self.duration=duration
class OnlineCourse(Course):
    def __init__(self,course_name,duration,platform):
        super().__init__(course_name,duration)
        self.platform=platform
    def display(self):
        print(f"Course Name: {self.course_name}, Duration: {self.duration} hours, Platform: {self.platform}")
online_course1=OnlineCourse("Python Programming",40,"Udemy")
online_course1.display()
# 17. Game → MobileGame
# Game: title, genre. MobileGame: size. Use super().
class Game:
    def __init__(self,title,genre):
        self.title=title
        self.genre=genre
class MobileGame(Game):
    def __init__(self,title,genre,size):
        super().__init__(title,genre)
        self.size=size
    def display(self):
        print(f"Game Title: {self.title}, Genre: {self.genre}, Size: {self.size} GB")
mobile_game1=MobileGame("Minecraft", "Sandbox", 1.2)
mobile_game1.display()
# 18. Hospital → Doctor
# Hospital: name, location. Doctor: specialization. Use super().
class Hospital:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class Doctor(Hospital):
    def __init__(self,name,location,specialization):
        super().__init__(name,location)
        self.specialization=specialization
    def display(self):
        print(f"Doctor Name: {self.name}, Location: {self.location}, Specialization: {self.specialization}")
doctor1=Doctor("Dr. Smith","City Hospital","Cardiology")
doctor1.display()
# 19. Transport → Bus
# Transport: mode, fare. Bus: route_number. Use super().
class Transport:
    def __init__(self,mode,fare):
        self.mode=mode
        self.fare=fare
class Bus(Transport):
    def __init__(self,mode,fare,route_number):
        super().__init__(mode,fare)
        self.route_number=route_number
    def display(self):
        print(f"Transport Mode: {self.mode}, Fare: ${self.fare}, Route Number: {self.route_number}")
bus1=Bus("Bus",2.5,101)
bus1.display()
# 20. Clothing → Shirt
# Clothing: brand, size. Shirt: color. Use super().
class Clothing:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
class Shirt(Clothing):
    def __init__(self,brand,size,color):
        super().__init__(brand,size)
        self.color=color
    def display(self):
        print(f"Brand: {self.brand}, Size: {self.size}, Color: {self.color}")
shirt1=Shirt("Nike","M","Blue")
shirt1.display()