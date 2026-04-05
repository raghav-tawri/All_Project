# 1. Create a class called Student that has a class attribute school_name and
# instance attributes name and age which are initialized using a constructor. Create
# three objects and print both the class attribute and instance attributes for each
# object.
class Student:
    school_name = "ABC School"
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
print(f"School Name: {Student.school_name}")
print(f"Student 1 - Name: {student1.name}, Age: {student1.age}")
print(f"Student 2 - Name: {student2.name}, Age: {student2.age}")
# 2. Create a class called Car that has a class attribute wheels set to 4. Use a
# constructor to initialize instance attributes brand and price. Create two objects and
# show how both objects share the same class attribute but have different instance
# attributes.
class Car:
    wheels = 4
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
car1 = Car("Toyota", 20000)
car2 = Car("Honda", 25000)
print(f"Car 1 - Brand: {car1.brand}, Price: {car1.price}, Wheels: {Car.wheels}")
print(f"Car 2 - Brand: {car2.brand}, Price: {car2.price}, Wheels: {Car.wheels}")
# 3. Create a class called Employee that has a class attribute company_name.
# Initialize instance attributes emp_name and salary using a constructor. Create
# multiple employee objects and print their details along with the common company
# name.
class Employee:
    company_name = "XYZ Corporation"
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)
print(f"Employee 1 - Name: {employee1.emp_name}, Salary: {employee1.salary}, Company: {Employee.company_name}")
print(f"Employee 2 - Name: {employee2.emp_name}, Salary: {employee2.salary}, Company: {Employee.company_name}")
# 4. Create a class called Mobile that has a class attribute category set to
# Electronics. Use a constructor to initialize mobile_name and RAM. Create three
# objects and print all values to clearly understand class vs instance attributes.
class Mobile:
    category = "Electronics"
    def __init__(self, mobile_name, RAM):
        self.mobile_name = mobile_name
        self.RAM = RAM
mobile1 = Mobile("iPhone", "4GB")
mobile2 = Mobile("Samsung", "6GB")
mobile3 = Mobile("OnePlus", "8GB")
print(f"Mobile 1 - Name: {mobile1.mobile_name}, RAM: {mobile1.RAM}, Category: {Mobile.category}")
print(f"Mobile 2 - Name: {mobile2.mobile_name}, RAM: {mobile2.RAM}, Category: {Mobile.category}")
print(f"Mobile 3 - Name: {mobile3.mobile_name}, RAM: {mobile3.RAM}, Category: {Mobile.category}")
# 5. Create a class called Book that has a class attribute library_name. Initialize
# instance attributes title and author using a constructor. Create at least two objects
# and print their complete information.
class Book:
    library_name = "City Library"
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(f"Book 1 - Title: {book1.title}, Author: {book1.author}, Library: {Book.library_name}")
print(f"Book 2 - Title: {book2.title}, Author: {book2.author}, Library: {Book.library_name}")
# 6. Create a class called Laptop that has a class attribute warranty_years. Use a
# constructor to initialize brand and price. Create multiple laptop objects and display
# how the class attribute remains same for all objects.
class Laptop:
    warranty_years = 2
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
laptop1 = Laptop("Dell", 800)
laptop2 = Laptop("HP", 900)
print(f"Laptop 1 - Brand: {laptop1.brand}, Price: {laptop1.price}, Warranty: {Laptop.warranty_years} years")
print(f"Laptop 2 - Brand: {laptop2.brand}, Price: {laptop2.price}, Warranty: {Laptop.warranty_years} years")
# 7. Create a class called Person that has a class attribute country. Initialize instance
# attributes name and age using a constructor. Create three person objects and print
# their data.
class Person:
    country = "USA"
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)
print(f"Person 1 - Name: {person1.name}, Age: {person1.age}, Country: {Person.country}")
print(f"Person 2 - Name: {person2.name}, Age: {person2.age}, Country: {Person.country}")
print(f"Person 3 - Name: {person3.name}, Age: {person3.age}, Country: {Person.country}")
# 8. Create a class called Bike that has a class attribute type set to Two Wheeler.
# Use a constructor to initialize bike_name and mileage. Create objects and print all
# details.
class Bike:
    type = "Two Wheeler"
    def __init__(self, bike_name, mileage):
        self.bike_name = bike_name
        self.mileage = mileage
bike1 = Bike("Yamaha", 40)
bike2 = Bike("Honda", 45)
print(f"Bike 1 - Name: {bike1.bike_name}, Mileage: {bike1.mileage} km/l, Type: {Bike.type}")
print(f"Bike 2 - Name: {bike2.bike_name}, Mileage: {bike2.mileage} km/l, Type: {Bike.type}")
# 9. Create a class called Movie that has a class attribute industry set to Bollywood.
# Initialize instance attributes movie_name and rating using a constructor. Create
# multiple movie objects and print the details.
class Movie:
    industry = "Bollywood"
    def __init__(self, movie_name, rating):
        self.movie_name = movie_name
        self.rating = rating
movie1 = Movie("3 Idiots", 8.5)
movie2 = Movie("Dangal", 8.7)
print(f"Movie 1 - Name: {movie1.movie_name}, Rating: {movie1.rating}, Industry: {Movie.industry}")
print(f"Movie 2 - Name: {movie2.movie_name}, Rating: {movie2.rating}, Industry: {Movie.industry}")
# 10. Create a class called BankAccount that has a class attribute bank_name. Use
# a constructor to initialize account_holder and balance. Create two account objects
# and print their information showing both class and instance attributes.
class BankAccount:
    bank_name = "ABC Bank"
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
account1 = BankAccount("Alice", 5000)
account2 = BankAccount("Bob", 3000)
print(f"Account 1 - Holder: {account1.account_holder}, Balance: {account1.balance}, Bank: {BankAccount.bank_name}")
print(f"Account 2 - Holder: {account2.account_holder}, Balance: {account2.balance}, Bank: {BankAccount.bank_name}")
