# from Student-Management-System.database.connection import create_connection
import sys
import os
# from models.student import Student
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.connection import DatabaseConnection

# class StudentServices:
#     def __init__(self):
#         self.conn=create_connection()

#     def insert_student(self, name, age, course, email):
#         cursor = self.conn.execute("INSERT INTO students (name,age,course,email) VALUES (?,?,?,?)", (name, age, course, email))
#         self.conn.commit()
#         # self.conn.close()

#     def get_all_students(self):
#         cursor = self.conn.execute("SELECT * FROM students")
#         students = cursor.fetchall()
#         self.conn.close()
#         return students

#     def update_student(self, name, age, course, email):
#         self.conn.execute("UPDATE students SET name=?,age=?,course=?,email=? WHERE id=?", (name, age, course, email))
#         self.conn.commit()
#         self.conn.close()

#     def delete_student(self, id):
#         self.conn.execute("DELETE FROM students WHERE id=?", (id,))
#         self.conn.commit()
#         self.conn.close()

#     def create_table(self):
#         self.conn.execute('''CREATE TABLE IF NOT EXISTS students
#                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                      name TEXT NOT NULL,
#                  age INTEGER NOT NULL,
#                  course TEXT NOT NULL,
#                  email TEXT NOT NULL)''')
#         print("Table created successfully")
#         # self.conn.close()
# if __name__ == "__main__":    
#     student_services = StudentServices()
#     student_services.create_table()
#     # student_services.insert_student(Student.name, Student.age, Student.course, Student.email)
#     student_services.insert_student("John Doe", 20, "Computer Science", "john@gmail.com")
#     students = student_services.get_all_students()
#     print(students)


# from database.connection import DatabaseConnection

class StudentService:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.initialize_db()

    def insert_student(self, student_id, name, age, course, email):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", 
                           (student_id, name, age, course, email))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting record: {e}")
            return False
        finally:
            conn.close()

    def fetch_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        conn.close()
        return data

    def fetch_last(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY ROWID DESC LIMIT 1")
        data = cursor.fetchone()
        conn.close()
        return data

    def update_student(self, student_id, name, age, course, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute('''UPDATE students SET name=?, age=?, course=?, email=? 
                          WHERE student_id=?''', (name, age, course, email, student_id))
        conn.commit()
        updated = cursor.rowcount
        conn.close()
        return updated > 0

    def delete_student(self, student_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()
        return deleted > 0