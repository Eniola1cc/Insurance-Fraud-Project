-- Insurance Fraud Risk Prioritisation System
-- SQL Analysis Queries

-- 1. Total number of claims
SELECT COUNT(*) AS total_claims
FROM insurance_claims;

-- 2. Fraud vs non-fraud distribution
SELECT 
    fraud_reported,
    COUNT(*) AS claim_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM insurance_claims), 2) AS percentage
FROM insurance_claims
GROUP BY fraud_reported;

-- 3. Fraud rate by incident type
SELECT 
    incident_type,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) AS fraud_cases,
    ROUND(SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fraud_rate
FROM insurance_claims
GROUP BY incident_type
ORDER BY fraud_rate DESC;

-- 4. Average claim amount by fraud status
SELECT 
    fraud_reported,
    ROUND(AVG(total_claim_amount), 2) AS average_claim_amount
FROM insurance_claims
GROUP BY fraud_reported;

-- 5. Fraud rate by police report availability
SELECT 
    police_report_available,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) AS fraud_cases,
    ROUND(SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fraud_rate
FROM insurance_claims
GROUP BY police_report_available
ORDER BY fraud_rate DESC;