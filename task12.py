from getpass import getpass
pasword = getpass("Parolni kiriting:")
pasword1 = getpass("Parolni qayta kiriting:")
if pasword == pasword1 :
    print("Password is correct")
else :
    print("Password error")