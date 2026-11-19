# Nairobi Distributor — Weekly Sales SQL Report

A Python and SQLite solution that automates the 5 weekly reporting questions asked by the sales manager, reducing 45 minutes of manual Excel work into a 2-second automated terminal report.

## The Business Problem
Every Monday morning, the sales manager spends 45 minutes manually cross-referencing Excel spreadsheets to answer 5 critical questions about sales performance, pending orders, and top products. This is prone to human error and wastes valuable time.

## The Solution
A lightweight SQLite database and a Python script that runs 5 optimized SQL queries in milliseconds, printing the results directly to the terminal.

## The 5 Questions Automated
1. **Mombasa Orders:** All orders originating from Mombasa county.
2. **Top 10 Orders:** Ranked by total value (quantity × unit_price).
3. **County Revenue:** Total revenue generated per county.
4. **High-Value Pending:** All pending orders worth over KES 50,000.
5. **Best Sellers:** The top 3 products by total quantity sold.

## How to Run
1. Install requirements: 

`pip install pandas`

2. Create and populate the database: 

`python setup_database.py`

3. Run the weekly report: 

`python queries.py`

## 💰 Commercial Value & Pricing Note

*If a distributor wanted this system built and maintained, here is the cost:*

**Setup Fee: KES 25,000 - 35,000 (One-time)**
This covers consultation, database creation, historical data migration, script development, and a handover session. 

**Monthly Maintenance: KES 2,000 - 3,000 / month**
This covers weekly data backups, bug fixes, script adjustments for new metrics, and a monthly 1-page PDF summary. 

*Why? Because this system instantly recovers 3 hours of admin time per month and prevents costly errors (like missing a KES 450,000 pending order).*