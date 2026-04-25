import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

raw_data_path = BASE_DIR / "data" / "raw" / "insurance_claims.csv"
database_path = BASE_DIR / "database" / "insurance_fraud.db"

df = pd.read_csv(raw_data_path)

conn = sqlite3.connect(database_path)
df.to_sql("insurance_claims", conn, if_exists="replace", index=False)
conn.close()

print(f"Database created successfully at: {database_path}")
print(f"Table created: insurance_claims")
print(f"Rows loaded: {len(df)}")