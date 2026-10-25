import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Abel", "Sara", "Dawit", "Hana", "Meron",
                "Yonas", "Liya", "Robel", "Mimi", "Samuel"],
    "Study_Hours": [2, 5, 3, 7, 6, 1, 8, 4, 5, 2],
    "Attendance": [60, 90, 70, 95, 85, 50, 98, 75, 88, 65],
    "Score": [45, 85, 60, 95, 82, 35, 98, 68, 80, 50]
}

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(10, 6))

plt.bar(df["Student"], df["Score"], color="skyblue",
        edgecolor="black")

plt.title("Student Scores Comparison")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.show()