from numbers import numbers
from addition import add
from  substration import sub
from multiplication import mul
from division import div
while True:
    print("""
1.addition
2.substration
3.multiplication
4.division""")
    ch=int(input("enter your choice:"))
    if ch==1:
        a,b=numbers()
        add(a,b)
    elif ch==2:
        a,b=numbers()
        sub(a,b)
    elif ch==3:
        a,b=numbers()
        mul(a,b)
    elif ch==4:
        a,b=numbers()
        div(a,b)
    else:
        print("invalid choice")


    

    