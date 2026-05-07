# MULTIPLE INHERITANCE QUESTIONS
# 1. Create two classes Father and Mother with methods skills_father() and skills_mother(). Create a child class Child that inherits from both and prints both skills.
class Father:
    def skills_father(self):
        print("father skill")
class Mother:
    def skills_mother(self):
        print("Mother skill")
class Child(Father,Mother):
    pass
obj=Child()
obj.skills_father()
obj.skills_mother()

# 2. Write a program where class Teacher has a method teach() and class Researcher has a method research(). Create a class Professor that inherits from both and uses both methods.
class Teacher:
    def teach(self):
        print("Teacher teach")
class Researcher:
    def research(self):
        print("Research by Researcher")
class Professor(Teacher,Researcher):
    pass
obj2=Professor()
obj2.teach()
obj2.research()
# 3. Create two classes Engine and ElectricSystem with respective methods. Create a class
# HybridCar that inherits from both and demonstrates both functionalities.
class Engine:
    def engine_fun(self):
        print("Petrol Engine Car")
class ElectricSystem:
    def ele_sys_sys(self):
        print("EV Battery Car")
class HybridCar(Engine,ElectricSystem):
    pass
obj3=HybridCar()
obj3.engine_fun()
obj3.ele_sys_sys()
# 4. Implement two classes Writer and Speaker with methods write() and speak(). Create a class Author that inherits from both and calls both methods.
class Writer:
    def write(self):
        print("Write the thing")
class Speaker:
    def speak(self):
        print("Speak")
class Auther(Writer,Speaker):
    pass
obj4=Auther()
obj4.speak()
obj4.write()
# 5. Create two parent classes Calculator1 (addition) and Calculator2 (multiplication). Create a child class that uses both operations.
class Calculator1:
    def addition(self,a,b):
        self.a=a
        self.b=b
        print("Addition",a+b)
class Calculator2:
    def Multiplication(self,a,b):
        self.a=a
        self.b=b
        print("Multplication",a*b)
class Calculator3(Calculator1,Calculator2):
    def calc3_add(self,a,b):
        super().addition(a,b)
    def calc3_multi(self,a,b):
        super().Multiplication(a,b)
obj5=Calculator3()
obj5.calc3_add(3,4)
obj5.calc3_multi(5,6)
# 6. Demonstrate method overriding in multiple inheritance where both parent classes have a method
# with the same name.
class Dog:
    def speak(self):
        print("speak by dog")
class Cat:
    def speak(self):
        print("speak by cat")
class Child(Dog, Cat):
    def speak_cat(self):
        Cat.speak(self)
obj6 = Child()
obj6.speak()
obj6.speak_cat()
# 7. Create a class A and B with constructors. Create class C inheriting from both and show how
# constructors are called.
class A:
    def __init__(self):
        print("A constructer called")
        super().__init__()
class B:
    def __init__(self):
        print("B constructer called")
        super().__init__()
class C(A,B):
    def __init__(self):
        print("C constructer Called")
        super().__init__()
obj7=C()
# 8. Write a program to demonstrate the Method Resolution Order (MRO) in multiple inheritance.
print(C.mro())
# 9. Create two classes Person and Employee with attributes. Inherit both into Manager and display
# combined details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, depart):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.depart = depart
    def display(self):
        print("--- Manager Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.depart}")
obj8 = Manager("Alice Smith", 42, "MGR101", 95000, "Operations")
obj8.display()
# 10. Implement a class SmartDevice that inherits from both Phone and Camera and performs both
# calling and clicking photos.
class Phone:
    def callings(self):
        print(f"Calling from ...")
class Camera:
    def click_photo(self):
        print(f"Clicking a MP photo...")
class SmartDevice(Phone, Camera):
    def display(self):
        print(f"Smart Device")
obj9 = SmartDevice()
obj9.callings()
obj9.click_photo()
obj9.display()

# MULTILEVEL INHERITANCE QUESTIONS
# 1. Create class Grandparent, Parent, and Child. Add methods in each and show how child accesses all.
class Grandparent:
    def grandparent_method(self):
        print("Accessing Grandparent method")
class Parent(Grandparent):
    def parent_method(self):
        print("Accessing Parent method")
class Child(Parent):
    def child_method(self):
        print("Accessing Child method")
obj10 = Child()
obj10.grandparent_method()
obj10.parent_method()
obj10.child_method()
# 2. Write a program where Animal → Mammal → Dog and each class has its own method. Call all
# methods using the Dog class.
class Animal:
    def bite(self):
        print("animal bite")
class Mammal(Animal):
    def walk(self):
        print("mammal walk")
class Dog(Mammal):
    def speak(self):
        print("Dog Bark")
obj11 = Dog()
obj11.bite()
obj11.walk()
obj11.speak()
# 3. Create a class Vehicle, then Car inherits from it, and SportsCar inherits from Car. Add methods
# at each level.
class Vehicle:
    def speed(self):
        print("Vehicle running")
class Car(Vehicle):
    def fuel(self):
        print("Petrol cal function")
class SportsCar(Car):
    def f1(self):
        print("F1 sports car")
obj12=SportsCar()
obj12.f1()
obj12.fuel()
obj12.speed()
# 4. Demonstrate constructor chaining in multilevel inheritance using super().
class A:
    def __init__(self):
        print("A constructer called")
        super().__init__()
class B(A):
    def __init__(self):
        print("B constructer called")
        super().__init__()
class C(B):
    def __init__(self):
        print("C constructer called")
        super().__init__()
