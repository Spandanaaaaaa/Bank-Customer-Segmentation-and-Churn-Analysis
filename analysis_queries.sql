-- 1. Total number of customers
SELECT COUNT(*) AS total_customers
FROM bank_customers;

-- 2. Overall churn analysis
SELECT
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_customers,
    ROUND(100.0 * SUM(Exited) / COUNT(*), 2) AS churn_rate
FROM bank_customers;

-- 3. Churn by geography
SELECT
    Geography,
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_customers,
    ROUND(100.0 * SUM(Exited) / COUNT(*), 2) AS churn_rate
FROM bank_customers
GROUP BY Geography
ORDER BY churn_rate DESC;

-- 4. Customer distribution by age group
SELECT
    CASE
        WHEN Age < 30 THEN 'Under 30'
        WHEN Age BETWEEN 30 AND 45 THEN '30-45'
        WHEN Age BETWEEN 46 AND 60 THEN '46-60'
        ELSE 'Above 60'
    END AS age_group,
    COUNT(*) AS customer_count
FROM bank_customers
GROUP BY age_group
ORDER BY customer_count DESC;

-- 5. Average balance by churn status
SELECT
    Exited,
    ROUND(AVG(Balance), 2) AS average_balance
FROM bank_customers
GROUP BY Exited;

-- 6. CTE: churn rate by activity
WITH activity_summary AS (
    SELECT
        IsActiveMember,
        COUNT(*) AS total_customers,
        SUM(Exited) AS churned_customers
    FROM bank_customers
    GROUP BY IsActiveMember
)
SELECT
    IsActiveMember,
    total_customers,
    churned_customers,
    ROUND(100.0 * churned_customers / total_customers, 2) AS churn_rate
FROM activity_summary;

-- 7. Window function: rank customers by balance
SELECT
    CustomerID,
    Geography,
    Balance,
    RANK() OVER (ORDER BY Balance DESC) AS balance_rank
FROM bank_customers;

-- 8. Subquery: customers with balance above average
SELECT CustomerID, Age, Geography, Balance
FROM bank_customers
WHERE Balance > (
    SELECT AVG(Balance)
    FROM bank_customers
);
-- 9. Churn rate by customer segment
SELECT
    CustomerSegment,
    COUNT(*) AS Total_Customers,
    SUM(Exited) AS Churned_Customers,
    ROUND(AVG(Exited) * 100, 2) AS Churn_Rate
FROM bank_customers
GROUP BY CustomerSegment
ORDER BY Churn_Rate DESC;


-- 10. Active and inactive customer analysis
SELECT
    IsActiveMember,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Exited) * 100, 2) AS Churn_Rate
FROM bank_customers
GROUP BY IsActiveMember;


-- 11. Customers with multiple products
SELECT
    NumOfProducts,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Exited) * 100, 2) AS Churn_Rate
FROM bank_customers
GROUP BY NumOfProducts
ORDER BY NumOfProducts;


-- 12. Top 10 customers by account balance
SELECT
    CustomerID,
    Geography,
    Age,
    Balance
FROM bank_customers
ORDER BY Balance DESC
LIMIT 10;
