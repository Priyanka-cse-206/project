import mysql.connector
import numpy as np

# Connect to database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyanka@123",
    database="student_performance"
)

cursor = connection.cursor()

# Get student performance data
query = """
SELECT
    s.student_id,
    s.name,
    p.attendance,
    p.previous_marks,
    p.assignment_marks,
    p.internal_marks,
    p.study_hours,
    p.risk_status
FROM students s
JOIN performance p
ON s.student_id = p.student_id
"""

cursor.execute(query)

# Get data from MySQL
data = cursor.fetchall()

# Display first 10 records
print("--- FIRST 10 STUDENTS ---")

for row in data[:10]:
    print(row)

print("Total records:", len(data))


# Convert database data into NumPy arrays

attendance = np.array([row[2] for row in data])
previous_marks = np.array([row[3] for row in data])
assignment_marks = np.array([row[4] for row in data])
internal_marks = np.array([row[5] for row in data])
study_hours = np.array([row[6] for row in data])
risk_status = np.array([row[7] for row in data])


# Calculate averages

print("\n--- STUDENT PERFORMANCE ANALYSIS ---")

print("Average Attendance:", np.mean(attendance))

print("Average Previous Marks:", np.mean(previous_marks))

print("Average Assignment Marks:", np.mean(assignment_marks))

print("Average Internal Marks:", np.mean(internal_marks))

print("Average Study Hours:", np.mean(study_hours))


# Count risk status

at_risk = np.sum(risk_status == 1)
not_at_risk = np.sum(risk_status == 0)

print("\nStudents At Risk:", at_risk)

print("Students Not At Risk:", not_at_risk)


# Close connection

cursor.close()
connection.close()

print("\nDatabase connection closed.")