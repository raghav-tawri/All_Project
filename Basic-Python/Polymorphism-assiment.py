# 1. Create a base class Animal with a method sound(). Then create three child classes Dog, Cat, and
# Cow that override the sound() method to print their respective sounds. Write a main program where you
# create objects of each class and call the sound() method using a parent class reference to demonstrate
# runtime polymorphism.
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")
objects = [Dog(), Cat(), Cow()]
for obj in objects:
    obj.sound()
# 2. Create a base class Vehicle with a method start(). Then create child classes Car, Bike, and Truck
# that override the start() method with their own implementation. Demonstrate how the correct method is
# called at runtime when using a common reference.
class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")  
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")
class Truck(Vehicle):
    def start(self):
        print("Truck starts with a diesel engine")
vehicles = [Car(), Bike(), Truck()]
for vehicle in vehicles:
    vehicle.start()
# 3. Create a base class Shape with a method area(). Then create child classes Circle and Rectangle.
# Override the area() method in both classes to calculate their respective areas. Use dynamic method
# dispatch to call the correct area() method.
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())
# 4. Create a base class Employee with a method salary(). Then create subclasses FullTimeEmployee
# and PartTimeEmployee. Override the salary() method in each subclass to calculate salary differently.
# Demonstrate runtime polymorphism using these classes.
class Employee:
    def salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def salary(self):
        return self.monthly_salary * 12
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def salary(self):
        return self.hourly_rate * self.hours_worked
employees = [FullTimeEmployee(5000), PartTimeEmployee(20, 100)]
for employee in employees:
    print("Annual Salary:", employee.salary())
# 5. Create a base class Bank with a method interest_rate(). Then create subclasses SBI, HDFC, and
# ICICI. Each subclass should override the interest_rate() method with different values. Write a program
# to show polymorphic behavior.
class Bank:
    def interest_rate(self):
        pass
class SBI(Bank):
    def interest_rate(self):
        return 4.0
class HDFC(Bank):
    def interest_rate(self):
        return 5.0
class ICICI(Bank):
    def interest_rate(self):
        return 4.5
banks = [SBI(), HDFC(), ICICI()]
for bank in banks:
    print("Interest Rate:", bank.interest_rate())
# 6. Create a base class Payment with a method pay(amount). Then create subclasses
# CreditCardPayment, UPIPayment, and CashPayment that override the pay() method with different
# logic. Show how runtime polymorphism works when calling the method.
class Payment:
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash")
payments = [CreditCardPayment(), UPIPayment(), CashPayment()]
for payment in payments:
    payment.pay(100)
# 7. Create a base class Notification with a method send(message). Then create subclasses
# EmailNotification, SMSNotification, and PushNotification. Each subclass should override the send()
# method. Demonstrate polymorphism using a loop.
class Notification:
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")
class PushNotification(Notification):
    def send(self, message):
        print(f"Push notification sent: {message}")
notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for notification in notifications:
    notification.send("Hello, this is a notification!")
# 8. Create a base class Media with a method play(). Then create subclasses Audio, Video, and Podcast.
# Override the play() method in each subclass. Show how different play() methods are called
# dynamically.
class Media:
    def play(self):
        pass
class Audio(Media):
    def play(self):
        print("Playing audio")
class Video(Media):
    def play(self):
        print("Playing video")
class Podcast(Media):
    def play(self):
        print("Playing podcast")
media_items = [Audio(), Video(), Podcast()]
for media in media_items:
    media.play()
# 9. Create a base class User with a method access_level(). Then create subclasses Admin, Editor, and
# Viewer. Override the access_level() method to return different permissions. Demonstrate runtime
# polymorphism.
class User:
    def access_level(self):
        pass
class Admin(User):
    def access_level(self):
        return "Admin has full access"
class Editor(User):
    def access_level(self):
        return "Editor has edit access"
class Viewer(User):
    def access_level(self):
        return "Viewer has read-only access"
users = [Admin(), Editor(), Viewer()]
for user in users:
    print(user.access_level())
# 10. Create a base class Appliance with a method turn_on(). Then create subclasses Fan, AC, and
# WashingMachine. Override the turn_on() method with specific behavior. Show polymorphism using a
# collection of objects.
class Appliance:
    def turn_on(self):
        pass
class Fan(Appliance):
    def turn_on(self):
        print("Fan is turned on")
class AC(Appliance):
    def turn_on(self):
        print("AC is turned on")
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is turned on")
appliances = [Fan(), AC(), WashingMachine()]
for appliance in appliances:
    appliance.turn_on()
# 11. Create a base class Account with a method withdraw(amount). Then create subclasses
# SavingsAccount and CurrentAccount. Override withdraw() with different rules such as minimum
# balance or overdraft. Demonstrate runtime polymorphism.
class Account:
    def withdraw(self, amount):
        pass
class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Cannot withdraw. Minimum balance must be maintained.")
class CurrentAccount(Account):
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Cannot withdraw. Overdraft limit exceeded.")
accounts = [SavingsAccount(5000), CurrentAccount(2000)]
accounts[0].withdraw(4000) 
accounts[1].withdraw(2500)
# 12. Create a base class GameCharacter with a method attack(). Then create subclasses Warrior,
# Mage, and Archer. Override attack() with different behaviors. Show dynamic method selection at
# runtime.
class GameCharacter:
    def attack(self):
        pass
class Warrior(GameCharacter):
    def attack(self):
        print("Warrior attacks with a sword")
class Mage(GameCharacter):
    def attack(self):
        print("Mage casts a fireball")
class Archer(GameCharacter):
    def attack(self):
        print("Archer shoots an arrow")
characters = [Warrior(), Mage(), Archer()]
for character in characters:
    character.attack()
# 13. Create a base class FileHandler with a method open(). Then create subclasses TextFile, ImageFile,
# and PDFFile. Override open() to simulate opening different file types. Demonstrate runtime
# polymorphism.
class FileHandler:
    def open(self):
        pass
class TextFile(FileHandler):
    def open(self):
        print("Opening text file")
class ImageFile(FileHandler):
    def open(self):
        print("Opening image file")
class PDFFile(FileHandler):
    def open(self):
        print("Opening PDF file")
files = [TextFile(), ImageFile(), PDFFile()]
for file in files:
    file.open()
# 14. Create a base class Transport with a method fare(distance). Then create subclasses Bus, Train,
# and Taxi. Override fare() with different fare calculation logic. Show polymorphism using different
# objects.
class Transport:
    def fare(self, distance):
        pass
class Bus(Transport):
    def fare(self, distance):
        return distance * 0.5
class Train(Transport):
    def fare(self, distance):
        return distance * 0.3
class Taxi(Transport):
    def fare(self, distance):
        return distance * 1.0
transports = [Bus(), Train(), Taxi()]
for transport in transports:
    print(f"Fare for 10 km: {transport.fare(10)}")
# 15. Create a base class SmartDevice with a method operate(). Then create subclasses SmartLight,
# SmartTV, and SmartSpeaker. Override operate() to perform device-specific actions. Demonstrate
# runtime polymorphism using a list of objects.
class SmartDevice:
    def operate(self):
        pass
class SmartLight(SmartDevice):
    def operate(self):
        print("Smart Light is turned on")
class SmartTV(SmartDevice):
    def operate(self):
        print("Smart TV is turned on")
class SmartSpeaker(SmartDevice):
    def operate(self):
        print("Smart Speaker is playing music")
devices = [SmartLight(), SmartTV(), SmartSpeaker()]
for device in devices:
    device.operate()