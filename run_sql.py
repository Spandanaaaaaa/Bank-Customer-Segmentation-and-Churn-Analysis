
import sqlite3
import pandas as pd

# Connect to the database
connection = sqlite3.connect(
    r"C:\Users\spandana\Downloads\Bank_Customer_Analytics\data\bank_customers.db"
)

# Read the SQL file using its exact path
with open(
    r"C:\Users\spandana\Downloads\Bank_Customer_Analytics\sql\analysis_queries.sql",
    "r"
) as file:
    sql_script = file.read()

print("SQL file loaded!")
print("SQL file length:", len(sql_script))

# Split SQL statements
queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]

print("Total queries found:", len(queries))

# Execute each query
for i, query in enumerate(queries, start=1):
    print("\n" + "=" * 50)
    print(f"QUERY {i}")
    print("=" * 50)

    try:
        result = pd.read_sql_query(query, connection)
        print(result.to_string(index=False))
    except Exception as error:
        print("Error:", error)

connection.close()

print("\nSQL analysis completed!")
