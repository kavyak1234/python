# import sqlite3

# con = sqlite3.connect("sample.db")

# try:
#     con.execute("create table Student(roll int,name text,age int)")  #text-string
#     con.commit() #save

# except:
#     pass

# con.execute("insert into student(roll,name,age)values(1,'akhil',22),(2,'manu',24)")
# con.commit()

# roll = int(input("enter roll"))
# name = input("enter name")
# age = int(input("enter age"))
# con.execute("insert into student(roll,name,age)values(?,?,?)",(roll,name,age))#insert cheyyandea variable annnu question mark

# con.commit()

# import sqlite3
# con = sqlite3.connect("sample.db")

# data = con.execute("select  roll,name,age from student")
# print('{:<10}{:<20}{:<10}' .format('roll','name','age'))

# for i in data:
#     print('{:<10}{:<20}{:<10}'.format(i[0],i[1],i[2]))


# import sqlite3
# con = sqlite3.connect("sample.db")
# # data = con.execute("select * from student where roll=1 or name='manu")# condition add cheyyan where use cheyyunu
# data = con.execute("select * from student order by roll desc")
# # print(data)
# for i in data:
#     print(i)

# import sqlite3
# con = sqlite3.connect("sample.db")
# roll = int(input("enter roll")) 
# data = con.execute("select * from student where  roll = ?",(roll,))    #roll number enter cheyumbo display cheyd kanikkan                                                                                                                                                                              
# con.commit()
# for i in data:
#     print(i)

# import sqlite3
# con = sqlite3.connect("sample.db")
# roll = int(input("enter roll")) 
# data = con.execute("select * from student where  roll = ?",(roll,)) #roll number enter cheyumbo display cheyd kanikkan   
# print('{:<10}{:<10}{:<10}' .format('roll','name','age'))                                                                                                                           
# con.commit()
# for i in data:
#     print('{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2]))
    
# import sqlite3
# con = sqlite3.connect("sample.db")
# data = con. execute("select * from student where name like'____'") #underscore used in letters using
# for i in data:
#     print(i)

# import sqlite3
# con = sqlite3.connect("sample.db")
# con.execute("update Student set name='kavya',age=54 where roll=5")
# con.commit()

# import sqlite3
# con = sqlite3.connect("sample.db")
# data =  con.execute("update Student set name='appu',age=22 where roll=1")
# data1 = con. execute("select *from student where roll =1")
# con.commit()
# for i in data1:
#     print(i)

# import sqlite3
# con = sqlite3.connect("sample.db")
# roll=int(input("enter roll"))
# data =  con.execute("update Student set name='appu',age=22 where roll=?",(roll,))
# data1 = con. execute("select *from student where roll =?",(roll,))
# con.commit()
# for i in data1:
#     print(i)

#delete
# import sqlite3
# con = sqlite3.connect("sample.db")
# data=con.execute("delete from Student where roll=3")
# data1 = con.execute("select * from student ")
# con.commit()

# for i in data1:
#     print(i)

# import sqlite3

# con = sqlite3.connect("sample.db")

# # con.execute("create table mark(roll int,sub text,mark int)")
# # con.commit()
# con.execute("insert into mark(roll,sub,mark)values(1,'eng',65),(2,'maths',75)")
# con.commit()

# data= con.execute("select student.roll,student.name,student.age,mark.sub,mark.mark from student join mark on student.roll=mark.roll")
# for i in data:
#     print(i)

#aggregation
#max
# import sqlite3

# con = sqlite3.connect("sample.db")

# data = con.execute("select max(roll)from mark")#2
# print(data)
# for i in data:
#     print(i)

#minimum
# import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select min(roll)from mark")#1
# print(data)
# for i in data:
#     print(i)

#sum

# import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select sum(roll)from student")#3
# print(data)
# for i in data:
#     print(i)

#average
#import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select sum(roll)from student")#3
# print(data)
# for i in data:
#     print(i)

#count
# import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select count(roll)from student")#3
# print(data)
# for i in data:
#     print(i)


# import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select max(roll)from student")#3
# print(data)
# for i in data:
#     print(i)

# import sqlite3

# con = sqlite3.connect("sample.db")
# data = con.execute("select roll,name,max(age)from student group by name")
# for i in data:

#     print(i)














