def login(bank):
    username=input('enter username')
    password=input('enter password')
    f=0
    for bnk in bank:
        if bnk("username")==username and bnk("password")==password:
            print("bank",bnk)
            f=1
    return f,bnk
