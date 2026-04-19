# Exploratory Data Analysis (EDA) – Insurance Fraud Detection

## 1. Overview

This analysis explores patterns and relationships within the insurance claims dataset to identify potential indicators of fraudulent activity. The goal is to understand key variables that can help prioritise high-risk claims for investigation.

---

## 2. Dataset Summary

- Total Records: 1,000
- Total Features: 40 (before cleaning)
- Target Variable: `fraud_reported`

---

## 3. Fraud Distribution

Fraudulent claims account for approximately **24.7%** of the dataset, while non-fraudulent claims make up **75.3%**.

### Key Insight:
This indicates a **class imbalance**, where fraud cases are the minority. Any predictive model must be designed to effectively detect fraud without being biased toward non-fraud cases.

---

## 4. Claim Amount Analysis

An analysis of claim amounts shows:

- Average Non-Fraud Claim: ~50,288  
- Average Fraud Claim: ~60,302  

### Key Insight:
Fraudulent claims tend to have **higher monetary value**, suggesting that fraudsters are more likely to inflate claim amounts for financial gain. This makes claim amount a strong predictive feature.

---

## 5. Claim Amount Distribution (Boxplot)

The distribution of claim amounts reveals:

- Fraudulent claims have **greater variability**
- Presence of **extreme values (outliers)**
- Some unusually low fraud claims (potential anomalies)

### Key Insight:
Fraudulent behaviour is less consistent and more variable, indicating that **unusual patterns in claim values** may signal fraud.

---

## 6. Incident Type Analysis

Fraud occurrence varies significantly by incident type:

- **Single Vehicle Collision** → High fraud cases  
- **Multi-Vehicle Collision** → High fraud cases  
- **Parked Car** → Low fraud cases  
- **Vehicle Theft** → Low fraud cases  

### Key Insight:
More complex incidents (involving multiple vehicles or scenarios) show higher fraud rates, likely due to increased opportunity for manipulation.

---

## 7. Police Report Availability

Analysis of police report availability shows:

- Missing or unknown reports (`?`) → Highest fraud occurrence  
- No police report → High fraud occurrence  
- Police report available → Lowest fraud occurrence  

### Key Insight:
Lack of official documentation is a **strong indicator of potential fraud**. Claims without police verification should be prioritised for investigation.

---

## 8. Customer Age Analysis

- Average Age (Fraud): ~39.1  
- Average Age (Non-Fraud): ~38.8  

### Key Insight:
There is **no significant relationship** between age and fraud. Age is unlikely to be a strong predictive feature.

---

## 9. Number of Vehicles Involved

- Fraud: ~1.93 vehicles  
- Non-Fraud: ~1.80 vehicles  

### Key Insight:
Fraudulent claims tend to involve slightly more vehicles, supporting the idea that **complex incidents increase fraud risk**.

---

## 10. Missing Data Analysis

Key observations:

- `_c39` column contains 100% missing values → removed  
- `authorities_contacted` contains missing values  

### Key Insight:
Missing data itself may carry meaning (e.g., missing reports), and should be handled carefully during modeling.

---

## 11. Key Takeaways

The following variables show strong potential for fraud detection:

- Total Claim Amount  
- Incident Type  
- Police Report Availability  
- Number of Vehicles Involved  

Variables with weak predictive power:

- Age  

---

## 12. Conclusion

The EDA reveals clear behavioural and transactional patterns associated with fraudulent claims. These insights will guide feature engineering and model development, ensuring that the final system effectively prioritises high-risk claims for investigation.