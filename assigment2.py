
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Student": ["Abel", "Sara", "Dawit", "Hana", "Meron",
                "Yonas", "Liya", "Robel", "Mimi", "Samuel"],
    "Study_Hours": [2, 5, 3, 7, 6, 1, 8, 4, 5, 2],
    "Attendance": [60, 90, 70, 95, 85, 50, 98, 75, 88, 65],
    "Score": [45, 85, 60, 95, 82, 35, 98, 68, 80, 50]
}

df = pd.DataFrame(data)

# Set a consistent chart style
sns.set_theme(style="whitegrid")

# 2. Bar plot: Compare each student's score
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Student", y="Score")
plt.title("Comparison of Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Scatter plot: Study hours versus scores
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Score",
    s=100
)
plt.title("Relationship Between Study Hours and Scores")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

# 4. Histogram: Distribution of scores
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="Score", bins=6, edgecolor="black")
plt.title("Distribution of Student Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()


numeric_df = df[["Study_Hours", "Attendance", "Score"]]
correlation = numeric_df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)
plt.title("Correlation Heatmap of Student Data")
plt.tight_layout()
plt.show()


