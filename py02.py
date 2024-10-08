a=input("baxoinggizni kiriting\ta=")

if int(a)==5:
    print("alo")
elif int(a)<5 and int(a)>=4:
    print("yaxshi")
elif int(a)<4 and int(a)>=3:
    print("qoniqarli")
elif int(a)>=2 and int(a)<3:
    print("yomon")
else:
    print("bunday baxo yo\'q!!")

# 3 xonali sonni raqamlar yig'indisi
b=int(input("100 dan 999 gacha son kiriting  b="))
if b<100 | b>999:
    print(" kiritilgan son 100 va 999 gacha bo'lichi kerak!!!")
else:
    print(b//100)
    print((b//10)%10)
    print(b%10)
    print("b sonni raqamlar yig\'indisi yig\'indisi \t",b//100+(b//10)%10+b%10)

    


