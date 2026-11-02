# 🏦 Bank Customer Segmentation & Churn Analysis

An end-to-end data analytics project focused on understanding customer behaviour, identifying customer segments, and analysing customer churn using Python, SQL, Power BI, and Streamlit.

## 📌 Project Overview

Customer churn is a major challenge for banking businesses. This project analyses customer data to identify patterns, understand customer segments, and explore factors associated with customer churn.

The project combines data cleaning, exploratory data analysis, machine learning, SQL analysis, and interactive dashboards to generate meaningful business insights.

**Note:** This project uses a synthetically generated dataset of 5,000 banking customers for educational and portfolio purposes. It does not contain real customer information.

## 🎯 Project Objectives

- Analyse customer demographics and banking behaviour.
- Identify customer segments using K-Means clustering.
- Understand customer churn patterns.
- Analyse churn across geography, age groups, and activity status.
- Build interactive dashboards for business insights.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas, NumPy | Data cleaning and manipulation |
| Matplotlib, Seaborn | Exploratory data analysis |
| Scikit-learn | K-Means clustering |
| SQL | Customer and churn analysis |
| SQLite | Database management |
| Power BI | Interactive business dashboard |
| Streamlit | Interactive analytics application |
| Plotly | Data visualisation |

## 📊 Project Features

### 1. Data Cleaning
- Removed duplicate customer records.
- Handled missing values.
- Prepared data for analysis and modelling.

### 2. Exploratory Data Analysis
- Analysed customer demographics.
- Explored account balances and product usage.
- Examined customer activity and churn patterns.

### 3. Customer Segmentation
- Applied K-Means clustering.
- Identified four customer segments.
- Analysed customer distribution across segments.

### 4. SQL Analysis
Performed analytical queries using:
- Aggregations and GROUP BY
- CASE statements
- Subqueries
- Common Table Expressions (CTEs)
- Window functions and RANK()

### 5. Power BI Dashboard
Created an interactive dashboard featuring:
- Total customers
- Churned customers
- Churn rate and retention rate
- Churn analysis by geography and age
- Customer segment distribution
- Customer activity analysis

### 6. Streamlit Dashboard
Developed an interactive application featuring:
- Geography and gender filters
- Age range filter
- Customer segment filter
- Activity status and credit card filters
- KPI metrics and interactive charts
- Customer details table
- Filtered customer data download

## 📁 Project Structure

```text
Bank-Customer-Segmentation-and-Churn-Analysis/
│
├── data/
├── notebooks/
├── sql/
├── src/
├── screenshots/
│
├── app.py
├── generate_data.py
├── load_sql.py
├── run_sql.py
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Spandanaaaaaa/Bank-Customer-Segmentation-and-Churn-Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Bank-Customer-Segmentation-and-Churn-Analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📈 Key Outcomes

- Analysed 5,000 synthetic banking customer records.
- Identified four customer segments using K-Means clustering.
- Explored customer churn and retention patterns.
- Created SQL-based analytical queries.
- Developed interactive Power BI and Streamlit dashboards.

## 👩‍💻 Author

**Spandana Gunda**

B.Tech Computer Science and Engineering

**Areas of Interest:** Data Analytics | Python | SQL | Power BI | Machine Learning

## ⭐ Acknowledgement

This project was developed as a hands-on portfolio project to demonstrate practical data analytics, SQL, machine learning, and dashboard development skills.
