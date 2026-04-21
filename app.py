import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Insurance Fraud Risk Prioritisation System",
    page_icon="🚨",
    layout="wide"
)

# -------------------------------
# Load data
# -------------------------------
final_claims = pd.read_csv("reports/final_prioritised_claims.csv")
business_metrics = pd.read_csv("reports/business_metrics.csv")
model_results = pd.read_csv("reports/model_results.csv")
risk_band_summary = pd.read_csv("reports/risk_band_summary.csv")
top_20_claims = pd.read_csv("reports/top_20_priority_claims.csv")

# -------------------------------
# Title and introduction
# -------------------------------
st.title("🚨 Insurance Fraud Risk Prioritisation System")
st.markdown(
    """
This dashboard presents an insurance fraud risk prioritisation workflow designed to help investigators
focus on the most suspicious claims first.

The system combines machine learning model outputs, business threshold analysis, and ranked claims scoring
to support more efficient fraud investigation.
"""
)

# -------------------------------
# Sidebar filters
# -------------------------------
st.sidebar.header("Filters")

risk_band_filter = st.sidebar.multiselect(
    "Select Risk Band",
    options=sorted(final_claims["risk_band"].dropna().unique().tolist()),
    default=sorted(final_claims["risk_band"].dropna().unique().tolist())
)

recommended_action_filter = st.sidebar.multiselect(
    "Select Recommended Action",
    options=sorted(final_claims["recommended_action"].dropna().unique().tolist()),
    default=sorted(final_claims["recommended_action"].dropna().unique().tolist())
)

# Apply filters
filtered_claims = final_claims[
    (final_claims["risk_band"].isin(risk_band_filter)) &
    (final_claims["recommended_action"].isin(recommended_action_filter))
]

# -------------------------------
# Key metrics
# -------------------------------
st.subheader("Key Dashboard Metrics")

total_claims = len(final_claims)
high_risk_claims = (final_claims["risk_band"] == "High").sum()
medium_risk_claims = (final_claims["risk_band"] == "Medium").sum()
low_risk_claims = (final_claims["risk_band"] == "Low").sum()

top_30_capture = business_metrics.loc[
    business_metrics["review_threshold"] == "Top 30%", "fraud_capture_rate"
]

top_30_capture_value = (
    f"{top_30_capture.iloc[0] * 100:.2f}%"
    if not top_30_capture.empty else "N/A"
)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Claims", f"{total_claims:,}")
col2.metric("High Risk", f"{high_risk_claims:,}")
col3.metric("Medium Risk", f"{medium_risk_claims:,}")
col4.metric("Low Risk", f"{low_risk_claims:,}")
col5.metric("Top 30% Fraud Capture", top_30_capture_value)

# -------------------------------
# Business threshold analysis
# -------------------------------
st.subheader("Business Threshold Performance")
st.markdown(
    """
This table shows how much fraud can be captured when investigators review only the highest-risk subset of claims.
"""
)
st.dataframe(business_metrics, use_container_width=True)

# -------------------------------
# Model comparison
# -------------------------------
st.subheader("Model Comparison Results")
st.markdown(
    """
The project compared multiple baseline models to evaluate fraud detection performance.
"""
)
st.dataframe(model_results, use_container_width=True)

# -------------------------------
# Risk band summary
# -------------------------------
st.subheader("Risk Band Summary")
st.markdown(
    """
This summary shows the number of claims, fraud cases, and average risk score within each risk band.
"""
)
st.dataframe(risk_band_summary, use_container_width=True)

# -------------------------------
# Top priority claims
# -------------------------------
st.subheader("Top 20 Priority Claims")
st.markdown(
    """
These are the highest-ranked claims based on predicted fraud risk and should be prioritised for review.
"""
)
st.dataframe(top_20_claims, use_container_width=True)

# -------------------------------
# Full prioritised claims table
# -------------------------------
st.subheader("Prioritised Claims Table")
st.markdown(
    """
Use the sidebar filters to focus on specific claim groups.
"""
)
st.dataframe(filtered_claims, use_container_width=True)

# -------------------------------
# Download section
# -------------------------------
st.subheader("Download Filtered Results")

csv_data = filtered_claims.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered prioritised claims CSV",
    data=csv_data,
    file_name="filtered_prioritised_claims.csv",
    mime="text/csv"
)

# -------------------------------
# Footer note
# -------------------------------
st.markdown("---")
st.markdown(
    """
**Project Purpose:**  
This system is designed to support fraud investigation prioritisation by turning model outputs into a business-facing review workflow.
"""
)