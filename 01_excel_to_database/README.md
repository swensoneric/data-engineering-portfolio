# Excel to Database Project

## Problem
Many companies store operational data in Excel spreadsheets. Analysts often struggle to query and scale this data efficiently.

## Solution
This project ingests Excel files into a relational database (e.g., PostgreSQL).  
It demonstrates:
- Cleaning and validating Excel data with **Python (pandas)**
- Designing a simple relational schema
- Loading data into PostgreSQL using **SQLAlchemy**
- Querying the database with SQL

## Tools
- Python (pandas, openpyxl, SQLAlchemy)
- PostgreSQL
- Docker (optional)

## How to Run
1. Place Excel files in the `data/` folder.
2. Run the ingestion script in `scripts/ingest_excel.py`.
3. Query the data via the SQL scripts in `notebooks/` or directly in PostgreSQL.
