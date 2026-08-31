import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyanka@123"
    database="student_performance"
)

print("Database connected successfully!")