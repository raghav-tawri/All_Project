create database joinpractice;

use joinpractice;


CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);



INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Sales');



INSERT INTO employees VALUES
(101, 'Alice', 70000, 1, NULL),
(102, 'Bob', 60000, 2, 101),
(103, 'Charlie', 55000, 2, 102),
(104, 'David', 50000, 3, 101),
(105, 'Eva', 45000, 4, 104),
(106, 'Frank', 75000, 1, 101),
(107, 'Grace', 80000, 2, 102),
(108, 'Helen', 62000, 3, 104),
(109, 'Ian', 47000, 4, 105),
(110, 'Jack', 53000, 2, 102),
(111, 'Kevin', 49000, 3, 104),
(112, 'Laura', 72000, 1, 101),
(113, 'Mike', 58000, 4, 105),
(114, 'Nina', 61000, 2, 107),
(115, 'Oscar', 52000, NULL, 101);

SELECT * FROM departments;

SELECT * FROM employees;

-- Display employee names along with their department names.
SELECT e.emp_name, d.dept_name
FROM employees e INNER JOIN departments d
ON e.dept_id = d.dept_id;

-- Display all employees and their department names, including employees without departments.
SELECT e.emp_name,d.dept_name FROM employees e LEFT JOIN departments d
ON e.dept_id = d.dept_id;

-- Find the number of employees in each department.
SELECT d.dept_name,COUNT(e.emp_id) AS total_employees FROM departments d LEFT JOIN employees e
ON e.dept_id=d.dept_id GROUP BY d.dept_name;


-- Display all departments and the total salary paid in each department.
SELECT d.dept_name,SUM(e.salary) AS total_salary FROM employees e LEFT JOIN departments d 
ON d.dept_id=e.dept_id GROUP BY d.dept_name;

-- Find how many employees report to each manager.
SELECT m.emp_name AS manager,COUNT(e.emp_id) AS team_size FROM employees e INNER JOIN employees m 
ON e.manager_id = m.emp_id GROUP BY m.emp_name ORDER BY team_size DESC;


-- Display average salary department-wise where average salary is greater than 60000.
SELECT d.dept_name,ROUND(AVG(e.salary), 2) AS avg_salary FROM departments d INNER JOIN employees e 
ON d.dept_id = e.dept_id GROUP BY d.dept_name HAVING AVG(e.salary) > 60000;