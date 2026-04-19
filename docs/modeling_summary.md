# Modeling Summary – Insurance Fraud Risk Prioritisation System

## 1. Overview
This phase of the project focused on building and evaluating machine learning models to predict whether an insurance claim is fraudulent. The objective was not only to classify fraud cases, but also to support the ranking of claims by risk level for prioritised investigation.

## 2. Models Trained
Three baseline models were trained and compared:

- Logistic Regression
- Gradient Boosting
- Random Forest

These models were selected to provide a balance between interpretability and predictive power.

## 3. Evaluation Metrics

### Precision
Precision measures the proportion of claims predicted as fraud that were actually fraudulent.

**Business meaning:** High precision reduces false positives, meaning investigators spend less time reviewing legitimate claims.

### Recall
Recall measures the proportion of actual fraud cases that were correctly identified by the model.

**Business meaning:** High recall helps the insurer detect more fraud and reduce missed fraudulent claims.

### F1 Score
F1 Score is the harmonic mean of precision and recall.

**Business meaning:** It is useful when fraud detection requires a balance between catching fraud and avoiding too many false alerts.

### ROC-AUC
ROC-AUC measures the model’s ability to rank fraudulent claims above non-fraudulent claims across thresholds.

**Business meaning:** A higher ROC-AUC means the model is better at prioritising suspicious claims for review.

## 4. Model Results

- **Logistic Regression**
  - Accuracy: 0.825
  - Precision: 0.625
  - Recall: 0.714
  - F1 Score: 0.667
  - ROC-AUC: 0.833

- **Gradient Boosting**
  - Accuracy: 0.795
  - Precision: 0.587
  - Recall: 0.551
  - F1 Score: 0.568
  - ROC-AUC: 0.838

- **Random Forest**
  - Accuracy: 0.780
  - Precision: 0.600
  - Recall: 0.306
  - F1 Score: 0.405
  - ROC-AUC: 0.841

## 5. Interpretation of Results
The results show that **Logistic Regression achieved the strongest F1 Score**, meaning it offered the best balance between precision and recall among the tested models.

It also had the highest recall, which is important in fraud detection because missing fraudulent claims can be costly.

**Random Forest achieved the highest ROC-AUC**, which suggests it may be useful when the main goal is ranking claims by fraud likelihood rather than direct classification at a fixed threshold.

**Gradient Boosting** performed moderately and did not outperform Logistic Regression on F1 or recall.

## 6. Model Choice
For this phase, **Logistic Regression is the preferred baseline model** because:

- it provides the strongest balance between fraud detection and false alerts,
- it is easier to interpret,
- it is suitable for communicating results to business stakeholders.

However, **Random Forest remains important for prioritisation analysis**, since its higher ROC-AUC suggests stronger ranking performance for risk-based review workflows.

## 7. Business Implication
The model comparison shows that different models are useful for different business purposes:

- **Logistic Regression** is better for balanced fraud classification and explainability.
- **Random Forest** is better for ranking claims by risk score.

This supports the project goal of building a fraud risk prioritisation system rather than just a binary classifier.

## 8. Next Step
The next step is to operationalise the model output into a ranked claims review workflow and present results in a dashboard or Streamlit app.