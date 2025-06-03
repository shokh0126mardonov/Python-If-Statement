month = int(input("Oyni raqamini kiriting:")) 

if 1 <= month <= 12: 
 if month>=3 and month<=5 :
    print("Bahor")
 elif month >=6 and month<=8 :
    print("Yoz")
 elif month >= 9 and month <=11 :
    print("Kuz")
 else :
    print("Qish")
else :
    print("Bir yil 12 oydan iborat siz noto'g'ri raqam kiritdingiz!")



