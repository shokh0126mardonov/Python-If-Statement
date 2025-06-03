email = input("Emailingizni kiriting:").strip()

# bu yerga char ga "@" belgisi kiritiladi chunki hamma amallar shu "@" belgisi asosida amalga oshirilmoqda.
char  = input("Qidirayotgan belgingizni kiriting:")

if (char in email) and (email[len(char):(len(email)-len(char))].find(".") and (" " not in email)):
    print("Email manzili to'g'ri")
else :
    print("Email manzili noto'g'ri")