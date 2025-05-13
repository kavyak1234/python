import sqlite3

con = sqlite3.connect("qstn12.db")
# con.execute("create table customers(id int,name text,email text)")  
# con.commit() 

id=int(input("enter id"))
name=input("enter name")
email=input("enter email")
con.execute("insert into customers(id,name,email)values(?,?,?)",(id,name,email))
con.commit()
