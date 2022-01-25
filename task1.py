import re
dic={}
username=input("enter the user name:::")
pswrd=input("enter the password:::")
mail=input("enter the email id:::")
dic["User Name"]=username
dic["Password"]=pswrd
dic["Email Id"]=mail
u=re.search('^[A-Z][\w\d]',username)
p=re.search('[\d\w!@#$%^]',pswrd)
m=re.search('[a-z0-9]@[a-z0-9]',mail)
if u and username.isalnum():
     pass
else:
    print("invalid username")    
if p and len(pswrd)>=8:
    pass
else:
    print("invalid password")    
if m and mail.islower():
    pass
else:
    print("invalid email id")    
if u and p and m:
    print(dic)
    print("THIS IS YOUR USER ID::")
    print(username[:4]+pswrd[:4]+mail[:4])
	
