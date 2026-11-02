import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

df = pd.DataFrame({
    "CustomerID": range(10001, 10001 + n),
    "Age": np.random.randint(18, 75, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Geography": np.random.choice(
        ["France", "Germany", "Spain"], n
    ),
    "Tenure": np.random.randint(0, 11, n),
    "Balance": np.random.uniform(0, 250000, n).round(2),
    "NumOfProducts": np.random.choice([1, 2, 3, 4], n),
    "HasCrCard": np.random.choice([0, 1], n),
    "IsActiveMember": np.random.choice([0, 1], n),
    "EstimatedSalary": np.random.uniform(10000, 200000, n).round(2)
})

churn_probability = (
    0.08
    + (df["Age"] > 50) * 0.12
    + (df["IsActiveMember"] == 0) * 0.15
    + (df["NumOfProducts"] == 1) * 0.08
    + (df["Geography"] == "Germany") * 0.05
)

churn_probability = np.clip(churn_probability, 0.02, 0.75)

df["Exited"] = np.random.binomial(1, churn_probability)

df["BalanceCategory"] = pd.cut(
    df["Balance"],
    bins=[-1, 50000, 150000, float("inf")],
    labels=["Low", "Medium", "High"]
)

df.to_csv("data/bank_customers.csv", index=False)

print("Dataset created successfully!")
print("Total rows:", len(df))
print(df.head())