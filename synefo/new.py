import sqlite3
con = sqlite3.connect("synefo.db")

import sqlite3

con = sqlite3.connect("synnefo.db")

# con.execute("create table Course(Name text,Duration int,Description text,fee int,Time int)")  
# con.commit()
# # con.execute("create table Admin(Username text,password text)")
# # con.commit()


name=input("enter course name")
Duration=int(input("duration of month"))
Description =input("enter course description")
fee =int(input("enter fee"))
Time = input("enter time")
con.execute("Insert into course(name,Duration,Description,fee,time)values(?,?,?,?,?)",(name,Duration,Description,fee,Time))
con.commit()

