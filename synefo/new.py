import sqlite3
con = sqlite3.connect("synefo.db")

import sqlite3

con = sqlite3.connect("synnefo.db")

# con.execute("create table Course(Name text,Duration int,Description text,fee int,Time int)")  
# con.commit()
con.execute("create table Admin(Username text,password text)")
con.commit()

while True:
    print("""
1.view
2.search
3.login
4.exit""")
    ch = int(input("enter choice"))
    if ch==1:
        data = con.execute("Select * from Course")
        print('{:<20}{:<30}{:<50}{:<10}{:<20}'.format('name','duration','description','fee','time'))
        print('-'*130)
        for cur in data:
            print('{:<20}{:<30}{:<50}{:<10}{:<20}'.format(cur[0],cur[1],cur[2],cur[3],cur[4]))

    elif ch==2:
        cour=input("enter course name")
        data=con.execute("select * from Course where name=?",(cour,))
        print('{:<20}{:<30}{:<50}{:<10}{:<20}'.format('name','duration','description','fee','time'))
        print('-'*130)

        for cur in data:
            print('{:<20}{:<30}{:<50}{:<10}{:<20}'.format(cur[0],cur[1],cur[2],cur[3],cur[4]))
            name=input("enter course name")
            Duration=int(input("duration of month"))
            Description =input("enter course description")
            fee =int(input("enter fee"))
            Time = input("enter time")
            con.execute("Insert into course(name,Duration,Description,fee,time)values(?,?,?,?,?)",(name,Duration,Description,fee,Time))
            con.commit()

    elif ch==3:
            username = input("enter username")
            password = input("enter password")
            data=con.execute("select * from admin Where username=? and password=?",(username,password))
            

        
            f=0
            for i in data:
                f=1
            if f==1:
                print("login succesfull")

            else:
                print("login failed")
            






