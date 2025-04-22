def register(bank):
    if len (bank)==0:
        bnk=1
    else:
        bnk=bnk[-1]["bank_id"]+1
    username=input("enter user_name")
    accountno=int("enter accountno")
    phn_no=int("enter phn_no")
    email=input("enter email")
    password=input("enter password")
    balance_amount=1000
    bank.append({'bank_id':bnk,'username':username,'accountno':accountno,'phno':phn_no,'email':email,'password':password,'balnce':1000})