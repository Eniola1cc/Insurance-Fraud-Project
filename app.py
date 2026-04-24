import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Insurance Fraud Risk Prioritisation System",
    page_icon="🚨",
    layout="wide"
)

# -------------------------------
# Helper functions
# -------------------------------
@st.cache_data
def load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None


def format_percentage(value):
    return f"{value * 100:.2f}%"


# -------------------------------
# Load data
# -------------------------------
final_claims = load_csv("reports/final_prioritised_claims.csv")
business_metrics = load_csv("reports/business_metrics.csv")
model_results = load_csv("reports/model_results.csv")
risk_band_summary = load_csv("reports/risk_band_summary.csv")
top_20_claims = load_csv("reports/top_20_priority_claims.csv")

required_files = {
    "reports/final_prioritised_claims.csv": final_claims,
    "reports/business_metrics.csv": business_metrics,
    "reports/model_results.csv": model_results,
    "reports/risk_band_summary.csv": risk_band_summary,
    "reports/top_20_priority_claims.csv": top_20_claims,
}

missing_files = [path for path, data in required_files.items() if data is None]

if missing_files:
    st.error("Some required files are missing. Please generate them from the notebooks first.")
    st.write(missing_files)
    st.stop()

# -------------------------------
# Title
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

risk_band_options = sorted(final_claims["risk_band"].dropna().unique().tolist())
action_options = sorted(final_claims["recommended_action"].dropna().unique().tolist())

risk_band_filter = st.sidebar.multiselect(
    "Select Risk Band",
    options=risk_band_options,
    default=risk_band_options
)

recommended_action_filter = st.sidebar.multiselect(
    "Select Recommended Action",
    options=action_options,
    default=action_options
)

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
    business_metrics["review_threshold"] == "Top 30%",
    "fraud_capture_rate"
]

top_30_capture_value = (
    format_percentage(top_30_capture.iloc[0])
    if not top_30_capture.empty else "N/A"
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Claims", f"{total_claims:,}")
col2.metric("High Risk", f"{high_risk_claims:,}")
col3.metric("Medium Risk", f"{medium_risk_claims:,}")
col4.metric("Low Risk", f"{low_risk_claims:,}")
col5.metric("Top 30% Fraud Capture", top_30_capture_value)

# -------------------------------
# Charts
# -------------------------------
st.subheader("Risk Score Distribution")
st.bar_chart(final_claims["risk_band"].value_counts())

st.subheader("Fraud Capture vs Review Threshold")
capture_chart = business_metrics.copy()
capture_chart["fraud_capture_rate_pct"] = capture_chart["fraud_capture_rate"] * 100
st.line_chart(
    capture_chart.set_index("review_threshold")["fraud_capture_rate_pct"]
)

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
# Feature importance
# -------------------------------
feature_importance_path = "reports/figures/feature_importance.png"

if os.path.exists(feature_importance_path):
    st.subheader("Top Fraud Risk Drivers")
    st.markdown(
        """
This chart shows the most influential variables used by the model when estimating fraud risk.
"""
    )
    st.image(feature_importance_path)
else:
    st.warning("Feature importance chart not found. Generate `reports/figures/feature_importance.png` from the notebook.")

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
# Prioritised claims table
# -------------------------------
st.subheader("Prioritised Claims Table")
st.markdown("Use the sidebar filters to focus on specific claim groups.")

if filtered_claims.empty:
    st.warning("No claims match the selected filters.")
else:
    st.dataframe(filtered_claims, use_container_width=True)

# -------------------------------
# Explain selected claim
# -------------------------------
st.subheader("Why This Claim Is High Risk")

if filtered_claims.empty:
    st.info("Select at least one risk band and action to view claim details.")
else:
    selected_rank = st.selectbox(
        "Select a claim by priority rank",
        options=filtered_claims["priority_rank"].tolist()
    )

    selected_claim = filtered_claims[
        filtered_claims["priority_rank"] == selected_rank
    ].iloc[0]

    col_a, col_b, col_c = st.columns(3)

    col_a.metric("Priority Rank", int(selected_claim["priority_rank"]))
    col_b.metric("Risk Score", f"{selected_claim['risk_score_100']:.2f}")
    col_c.metric("Risk Band", selected_claim["risk_band"])

    st.markdown("### Selected Claim Details")

    important_columns = [
        "priority_rank",
        "risk_score_100",
        "risk_band",
        "recommended_action",
        "actual_fraud",
        "total_claim_amount",
        "policy_annual_premium",
        "claim_to_premium_ratio",
        "incident_severity",
        "insured_hobbies",
        "insured_occupation",
        "property_damage",
        "police_report_available",
    ]

    available_columns = [
        col for col in important_columns
        if col in selected_claim.index
    ]

    st.dataframe(
        selected_claim[available_columns].to_frame(name="value"),
        use_container_width=True
    )

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
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    """
**Project Purpose:**  
This system supports fraud investigation prioritisation by turning model outputs into a business-facing review workflow.
"""
)