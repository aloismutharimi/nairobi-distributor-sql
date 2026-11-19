import sqlite3
import pandas as pd

def setup_db():
    # 1. Connect to SQLite (creates the file if it doesn't exist)
    conn = sqlite3.connect("distributor.db")
    cursor = conn.cursor()

    # 2. Drop table if it exists to start fresh
    cursor.execute("DROP TABLE IF EXISTS orders")

    # 3. Create the table
    cursor.execute("""
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            county TEXT,
            product TEXT,
            quantity INTEGER,
            unit_price REAL,
            order_date DATE,
            status TEXT
        )
    """)

    # 4. Insert 20 realistic rows
    orders_data = [
        (1, "Kamau Stores", "Nairobi", "Sugar 50kg", 10, 6500.00, "2023-10-01", "Completed"),
        (2, "Otieno Wholesale", "Kisumu", "Rice 25kg", 50, 3200.00, "2023-10-01", "Completed"),
        (3, "Hassan Traders", "Mombasa", "Cooking Oil 20L", 15, 4500.00, "2023-10-02", "Pending"),
        (4, "Muthoni MiniMart", "Nairobi", "Sugar 50kg", 5, 6500.00, "2023-10-02", "Completed"),
        (5, "Coast Retailers", "Mombasa", "Wheat Flour 50kg", 20, 3800.00, "2023-10-03", "Completed"),
        (6, "Nakuru Agri Supplies", "Nakuru", "Maize 90kg", 100, 4500.00, "2023-10-03", "Pending"),
        (7, "Kamau Stores", "Nairobi", "Cooking Oil 20L", 10, 4500.00, "2023-10-04", "Completed"),
        (8, "Eldoret Wholesalers", "Uasin Gishu", "Rice 25kg", 30, 3200.00, "2023-10-04", "Completed"),
        (9, "Juma & Sons", "Mombasa", "Sugar 50kg", 12, 6500.00, "2023-10-05", "Pending"),
        (10, "Kisumu Traders", "Kisumu", "Wheat Flour 50kg", 40, 3800.00, "2023-10-05", "Completed"),
        (11, "Thika Wholesale", "Kiambu", "Maize 90kg", 25, 4500.00, "2023-10-06", "Completed"),
        (12, "Hassan Traders", "Mombasa", "Rice 25kg", 60, 3200.00, "2023-10-06", "Pending"),
        (13, "Nyamira Distributors", "Nyamira", "Sugar 50kg", 8, 6500.00, "2023-10-07", "Completed"),
        (14, "Machakos Retail", "Machakos", "Cooking Oil 20L", 5, 4500.00, "2023-10-07", "Completed"),
        (15, "Kisumu Traders", "Kisumu", "Maize 90kg", 15, 4500.00, "2023-10-08", "Pending"),
        (16, "Kamau Stores", "Nairobi", "Rice 25kg", 25, 3200.00, "2023-10-08", "Completed"),
        (17, "Garissa Wholesale", "Garissa", "Wheat Flour 50kg", 10, 3800.00, "2023-10-09", "Pending"),
        (18, "Otieno Wholesale", "Kisumu", "Cooking Oil 20L", 8, 4500.00, "2023-10-09", "Completed"),
        (19, "Nakuru Agri Supplies", "Nakuru", "Sugar 50kg", 30, 6500.00, "2023-10-10", "Completed"),
        (20, "Coast Retailers", "Mombasa", "Rice 25kg", 35, 3200.00, "2023-10-10", "Completed")
    ]

    cursor.executemany("""
        INSERT INTO orders (order_id, customer_name, county, product, quantity, unit_price, order_date, status) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, orders_data)

    conn.commit()
    print("✅ Database 'distributor.db' created and 20 rows inserted.")
    conn.close()

if __name__ == "__main__":
    setup_db()