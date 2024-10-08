# python operatorlari
"""
Arfmatetik operatorlar
O'zlashtirish operatorlar
Toqqoslash operatorlar
Mantiqiy operatorlar
Aniqlash opertorlar
A'zolik operatorlar
Bitli operatorlar
"""

# Arfmetik operatorlar
"""
+ Qo'shish x+y
- Ayirish x-y
* Ko'paytieish x*y
/ bo'lish x/y
% qoldiqli bo'lish x%y
// butunli bo'lish x//y
"""
x=int(input("butun son kiritilsin\t x="))
y=int(input("butun son kiritilsin\t y="))
s=x+y
a=x-y
k=x*y
b=x/y
q=x%y
bb=x//y
print(f"+ Qo'shish x+y={s}\n - Ayirish x-y={a}\n * Ko'paytieish x*y={k}\n / bo'lish x/y={b}\n % qoldiqli bo'lish x%y={q}\n // butunli bo'lish x//y={bb}")

# O'zlashtirish operatorlar
"""
=   x=5  x=5
+=  x+=5   x=x+5
-=   x-=5  x=x-5
*=  x*=5  x=x*5
/=  x/=5  x=x/5
%=  x%=5  x=x%5
//=  x//=5  x=x//5
**=  x**=5  x=x**5
"""
# songa o'zgartirish
x=int(input("butun son kiritilsin\t x="))
x=5 # x=5
print(x)

# kiritilgan sonni 5 qo'shib o'zlashtirish
x=int(input("butun son kiritilsin\t x="))
x+=5 # x=x+5
print(x)

# kiritish sonni 5 ayerib o'zgartirish
x=int(input("butun son kiritilsin\t x="))
x-=5 # x=x-5
print("x=x-5",x)

# kiritilgan sonni 2 ga ko'payterib o'zlashtirish 
x=int(input("butun son kiritilsin\t x="))
x*=2 # x=x*2
print("x=x*2",x)

# kiritilgan sonni 6 ga bo'lib  o'zlashtirish 
x=int(input("butun son kiritilsin\t x="))
x/=6 # x=x/6
print("x=x/6",x)

# kiritilgan sonni 6 ga butun bo'lib  o'zlashtirish 
x=int(input("butun son kiritilsin\t x="))
x//=6 # x=x//6
print("x=x//6",x)

# kiritilgan sonni 6 ga qoldiqli bo'lib  o'zlashtirish 
x=int(input("butun son kiritilsin\t x="))
x%=6 # x=x%6
print("x=x%6",x)



# Toqqoslash operatorlar
"""
== Teng x==y
!= Teng emas x!=y
>  Ketta x>y
< Kichik x<y
>= Katta yoki Teng x>=y
<= Kichik yoki ting x<=y
"""
x=int(input("x="))
y=int(input("y="))
print("==",x==y)
print("!=",x!=y)
print(">",x>y)
print("<",x<y)
print(">=",x>=y)
print("<=",x<=y)

# mantiqiy operatorlar
"""
and- agar ikki shart ham rost bo'lsa , True qaytaradi
or- kamida bitta shart rost bo'lsa True qaytaradi
not- Shar qiymatini teskariga o'girish yani True bo'lsa False Yoke False bo'lsa True
"""
x=int(input("x="))
y=int(input("y="))
print(x>y and x>0) # and x son y sna katta  bo'lsa va x son 0 dan katta bo'lsa True aks holda False 
print(x<y or  x>0) # or  x son y dan kichik bo'lsa yoke x son 0 dan katta bo'lsa 
print(not x>y) # x son y dan kichik bo'lsa True aks holda False

# Aniqlash operatorlar
"""
is- ikkila o'zgarovchi ham bir xil obekt bo'lsa True aks holda False
is not- obektlar bir xil bo'lmasa True aks holda False
"""
x=int(input("x="))
y=int(input("y="))
if x>0 is y>0:
    print(True)
else:
    print(False)

if x is not None: # x bo'sh bo'lmsa True aks holda False  
    print(" x son bo'sh  emas")

    
# A'zolik operatorlar
"""
in- belgilangan qiymat obektda mavjud bo'lsa True aks holda False
in not - belgilangan qiymat obektda mavjud bo'lmsa True aks holda False
"""
x=str(input(" so\'z kiring x="))
y=str(input("so\'z kiring y="))

if x in y:
    print(True)
else: 
    print(False)

# Bitle Operatorlar
"""
&(and)
|(or)
~(not)
"""
a=int(input("a="))
b=int(input("b="))
print(a&b)
print(a|b)
print(~(a>b))
