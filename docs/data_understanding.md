# Data Understanding – Insurance Fraud Detection

## 1. Dataset Overview

The dataset consists of 1,000 insurance claims with 40 features capturing customer details, policy information, and incident characteristics.

The target variable is `fraud_reported`, which indicates whether a claim is fraudulent (1) or not (0).

---

## 2. Fraud Distribution

Fraudulent claims account for approximately **24.7%** of the dataset, while non-fraudulent claims make up **75.3%**.

### Key Insight:
This indicates a **class imbalance problem**, where fraud cases are significantly fewer than non-fraud cases. This must be considered during model development.

---

## 3. Key Variables

Important variables identified during exploration include:

- `total_claim_amount` → financial value of claims  
- `incident_type` → type of accident  
- `policy_annual_premium` → cost of policy  
- `police_report_available` → documentation availability  
- `number_of_vehicles_involved` → accident complexity  

---

## 4. Missing Data Issues

- `_c39` column contained 100% missing values and was removed  
- `authorities_contacted` contains missing values  
- Some categorical fields originally contained `"?"`, which were converted to null values  

### Key Insight:
Missing values may carry meaning (e.g., missing reports) and can be useful indicators of fraud.

---

## 5. Early Fraud Patterns

Initial analysis revealed several patterns:

- Fraudulent claims tend to have **higher claim amounts**
- Fraud is more common in **complex incidents** (multi-vehicle collisions)
- Claims without police reports show **higher fraud likelihood**
- Fraudulent claims show **higher variability and outliers**
- Customer age shows **little to no relationship** with fraud

---

## 6. Engineered Features

To improve fraud detection, new features were created:

- `policy_duration_days`  
  → Measures time between policy start and incident  

- `claim_to_premium_ratio`  
  → Measures how large a claim is relative to the premium  

### Key Insight:
Short policy durations and high claim-to-premium ratios are potential indicators of fraudulent behaviour.

---

## 7. Conclusion

The dataset shows clear behavioural and financial patterns associated with fraud. These insights form the foundation for feature engineering and predictive modeling in subsequent phases.
