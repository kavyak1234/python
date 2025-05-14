import sqlite3
def read_products(db_name):
    conn = sqlite3.connect(db_name)
    cursor =conn.cursor()
    cursor.execute("SELECT* FROM PRODUCTS")
    rows = cursor.fetchall()
    conn.close
    return rows

    
