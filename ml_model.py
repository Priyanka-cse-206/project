import mysql.connector
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# 1. Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyanka@123",
    database="student_performance"
)

cursor = connection.cursor()


# 2. Get data from MySQL
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


# 3. Convert data into NumPy array
data = np.array(data)

X = data[:, 0:5]
y = data[:, 5]


# 4. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create Decision Tree
model = DecisionTreeClassifier(random_state=42)


# 6. Train model
model.fit(X_train, y_train)


# 7. Test model
y_pred = model.predict(X_test)


# 8. Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("Model Accuracy (%):", accuracy * 100)


# 9. Predict a new student

new_student = np.array([
    [55, 38, 60, 42, 2]
])

prediction = model.predict(new_student)


if prediction[0] == 1:
    print("Prediction: AT RISK")
else:
    print("Prediction: NOT AT RISK")


# 10. Close database
cursor.close()
connection.close()