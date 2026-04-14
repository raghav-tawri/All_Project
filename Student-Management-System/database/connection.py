# import sqlite3
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# def create_connection():
#     conn=None
#     try:
#         conn=sqlite3.connect('connection.db')
#         print("Connection successful")
#         return conn
#     except sqlite3.Error as e:
#         print(f"Error connecting to database: {e}")

# if __name__ == "__main__":
#     create_connection()


import sqlite3
import os

class DatabaseConnection:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Connection Error: {e}")
            return None

    def initialize_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()
        conn.close()