# Data Pipeline (Airflow + dbt)

## Problem
Data ingestion and transformation should not be manual. Companies need automated, reliable pipelines to keep data fresh and consistent.

## Solution
This project simulates a modern data pipeline using:
- **Airflow** for scheduling and orchestration
- **dbt** for modular SQL transformations
- Logging to monitor pipeline health

## Tools
- Apache Airflow
- dbt (Data Build Tool)
- PostgreSQL

## How to Run
1. Start Airflow with Docker Compose (`docker-compose up`).
2. Deploy DAGs from `airflow_dags/`.
3. Run dbt models from `dbt_project/`.
4. Check logs in `logs/` for pipeline status.
