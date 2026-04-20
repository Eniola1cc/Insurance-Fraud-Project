# Risk Scoring Summary – Insurance Fraud Risk Prioritisation System

## 1. Overview
This phase converts the machine learning model output into a practical fraud risk prioritisation system for insurance claims.

Rather than using the model only for binary fraud prediction, the project transforms predicted fraud probabilities into business-friendly risk scores and investigation priorities.

## 2. What Was Done
The following steps were completed in this phase:

- Converted predicted fraud probabilities into a 0–100 fraud risk score
- Ranked claims from highest to lowest risk
- Grouped claims into risk bands: High, Medium, and Low
- Assigned recommended investigation actions based on risk level
- Produced a final prioritised claims file for operational use

## 3. Risk Scoring Logic
The fraud model produces a probability score between 0 and 1. This was converted into a risk score between 0 and 100 for easier business interpretation.

### Risk Bands
- **High Risk:** 70 and above
- **Medium Risk:** 40 to 69.99
- **Low Risk:** Below 40

### Recommended Actions
- **High Risk:** Immediate Review
- **Medium Risk:** Secondary Review
- **Low Risk:** Monitor

## 4. Business Value
This phase is important because insurance fraud detection is not only about classifying claims as fraud or non-fraud. In real business operations, investigators need a ranked queue of suspicious claims so that limited review resources can be used effectively.

The prioritisation system helps to:

- focus attention on the most suspicious claims first,
- reduce wasted effort on low-risk claims,
- improve fraud investigation efficiency,
- support operational decision-making.

## 5. Final Outputs
The key outputs of this phase are:

- `final_prioritised_claims.csv`
- `risk_band_summary.csv`
- `top_20_priority_claims.csv`

These outputs can be used in dashboards, reporting, or downstream fraud review workflows.

## 6. Next Step
The next step is to present the prioritisation results in an interactive dashboard so users can:

- filter claims by risk band,
- inspect the highest-risk claims,
- review model performance,
- download prioritised claims for investigation.