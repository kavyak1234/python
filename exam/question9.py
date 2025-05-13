import sqlite3
con = sqlite3.connect("question9.db")
# con.execute("create table product(id int,name text,price int)")  
# con.commit() 

# id=int(input("enter id"))
# name=input("enter name")
# price=int(input("enter price"))
# con.execute("insert into product(id,name,price)values(?,?,?)",(id,name,price))
# con.commit()

id = int(input("enter id"))
data=con.execute("update product set price=275 where id=?",(id,))
data1=con.execute("select * from product where id=?",(id,))
con.commit()
