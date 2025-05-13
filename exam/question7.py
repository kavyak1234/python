import sqlite3
def insert_product(db_name,product_id,product_name,product_price):
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    cursor.execute("insert into product(id,name,price)values(???)",(product_id,product_name,product_price))
    conn.commit()
    conn.close

