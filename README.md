
# 🎓 AI Student Performance Analyzer

An **AI-based Student Performance Analyzer and Risk Prediction System** that analyzes student academic data and predicts whether a student is **At Risk** or **Not At Risk** using Machine Learning.

The project uses **Python, NumPy, Pandas, MySQL, and Scikit-learn** to generate, store, analyze, and predict student performance.

## 🚀 Features

* 📊 Generate student performance data
* 🗄️ Store student data using MySQL
* 🔍 Analyze academic performance
* 🤖 Predict student academic risk using Machine Learning
* 📈 Use attendance, previous marks, assignment marks, internal marks, and study hours as performance factors
* 🌳 Decision Tree classification model
* 🧹 Data processing and analysis using Python libraries

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **MySQL**
* **Scikit-learn**
* **Basic ML**
* **VS Code**

## 📂 Project Structure

```text
AI_Student_Performance/
│
├── database.py
├── generate.py
├── analysis.py
├── ml_model.py
├── main.py
├── student_performance.ipynb
├── requirements.txt
└── README.md
```

## 🔄 Project Workflow

```text
Student Data
     ↓
Data Generation
     ↓
MySQL Database
     ↓
Data Extraction & Analysis
     ↓
Data Preprocessing
     ↓
Machine Learning Model
     ↓
Risk Prediction
     ↓
At Risk / Not At Risk
```

## 📊 Dataset Features

The system considers different factors related to student performance:

| Feature          | Description                   |
| ---------------- | ----------------------------- |
| Attendance       | Student attendance percentage |
| Previous Marks   | Marks obtained previously     |
| Assignment Marks | Performance in assignments    |
| Internal Marks   | Internal examination marks    |
| Study Hours      | Average study hours           |

### Risk Prediction

A student is considered **At Risk** when performance indicators fall below predefined thresholds, such as:

* Attendance < 60%
* Previous Marks < 40
* Internal Marks < 40

Otherwise, the student is classified as **Not At Risk**.

## 🤖 Machine Learning Model

The project uses a **Decision Tree Classifier** from Scikit-learn.

### Input Features

```text
Attendance
Previous Marks
Assignment Marks
Internal Marks
Study Hours
```

### Output

```text
0 → Not At Risk
1 → At Risk
```

The dataset is divided into training and testing sets using `train_test_split()` before training the model.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd AI_Student_Performance
```

### 3. Install required libraries

```bash
pip install numpy pandas scikit-learn mysql-connector-python
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

## 🗄️ MySQL Setup

1. Open **MySQL Workbench**.
2. Create the required database.
3. Configure the MySQL username, password, and database name in `database.py`.
4. Run the database setup code.
5. Generate or insert student performance data.

Example:

```sql
CREATE DATABASE student_performance;
```

## ▶️ Running the Project

Run the Python files according to the project workflow:

```bash
python database.py
python generate.py
python analysis.py
python ml_model.py
python main.py
```

If using Jupyter Notebook, open:

```text
student_performance.ipynb
```

and run the cells sequentially.

## 📌 Future Improvements

* Create a graphical user interface
* Add student performance visualizations
* Improve model accuracy
* Compare multiple Machine Learning algorithms
* Add personalized recommendations for students
* Predict future academic performance
* Add login and student management functionality
* Deploy the application as a web application

## 🎯 Objective

The main objective of this project is to use **Data Science and Machine Learning** to identify students who may be academically at risk and help educators take early action to improve their performance.

## 👩‍💻 Author

**Priyanka**

B.Tech CSE Student
Interested in **AI/ML, Data Science, Python & DSA**
