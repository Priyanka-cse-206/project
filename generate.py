import numpy as np
import mysql.connector

# -----------------------------
# 1. Generate student data
# -----------------------------

np.random.seed(42)

n = 100

attendance = np.random.randint(40, 101, n)
previous_marks = np.random.randint(30, 101, n)
assignment_marks = np.random.randint(30, 101, n)
internal_marks = np.random.randint(30, 101, n)
study_hours = np.round(np.random.uniform(1, 8, n), 1)

# 0 = Not At Risk
# 1 = At Risk
risk_status = (
    (attendance < 60) |
    (previous_marks < 40) |
    (internal_marks < 40)
).astype(int)


# -----------------------------
# 2. Connect to MySQL
# -----------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyanka@123",
    database="student_performance"
)

cursor = connection.cursor()

print("Database connected successfully!")


# -----------------------------
# 3. Insert student data
# -----------------------------

for i in range(n):

    student_id = i + 1
    name = f"Student_{student_id}"
    department = "CSE"
    year = 3

    student_query = """
    INSERT INTO students
    (student_id, name, department, year)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        student_query,
        (student_id, name, department, year)
    )

    performance_query = """
    INSERT INTO performance
    (student_id, attendance, previous_marks,
     assignment_marks, internal_marks,
     study_hours, risk_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        performance_query,
        (
            student_id,
            float(attendance[i]),
            float(previous_marks[i]),
            float(assignment_marks[i]),
            float(internal_marks[i]),
            float(study_hours[i]),
            int(risk_status[i])
        )
    )


# -----------------------------
# 4. Save changes
# -----------------------------

connection.commit()

print("100 student records inserted successfully!")

cursor.close()
connection.close()

print("Database connection closed.")