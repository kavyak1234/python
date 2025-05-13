# student=[]
# while True:
#     print("""
# 1.Register
# 2.View
# 3.Update
# 4.Delete
# 5.Search
# 6.exit""")
#     while True:
#         try:
#             ch=int(input("Enter your choice"))
#             break
#         except:
#             print('enter a number')
#     if ch==1:
#         if len(student)==0:
#             adm=1
#         else:
#             adm=student[-1]['adm_no']+1
#         name=input("Enter name:")
#         age=int(input("Enter age:"))
#         cur=input("Enter course:")
#         fee=int(input("Enter fee:"))
#         student.append({"adm_no":adm,"name":name,"age":age,"course":cur,"fee":fee})
#     elif ch==2:
#         print('{:<10}{:<20}{:<10}{:<20}{:<10}' .format('adm_no','name','age','course','fee'))#for formating the output to a table structure
#         print('-'*70)
#         print(std)
#         for std in student:
#             print('{:<10}{:<20}{:<10}{:<20}{:<10}' .format(std['adm_no'],std['name'],std['age'],std['course'],std['fee']))#for formating the output to a table structure
#     elif ch==3:
#         adm=int(input("Enter adm no:"))
#         f=0
#         for std in student:
#             print(std['adm_no'])
#             if std['adm_no']==adm:
#                 print("std",std)
#                 f=1
#                 newfee=int(input("enter new fee:"))
#                 std['fee']=newfee
#                 print("fee updated")
#         if f==0:
#             print("no record found")