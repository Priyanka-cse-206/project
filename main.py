import mysql.connector
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# ==========================================
# CONNECT TO DATABASE
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyanka@123",
    database="student_performance"
)

cursor = connection.cursor()

print("\n========================================")
print("   AI STUDENT PERFORMANCE ANALYSIS")
print("========================================")


# ==========================================
# GET DATA FROM DATABASE
# ==========================================

query = """
SELECT
    attendance,
    previous_marks,
    assignment_marks,
    internal_marks,
    study_hours,
    risk_status
FROM performance
"""

cursor.execute(query)

data = cursor.fetchall()

data = np.array(data)


# ==========================================
# PREPARE DATA FOR ML
# ==========================================

X = data[:, 0:5]
y = data[:, 5]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# TRAIN ML MODEL
# ==========================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n----------------------------------------")
    print("1. View Performance Analysis")
    print("2. Predict Student Risk")
    print("3. Exit")
    print("----------------------------------------")

    choice = input("Enter your choice: ")


    # ======================================
    # OPTION 1 — PERFORMANCE ANALYSIS
    # ======================================

    if choice == "1":

        attendance = data[:, 0]
        previous_marks = data[:, 1]
        assignment_marks = data[:, 2]
        internal_marks = data[:, 3]
        study_hours = data[:, 4]
        risk_status = data[:, 5]

        print("\n--- PERFORMANCE ANALYSIS ---")

        print(
            "Average Attendance:",
            np.mean(attendance)
        )

        print(
            "Average Previous Marks:",
            np.mean(previous_marks)
        )

        print(
            "Average Assignment Marks:",
            np.mean(assignment_marks)
        )

        print(
            "Average Internal Marks:",
            np.mean(internal_marks)
        )

        print(
            "Average Study Hours:",
            np.mean(study_hours)
        )

        at_risk = np.sum(risk_status == 1)

        not_at_risk = np.sum(risk_status == 0)

        print("\nStudents At Risk:", at_risk)

        print(
            "Students Not At Risk:",
            not_at_risk
        )


    # ======================================
    # OPTION 2 — PREDICT STUDENT RISK
    # ======================================

    elif choice == "2":

        print("\n--- NEW STUDENT PREDICTION ---")

        attendance = float(
            input("Enter attendance percentage: ")
        )

        previous_marks = float(
            input("Enter previous marks: ")
        )

        assignment_marks = float(
            input("Enter assignment marks: ")
        )

        internal_marks = float(
            input("Enter internal marks: ")
        )

        study_hours = float(
            input("Enter study hours per day: ")
        )

        new_student = np.array([
            [
                attendance,
                previous_marks,
                assignment_marks,
                internal_marks,
                study_hours
            ]
        ])

        prediction = model.predict(new_student)

        if prediction[0] == 1:

            print("\n⚠️ Prediction: AT RISK")

        else:

            print("\n✅ Prediction: NOT AT RISK")


    # ======================================
    # OPTION 3 — EXIT
    # ======================================

    elif choice == "3":

        print("\nThank you for using the system!")

        break


    else:

        print("\n❌ Invalid choice. Please enter 1, 2 or 3.")


# ==========================================
# CLOSE DATABASE
# ==========================================

cursor.close()

connection.close()

print("Database connection closed.")