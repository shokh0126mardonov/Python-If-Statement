a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if (a + b > c) and (a + c > b) and (b +c > a):
 if a == b and b == c :
    print("Teng tomonli uchburchak")
 elif (a == b and b != c) or (a == c and c != b) or (c == b and b != a) :
    print("Teng yonli uchburchak")
 elif a != b and b != c :
     print("Turli tomonli uchburchak")
else :
    print("Uchburchak yasalish shartiga ko'ra bunaqa uchburchak yasab bo'lmaydi !!!")