import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def load_and_clean_data(file_path="data/bank_customers.csv"):
    df = pd.read_csv(file_path)

    # Remove duplicate customers
    df = df.drop_duplicates(subset="CustomerID")

    # Handle missing values
    numeric_columns = df.select_dtypes(include="number").columns
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    # Create customer segments using K-Means
    features = ["Age", "Balance", "EstimatedSalary", "Tenure"]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])

    model = KMeans(n_clusters=4, random_state=42, n_init=10)
    df["CustomerSegment"] = model.fit_predict(scaled_data)

    return df


if __name__ == "__main__":
    cleaned_df = load_and_clean_data()
    cleaned_df.to_csv("data/cleaned_bank_customers.csv", index=False)

    print("Data cleaning completed!")
    print(cleaned_df.head())
    print("\nCustomer segments:")
    print(cleaned_df["CustomerSegment"].value_counts())