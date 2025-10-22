"""
Ingest Excel files into PostgreSQL
Author: swensoneric
Date: 2025-09-10
"""

import os
import pandas as pd
from sqlalchemy import create_engine

# ---------- CONFIG ----------
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "chewy")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "venmo_data")

DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DATA_DIR = "../data"
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
