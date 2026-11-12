import pandas as pd
students = [
    ["24/14586", "Computer Science", 300, 92, 85],
    ["25/15766", "Accounting", 200, 78, 73],
    ["26/12357", "Economics", 100, 85, 88],
    ["24/12345", "Mass Communication", 300, 69, 64],
    ["23/12346", "Business Administration", 400, 95, 91],
    ["25/15678", "Computer Science", 200, 81, 79],
    ["26/15906", "Economics", 100, 74, 70],
    ["25/12975", "Mass Communication", 200, 88, 82],
    ["24/12899", "Accounting", 300, 90, 86],
    ["23/13566", "Computer Science", 400, 97, 93],
    ["25/13555", "Economics", 200, 65, 68],
    ["26/17790", "Business Administration", 100, 83, 76],
    ["24/19990", "Computer Science", 300, 76, 80],
    ["23/13579", "Accounting", 400, 91, 89],
    ["26/24680", "Mass Communication", 100, 72, 75],
    ["24/17902", "Economics", 300, 86, 84],
    ["25/14677", "Business Administration", 200, 79, 77],
    ["26/23456", "Computer Science", 100, 68, 72],
    ["25/14478", "Accounting", 200, 93, 90],
    ["23/10007", "Mass Communication", 400, 89, 87]
]

columns = [
    "Matriculation Number",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

df = pd.DataFrame(students, columns=columns)
print(df)

df.to_csv("student_dataset.csv", index=False)

print("Dataset saved successfully!")
