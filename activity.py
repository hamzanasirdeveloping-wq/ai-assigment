import pandas as pd
df = pd.read_csv("students.csv")
df.head()
df.shape
df.columns
df.dtypes
df.info()
# Display Name and Score
print(df[["Name", "Score"]])

# Students scoring above 80
print(df[df["Score"] > 80])

# Students in IT
print(df[df["Department"] == "IT"])

# Students scoring below 50
print(df[df["Score"] < 50])


# 4. Find Data Problems

# Find missing values
print("Missing values:")
print(df.isnull().sum())

# Find duplicate rows
print("\nDuplicate rows:")
print(df[df.duplicated()])

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Find the invalid age value

print(df[df["Age"] == "twenty"])

# Find the invalid score

print(df[df["Score"] > 100])

# Convert Age to a numeric type
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Handle the missing Age using the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Handle the missing Score using the median
df["Score"] = df["Score"].fillna(df["Score"].median())

# Remove duplicate rows
df = df.drop_duplicates()


# Fix the invalid score
df.loc[df["Score"] > 100, "Score"] = 100

# Display the corrected score
print(df[df["Name"] == "Marta"])

print(df)

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
