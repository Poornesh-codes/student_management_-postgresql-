from db import connect
def add_student():
    conn = connect()
    cursor = conn.cursor()
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    dept = input("Enter student department: ")
    email= input("Enter student email: ")

    cursor.execute("INSERT INTO students (name, age, department, email) VALUES (%s, %s, %s, %s)", (name, age, dept, email))
    conn.commit()
    conn.close()
    print("Student added successfully!")
def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)
    conn.close()
def delete_student():
    conn = connect()
    cursor = conn.cursor()
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")