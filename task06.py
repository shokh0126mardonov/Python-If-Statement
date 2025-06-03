number = input("telefon raqamingizni kiriting>>")
code = number[4:6]

if number[:4] == '+998' and len(number) == 13:
    if code == '95' or code == '97':
        print("Uzmobile")
    elif code == '90' or code == '91':
        print("Ucell")
    elif code == '93' or code == '94':
        print("Beeline")
    elif code == '88' or code == '99':
        print("Mobiuz")
    else :
        print("Bunaqa raqam mavjud emas")

code = number[:2]

if code == '95' or code == '97':
    print("Uzmobile")
elif code == '90' or code == '91':
    print("Ucell")
elif code == '93' or code == '94':
    print("Beeline")
elif code == '88' or code == '99':
    print("Mobiuz")
else :
    print("Bunaqa raqam mavjud emas")


        