import sqlite3
import pandas as pd

df = pd.read_csv("data/segmented_bank_customers.csv")

connection = sqlite3.connect("data/bank_customers.db")

df.to_sql(
    "bank_customers",
    connection,
    if_exists="replace",
    index=False
)

print("Segmented data loaded into SQLite successfully!")
print("Total records:", len(df))

connection.close()