obj12=C()
# 5. Create a class Shape → Rectangle → Square and calculate area at each level.
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def rect_area(self,l,b):
        print(f"Area of rectangle is {l*b}")
class square(Rectangle):
    def sqar_area(self,n):
        print(f"Area of square {n*n}")
obj13=square()
obj13.sqar_area(12)
obj13.rect_area(12,34)
# 6. Write a program showing method overriding in multilevel inheritance.
class Grandparent:
    def display(self):
        print("This is the Grandparent")
class Parent(Grandparent):
    def display(self):
        print("This is the Parent")
class Child(Parent):
    def display(self):
        super().display()
        print("This is the Child")
obj14 = Child()
obj14.display()
# 7. Create a class Student → GraduateStudent → PhDStudent and add attributes progressively.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class GraduateStudent(Student):
    def __init__(self,name,age,degree,course):
        super().__init__(name,age)
        self.degree=degree
        self.course=course
class PhDStudent(GraduateStudent):
    def __init__(self,name,age,degree,course,phd):
        super().__init__(name,age,degree,course)
        self.phd=phd
    def display(self):
        print(f"Name:- {self.name} Age:- {self.age} Degree:- {self.degree} Course:- {self.course} PhD:- {self.phd}")
obj15=PhDStudent('Raghav',12,'BCA','MCA',3)
obj15.display()
# 8. Implement a banking system: Account → SavingsAccount → FixedDepositAccount.
class Account:
    def __init__(self,holder_name, balance=0.0):
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display(self):
        print(f"Holder: {self.holder_name} | Balance: ${self.balance:.2f}")
class SavingsAccount(Account):
    def __init__(self,holder_name, balance=0.0, interest_rate=0.02):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate
    def add_int(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
class FixedDepositAccount(SavingsAccount):
    def __init__(self,holder_name, balance=0.0, interest_rate=0.05, tenure_months=12):
        super().__init__(holder_name, balance, interest_rate)
        self.tenure_months = tenure_months
    def withdraw(self, amount):
        penalty = amount * 0.05
        total_deduction = amount + penalty
        self.balance -= total_deduction
gen_acc = Account("Alice", 1000)
sav_acc = SavingsAccount("Bob", 5000,0.03)
fd_acc = FixedDepositAccount("Charlie", 10000,0.06,24)
gen_acc.deposit(500)
gen_acc.withdraw(200)
gen_acc.display()
sav_acc.add_int()
sav_acc.display()
fd_acc.withdraw(1000)
fd_acc.display()
# 9. Create a class Device → Computer → Laptop and show functionality extension.
class Device:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
class Computer(Device):
    def __init__(self, brand, name, processor, ram):
        super().__init__(brand, name)
        self.processor = processor
        self.ram = ram
class Laptop(Computer):
    def __init__(self, brand, name, processor, ram, battery_level):
        super().__init__(brand, name, processor, ram)
        self.battery_level = battery_level
    def check_battery(self):
        print(f"Battery at {self.battery_level}%.")
    def display(self):
        print(f"Name:- {self.brand} Age:- {self.name} Degree:- {self.processor} Course:- {self.ram} PhD:- {self.battery_level}")
obj17 = Laptop("Apple", "MacBook Pro", "M3 Max", "32GB", 15)
obj17.check_battery()
obj17.display()
# 10. Write a program where each class in multilevel inheritance modifies a variable and shows how
# values change.
class Grand:
    def __init__(self):
        self.value = 10
        print(f"value initialized to: {self.value}")
class GrandB(Grand):
    def __init__(self):
        super().__init__()
        self.value += 20
        print(f"value modified to: {self.value}")
class GrandC(GrandB):
    def __init__(self):
        super().__init__()
        self.value *= 2
        print(f"value modified by another one to: {self.value}")
obj18 = GrandC()
print(f"Final value in Child instance: {obj18.value}")

# MIXED / CONCEPTUAL QUESTIONS
# 1. Combine both multiple and multilevel inheritance in a single program and demonstrate method
# calls.
class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    def method_c(self):
        print("Method C")
class D(C):
    def method_d(self):
        print("Method D")
obj19 = D()
obj19.method_a()
obj19.method_b()
obj19.method_c()
obj19.method_d()

# 2. Create a diamond problem scenario and resolve it using Python’s MRO.
class A:
    def method(self):
        print("Method in A")
class B(A):
    def method(self):
        print("Method in B")
class C(A):
    def method(self):
        print("Method in C")
class D(B, C):
    def method(self):
        print("Method in D")
obj20 = D()
obj20.method()
print(D.mro())
# 3. Write a program to print the MRO of a complex inheritance structure.
class X:
    pass
class Y(X):
    pass
class Z(X):
    pass
class W(Y, Z):
    pass
print(W.mro())
# 4. Create a system where one class inherits from two classes, and one of those classes further
# inherits from another (hybrid inheritance).
class A:
    def method_a(self):
        print("Method A")
class B:
    def method_b(self):
        print("Method B")
class C(A, B):
    def method_c(self):
        print("Method C")
class D(C):
    def method_d(self):
        print("Method D")
obj21 = D()
obj21.method_a()
obj21.method_b()
obj21.method_c()
obj21.method_d()

# 5. Build a mini project: Employee management system using both inheritance types.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
class TeamLead(Manager, Developer):
    def __init__(self, name, emp_id, department, programming_language):
        Manager.__init__(self, name, emp_id, department)
        Developer.__init__(self, name, emp_id, programming_language)
    def display(self):
        Manager.display(self)
        Developer.display(self)
obj22 = TeamLead("Alice", "TL001", "Software Development", "Python")
obj22.display()
