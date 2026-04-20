# Insurance Fraud Risk Prioritisation System

## Project Overview
This project builds a data-driven system for identifying and prioritising potentially fraudulent insurance claims. Instead of treating fraud detection as a simple classification problem, the project focuses on business decision-making: ranking claims by fraud risk so investigators can review the most suspicious cases first.

The goal is to help insurance companies improve fraud detection efficiency, reduce wasted investigative effort, and support better allocation of limited fraud investigation resources.

## Business Problem
Insurance companies process large numbers of claims, but only a limited proportion can be manually reviewed. Without an intelligent prioritisation system, high-risk claims may be missed while low-risk claims consume investigator time.

This project addresses that challenge by:
- predicting the likelihood that a claim is fraudulent,
- assigning a fraud risk score,
- ranking claims from highest to lowest risk,
- analysing how much fraud can be captured when only the top 10%, 20%, or 30% of claims are reviewed.

## Project Objectives
The main objectives are to:
- understand fraud patterns in historical claims data,
- engineer fraud-relevant features,
- compare multiple machine learning models,
- select a suitable model for fraud prioritisation,
- evaluate both statistical performance and business usefulness.

## Dataset
The dataset contains 1,000 insurance claims and 40 original features covering customer details, policy information, and incident characteristics. The target variable is `fraud_reported`, indicating whether a claim is fraudulent or not.

Key dataset observations:
- Fraud rate is approximately 24.7%
- The dataset is imbalanced
- Higher claim amounts and missing police reports appear associated with fraud
- Short policy duration may be an indicator of suspicious behaviour

## Project Structure
```text
Insurance-Fraud-Project/
│
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── business_problem.md
│   ├── data_understanding.md
│   ├── modeling_summary.md
│   └── risk_scoring_summary.md
├── models/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
├── reports/
│   ├── model_results.csv
│   ├── business_metrics.csv
│   ├── business_summary.md
│   ├── ranked_claims.csv
│   ├── final_prioritised_claims.csv
│   ├── risk_band_summary.csv
│   └── top_20_priority_claims.csv
├── app.py
└── README.md
```


---

## Workflow

### Phase 1: Foundation
- Defined the business problem  
- Explored the dataset  
- Identified fraud distribution and data quality issues  
- Created initial engineered features such as:
  - `policy_duration_days`
  - `claim_to_premium_ratio`

---

### Phase 2: Feature Engineering and Modeling
- Built fraud-relevant engineered features  
- Trained baseline models:
  - Logistic Regression  
  - Random Forest  
  - Gradient Boosting  

- Evaluated models using:
  - Precision  
  - Recall  
  - F1 Score  
  - ROC-AUC  

---

### Phase 3: Risk Prioritisation
- Converted model outputs into **fraud risk scores**  
- Ranked claims from highest to lowest risk  
- Evaluated fraud capture at different review thresholds  
- Prepared outputs for business decision-making and dashboards  

---

## Model Performance Summary
The baseline model comparison showed:

- **Logistic Regression**  
  - Strong balance between precision and recall  
  - Best overall F1 Score  
  - Highly interpretable  

- **Random Forest**  
  - Highest ROC-AUC  
  - Best for ranking claims by fraud likelihood  

- **Gradient Boosting**  
  - Moderate performance between both models  

**Key Insight:**  
- Logistic Regression is suitable for **classification and interpretability**  
- Random Forest is better for **risk ranking and prioritisation**

---

## Risk Prioritisation Output
In Phase 3, the fraud model output was transformed into a practical claims review workflow by:

- converting fraud probabilities into a 0–100 risk score,
- grouping claims into High, Medium, and Low risk bands,
- assigning recommended investigation actions,
- generating a final prioritised claims file.

## Dashboard
A Streamlit dashboard was built to display:

- model comparison results,
- threshold-based fraud capture analysis,
- risk band summaries,
- top priority claims,
- a downloadable prioritised claims table.

---

## Business Value
This project focuses on **decision support**, not just prediction.

The system enables insurers to:

- detect more fraud within limited review capacity  
- reduce manual workload  
- prioritise high-risk claims effectively  
- improve operational efficiency  

---

## Key Deliverables
- Fraud risk prioritisation model  
- Ranked claims by fraud score  
- Fraud capture analysis at different thresholds  
- Model comparison report  
- Visual evaluation outputs  
- End-to-end GitHub portfolio project  

---

## Tools Used
- Python  
- Pandas  
- NumPy  
- scikit-learn  
- Jupyter Notebook  
- Matplotlib  

---

## Next Steps

- Add explainability using Feature Importance and SHAP
- Build an interactive dashboard or Streamlit app
- Create a ranked claims output for investigator review
- Package the workflow into reusable Python scripts 

---

## Author
**Adesanmi Eniola Adetoba**
