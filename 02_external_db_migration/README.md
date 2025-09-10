# External Database Migration

## Problem
Organizations often rely on legacy or external databases. Migrating this data into a centralized database is critical for governance and analytics.

## Solution
This project shows how to:
- Connect to an external database (e.g., MySQL)
- Extract data using SQL
- Transform data into a standardized schema
- Load into PostgreSQL (our target database)

## Tools
- Python (psycopg2, SQLAlchemy)
- SQL scripts for transformations
- ERD (Entity Relationship Diagram) in `docs/`

## How to Run
1. Update `config.json` with external DB connection credentials.
2. Run `scripts/migrate_data.py`.
3. Validate migrated tables using the SQL queries in `sql/`.
