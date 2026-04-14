# 🎓 Advanced Student Management System (SMS)

A professional, modularized Student Management System built with **Python**, **SQLite**, and **Object-Oriented Programming (OOP)**. This project demonstrates a clean separation of concerns using a layered architecture (Model-Service-Database).

---

## 📂 Project Architecture

The system is divided into functional modules to ensure scalability and maintainability:

```text
student_management/
├── database/
│   └── connection.py       # Layer 1: Database connectivity & Schema setup
├── service/
│   └── student_services.py  # Layer 2: Data Access Object (DAO) / CRUD Logic
├── model/
│   └── student.py           # Layer 3: Business Logic & UI Formatting
├── main.py                 # Execution Hub: CLI Menu Controller
├── README.md               # Documentation
└── database.db             # SQLite Storage (Auto-generated)
🛠️ FeaturesObject-Oriented Design: Encapsulated logic across classes and modules.Persistent Storage: SQLite database ensures data remains after the program closes.Full CRUD Support: - Create: Insert new student records with unique constraints.Read: Fetch all records or the most recent entry.Update: Modify existing details based on Student ID.Delete: Remove records safely from the database.Clean CLI Interface: Intuitive menu-driven interaction.🚀 Execution InstructionsFollow these steps to set up and run the application on your local machine.1. PrerequisitesPython 3.8+ installed.No external libraries are required (uses standard built-in sqlite3 library).2. SetupClone or download the project files into a single directory. Ensure the folder structure remains intact:Bash# Example folder structure check
ls -R
3. Running the SystemFrom your terminal or command prompt, navigate to the root directory (student_management) and execute the following command:Bashpython main.py
4. Usage FlowInitialize: On the first run, the system will automatically create database.db.Navigation: Enter numbers 1-6 to select your desired operation.Data Entry: Follow the on-screen prompts to input Student ID, Name, Age, Course, and Email.📑 Module DescriptionsFilePurposeconnection.pyInitializes the sqlite3 connection and ensures the students table exists with the correct schema.student_services.pyContains the StudentService class. It maps Python methods to SQL queries (INSERT, SELECT, UPDATE, DELETE).student.pyContains the Student model. It handles user-facing tasks like formatting output and passing data to the service layer.main.pyThe controller that manages the program loop and maps user input to model functions.🛡️ Database SchemaThe system manages a table named students with the following attributes:student_id (INTEGER, Primary Key)name (TEXT)age (INTEGER)course (TEXT)email (TEXT, Unique)📝 LicenseThis project is for educational purposes and is open for modification and distribution.