"""
Ingest Excel files into PostgreSQL
Author: swensoneric
Date: 2025-09-10
"""

import os
import pandas as pd
from sqlalchemy import create_engine

# ---------- CONFIG ----------
DATA_DIR = "../data"
DB_URI = "postgresql+psycopg2://username:password@localhost:5432/mydatabase"
TABLE_NAME = "excel_data"
# ----------------------------

def load_excel_files_to_db():
    engine = create_engine(DB_URI)

    for file in os.listdir(DATA_DIR):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            file_path = os.path.join(DATA_DIR, file)
            print(f"Processing {file_path}...")

            df = pd.read_excel(file_path)
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
            df.dropna(how="all", inplace=True)

            df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
            print(f"Loaded {len(df)} rows from {file} into {TABLE_NAME}.")

    print("All Excel files processed!")

if __name__ == "__main__":
    load_excel_files_to_db()
