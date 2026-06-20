--DROP TABLE customer_churn;

-- Step1:- Create Tables and Load Dataset

CREATE TABLE customer_churn (

    customerid VARCHAR(50),
    gender VARCHAR(20),
    seniorcitizen VARCHAR(10),
    partner VARCHAR(10),
    dependents VARCHAR(10),
    tenure VARCHAR(20),
    phoneservice VARCHAR(20),
    multiplelines VARCHAR(30),
    internetservice VARCHAR(30),
    onlinesecurity VARCHAR(30),
    onlinebackup VARCHAR(30),
    deviceprotection VARCHAR(30),
    techsupport VARCHAR(30),
    streamingtv VARCHAR(30),
    streamingmovies VARCHAR(30),
    contract VARCHAR(30),
    paperlessbilling VARCHAR(10),
    paymentmethod VARCHAR(50),
    monthlycharges VARCHAR(30),
    totalcharges VARCHAR(30),
    churn VARCHAR(10)
);

-- Cheek our DataSet
select * from customer_churn;

-- Step 2:- Analysis and extracting meaning-full insights 

-- 1. Total Customers
SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- 2. Churn Distribution
SELECT churn, COUNT(*) AS customers
FROM customer_churn
GROUP BY churn;

-- 3. Overall Churn Rate
SELECT
ROUND(SUM(CASE WHEN churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS churn_rate
FROM customer_churn;

-- 4. Churn by Gender

SELECT
    gender,
    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        SUM(
            CASE
                WHEN churn = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customer_churn
GROUP BY gender;

-- 5. Churn by Contract (Most Important)
SELECT 
	contract,
	COUNT(*) AS total_customers,

	SUM(
        CASE
            WHEN churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        SUM(
            CASE
                WHEN churn = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS churn_rate

FROM customer_churn
GROUP BY contract
ORDER BY churn_rate DESC;

-- 6. Churn by Internet Service

SELECT
    internetservice,

    COUNT(*) customers,

    SUM(
        CASE
            WHEN churn='Yes' THEN 1
            ELSE 0
        END
    ) churned,

    ROUND(
        SUM(
            CASE
                WHEN churn='Yes' THEN 1
                ELSE 0
            END
        )*100.0/COUNT(*),
        2
    ) churn_rate

FROM customer_churn

GROUP BY internetservice

ORDER BY churn_rate DESC;


-- 7. Monthly Charges by Churn

SELECT
    churn,
    ROUND(AVG(monthlycharges::NUMERIC), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY churn;

-- 8. Payment Method vs Churn

SELECT PaymentMethod,
       COUNT(*) AS total_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn
GROUP BY PaymentMethod
;


-- 9. Senior Citizen vs Churn
SELECT SeniorCitizen,
       COUNT(*) AS total_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn
GROUP BY SeniorCitizen;

-- 10. Tenure Segmentation
SELECT
CASE
    WHEN tenure::INT <= 12 THEN '0-12 Months'
    WHEN tenure::INT <= 24 THEN '13-24 Months'
    WHEN tenure::INT <= 48 THEN '25-48 Months'
    ELSE '49+ Months'
END AS tenure_group,
COUNT(*) AS customers
FROM customer_churn
GROUP BY tenure_group;



