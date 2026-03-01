import psycopg2
def connect():
    return psycopg2.connect(
        host="localhost",
        database="student_db",
        user="your_username",
        password="your_password",
        port="5433")

