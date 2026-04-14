import sys
import os
# from models.student import Student
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.student_services import StudentService

class Student:
    def __init__(self):
        self.service = StudentService()

    def create(self, s_id, name, age, course, email):
        if self.service.insert_student(s_id, name, age, course, email):
            print("\nStudent added")

    def display_all(self):
        records = self.service.fetch_all()
        print("\n--- All Student Records ---")
        for row in records:
            print(f"ID: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nCourse: {row[3]}\nEmail: {row[4]}")

    def display_last(self):
        row = self.service.fetch_last()
        if row:
            print("\nLast Added Student:-")
            print(f"ID: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nCourse: {row[3]}\nEmail: {row[4]}")
        else:
            print("No records found")

    def update(self, s_id, name, age, course, email):
        if self.service.update_student(s_id, name, age, course, email):
            print(f"\nStudent ID {s_id} updated.")
        else:
            print("Update failed. ID not found.")

    def delete(self, s_id):
        if self.service.delete_student(s_id):
            print(f"\nStudent ID {s_id} deleted.")
        else:
            print("Deletion failed")