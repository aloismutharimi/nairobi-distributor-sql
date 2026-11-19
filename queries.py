import sqlite3
import pandas as pd

def run_queries():
    # Connect to the database
    conn = sqlite3.connect("distributor.db")

    print("=" * 60)
    print(" 📊 NAIROBI DISTRIBUTOR — WEEKLY SALES REPORT 📊 ".center(60, " "))
    print("=" * 60)

    # -------------------------------------------------------------------------
    # Q1: All orders from Mombasa county
    # -------------------------------------------------------------------------
    q1_sql = """
        SELECT order_id, customer_name, product, quantity, status
        FROM orders
        WHERE county = 'Mombasa';
    """
    q1_df = pd.read_sql_query(q1_sql, conn)
    print("\n1. ALL ORDERS FROM MOMBASA COUNTY")
    print(q1_df.to_string(index=False))

    # -------------------------------------------------------------------------
    # Q2: Top 10 orders by total value
    # Note: Total value = quantity * unit_price. We use ORDER BY and LIMIT.
    # -------------------------------------------------------------------------
    q2_sql = """
        SELECT order_id, customer_name, product, quantity, unit_price,
               (quantity * unit_price) AS total_value
        FROM orders
        ORDER BY total_value DESC
        LIMIT 10;
    """
    q2_df = pd.read_sql_query(q2_sql, conn)
    # Format the total_value column for the printout
    q2_df["total_value"] = q2_df["total_value"].map("KES {:,.2f}".format)
    print("\n2. TOP 10 ORDERS BY TOTAL VALUE")
    print(q2_df.to_string(index=False))

    # -------------------------------------------------------------------------
    # Q3: Total revenue per county
    # We calculate revenue per row, then SUM it and GROUP BY county.
    # -------------------------------------------------------------------------
    q3_sql = """
        SELECT county, SUM(quantity * unit_price) AS total_revenue
        FROM orders
        GROUP BY county
        ORDER BY total_revenue DESC;
    """
    q3_df = pd.read_sql_query(q3_sql, conn)
    q3_df["total_revenue"] = q3_df["total_revenue"].map("KES {:,.2f}".format)
    print("\n3. TOTAL REVENUE PER COUNTY")
    print(q3_df.to_string(index=False))

    # -------------------------------------------------------------------------
    # Q4: All pending orders over KES 50,000
    # We use AND to combine two conditions.
    # -------------------------------------------------------------------------
    q4_sql = """
        SELECT order_id, customer_name, county, (quantity * unit_price) AS total_value
        FROM orders
        WHERE status = 'Pending' 
          AND (quantity * unit_price) > 50000;
    """
    q4_df = pd.read_sql_query(q4_sql, conn)
    q4_df["total_value"] = q4_df["total_value"].map("KES {:,.2f}".format)
    print("\n4. PENDING ORDERS OVER KES 50,000")
    print(q4_df.to_string(index=False))

    # -------------------------------------------------------------------------
    # Q5: The three best-selling products by quantity
    # -------------------------------------------------------------------------
    q5_sql = """
        SELECT product, SUM(quantity) AS total_quantity_sold
        FROM orders
        GROUP BY product
        ORDER BY total_quantity_sold DESC
        LIMIT 3;
    """
    q5_df = pd.read_sql_query(q5_sql, conn)
    print("\n5. TOP 3 BEST-SELLING PRODUCTS BY QUANTITY")
    print(q5_df.to_string(index=False))

    print("\n" + "=" * 60)
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    run_queries()