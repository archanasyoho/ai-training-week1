
import pandas as pd
import matplotlib.pyplot as plt

# Read employee CSV file
df = pd.read_csv("employees.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check required columns
required_columns = ["id", "salary", "department"]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# --------------------------------
# 1. BAR CHART - Average Salary
# --------------------------------

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(
    avg_salary.index,
    avg_salary.values,
    color="skyblue"
)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()


# --------------------------------
# 2. HISTOGRAM - Salary Distribution
# --------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["salary"].dropna(),
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()


# --------------------------------
# 3. SCATTER PLOT - ID vs Salary
# --------------------------------

plt.figure(figsize=(8, 5))

for department in df["department"].dropna().unique():

    dept_data = df[df["department"] == department]

    plt.scatter(
        dept_data["id"],
        dept_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()


# --------------------------------
# 4. LINE CHART - Monthly Sales
# --------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="-",
    color="green",
    label="Monthly Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

print("All 4 charts created successfully!")

print("1. bar_chart.png")
print("2. histogram.png")
print("3. scatter_plot.png")
print("4. line_chart.png")
