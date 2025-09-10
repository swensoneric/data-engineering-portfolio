# Analytics Layer

## Problem
Stakeholders need dashboards and self-service analytics to make business decisions.  

## Solution
This layer provides:
- Clean SQL queries for reporting
- Pre-aggregated tables in the warehouse
- Example dashboards (Power BI or Tableau)

## Tools
- SQL
- Tableau / Power BI
- dbt (upstream transformations)

## How to Run
1. Connect BI tool to the database.
2. Import queries from `queries/`.
3. Open dashboards in `dashboards/`.
