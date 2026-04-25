import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

database_path = BASE_DIR / "database" / "insurance_fraud.db"
output_dir = BASE_DIR / "reports" / "sql_outputs"
output_dir.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(database_path)

queries = {
    "fraud_distribution": """
        SELECT 
            fraud_reported,
            COUNT(*) AS claim_count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM insurance_claims), 2) AS percentage
        FROM insurance_claims
        GROUP BY fraud_reported;
    """,

    "fraud_by_incident_type": """
        SELECT 
            incident_type,
            COUNT(*) AS total_claims,
            SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) AS fraud_cases,
            ROUND(SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fraud_rate
        FROM insurance_claims
        GROUP BY incident_type
        ORDER BY fraud_rate DESC;
    """,

    "average_claim_by_fraud_status": """
        SELECT 
            fraud_reported,
            ROUND(AVG(total_claim_amount), 2) AS average_claim_amount
        FROM insurance_claims
        GROUP BY fraud_reported;
    """,

    "fraud_by_police_report": """
        SELECT 
            police_report_available,
            COUNT(*) AS total_claims,
            SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) AS fraud_cases,
            ROUND(SUM(CASE WHEN fraud_reported = 'Y' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fraud_rate
        FROM insurance_claims
        GROUP BY police_report_available
        ORDER BY fraud_rate DESC;
    """
}

for name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    output_path = output_dir / f"{name}.csv"
    result.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

conn.close()

print("SQL analysis completed successfully.")