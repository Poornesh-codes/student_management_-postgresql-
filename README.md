# student_management_-postgresql-
# Student Management System (Python + PostgreSQL)

## 📌 Description
A CLI-based Student Management System built using Python and PostgreSQL.
It supports basic CRUD operations.

## 🚀 Features
- Add Student
- View Students
- Delete Student
- PostgreSQL Integration

## 🛠 Tech Stack
- Python
- PostgreSQL
- psycopg2

## 🗄 Database Schema

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK(age > 0),
    department VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

## ▶ How To Run

1. Create database:
   CREATE DATABASE student_db;
2. Install dependencies:
    pip install -r requirements.txt

3. Run;
    python main.py
---

<img width="897" height="827" alt="Screenshot 2026-03-01 174143" src="https://github.com/user-attachments/assets/0ccd8017-fd09-4550-b9d4-09e36d2ad16a" />
<img width="932" height="585" alt="Screenshot 2026-03-01 174209" src="https://github.com/user-attachments/assets/c9e01d61-9604-4dc9-8857-b85f96d249dd" />

---

