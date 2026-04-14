import sys
import os
# from models.student import Student
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Models.student import Student

def main():
    sms = Student()
    
    while True:
        print("\n--- Advanced Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Display Last Added")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            s_id = int(input("ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            email = input("Email: ")
            sms.create(s_id, name, age, course, email)

        elif choice == '2':
            sms.display_all()

        elif choice == '3':
            sms.display_last()

        elif choice == '4':
            s_id = int(input("Enter ID to Update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")
            email = input("New Email: ")
            sms.update(s_id, name, age, course, email)

        elif choice == '5':
            s_id = int(input("Enter ID to Delete: "))
            sms.delete(s_id)

        else:
            print("Invalid choice ")
            break

if __name__ == "__main__":
    main()