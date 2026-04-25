# 🚨 Insurance Fraud Risk Prioritisation System

## 📌 Project Overview
This project builds a **fraud risk prioritisation system** for insurance claims, designed to help investigators focus on the most suspicious cases first.

Instead of simply predicting whether a claim is fraudulent, the system:
- assigns a **fraud risk score** to each claim,
- ranks claims by risk level,
- enables **prioritised investigation** of high-risk cases.

---

## 🎯 Business Problem
Insurance companies process thousands of claims, but investigation resources are limited. Reviewing every claim manually is inefficient and leads to:

- missed fraud cases,
- wasted effort on low-risk claims,
- delayed investigation workflows.

This project addresses that problem by transforming fraud detection into a **decision-support system** that prioritises claims based on risk.

---

## 💡 Solution Approach

The system combines data processing, machine learning, and business logic to create a practical fraud prioritisation workflow.

### 🔹 Key Capabilities
- Predicts fraud likelihood for each claim  
- Converts predictions into a **0–100 risk score**  
- Groups claims into **Low / Medium / High risk bands**  
- Ranks claims for investigation priority  
- Measures **fraud capture vs workload trade-offs**  
- Provides a **dashboard for business users**

---

## ⚙️ Tech Stack

- **Python** (Pandas, NumPy)
- **Scikit-learn** (Logistic Regression, Random Forest, Gradient Boosting)
- **Matplotlib** (visualisation)
- **Streamlit** (dashboard)
- **Joblib** (model persistence)

---

## 📊 Model Development

### Models Trained
- Logistic Regression
- Random Forest
- Gradient Boosting

### Model Selection
- Logistic Regression selected for:
  - best **F1-score balance**
  - higher **recall** (important for fraud detection)
  - interpretability

- Random Forest used for:
  - strong **ranking capability (ROC-AUC)**

---

## 📈 Business Evaluation

The model was evaluated not just by accuracy, but by **business impact**:

| Review Threshold | Fraud Capture | Workload Reduction |
|-----------------|-------------|--------------------|
| Top 10%         | 20.4%       | 90%                |
| Top 20%         | 51.0%       | 80%                |
| Top 30%         | 71.4%       | 70%                |

---

## 💼 Business Impact

- Captures **71% of fraud** by reviewing only **30% of claims**
- Reduces investigation workload by **70%**
- Enables **risk-based prioritisation**
- Improves investigator efficiency and decision-making

---

## 🧠 Risk Scoring System

### Risk Bands
- **High Risk** → Immediate Review  
- **Medium Risk** → Secondary Review  
- **Low Risk** → Monitor  

Each claim is:
- scored (0–100),
- ranked,
- assigned an investigation action.

---

## 📊 Dashboard (Streamlit)

The project includes an interactive dashboard that allows users to:

- view prioritised claims
- filter by risk band and action
- analyse fraud capture performance
- compare model performance
- download investigation-ready data

### 🔍 Dashboard Preview
![Dashboard](reports/figures/dashboard.png)

---

## 🔍 Explainability

The system includes model explainability through:

- Feature importance (top fraud drivers)
- Identification of key variables influencing fraud risk

---


## Project Structure
```text
Insurance-Fraud-Project/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_model_training.ipynb
│ └── 04_risk_scoring_and_dashboard_prep.ipynb
│
├── models/
│ └── fraud_model_pipeline.pkl
│
├── reports/
│ ├── model_results.csv
│ ├── business_metrics.csv
│ ├── final_prioritised_claims.csv
│ ├── risk_band_summary.csv
│ ├── top_20_priority_claims.csv
│ └── figures/
│ ├── confusion_matrix.png
│ ├── roc_curve.png
│ └── feature_importance.png
│
├── docs/
│ ├── business_problem.md
│ ├── data_understanding.md
│ ├── modeling_summary.md
│ └── risk_scoring_summary.md
│
├── app.py
├── requirements.txt
└── README.md
```
---



---

## 🚀 How to Run the Project

### 1. Clone the repo
```bash
git clone https://github.com/Eniola1cc/Insurance-Fraud-Project.git
cd Insurance-Fraud-Project
2. Install dependencies
pip install -r requirements.txt
3. Run the dashboard
streamlit run app.py
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

## Business Impact

- Captures **71% of fraud** by reviewing only **30% of claims**
- Reduces investigation workload by **70%**
- Enables prioritised fraud detection workflow
- Improves investigator efficiency and resource allocation

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

## Project Status

This project is almost complete and includes:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Fraud detection modelling
- Risk scoring and ranking
- Top 10%, 20%, and 30% fraud capture analysis
- Business impact reporting
- Streamlit dashboard
- SQL-based analysis queries
- Model explainability using SHAP

## How to Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Author
**Adesanmi Eniola Adetoba**
