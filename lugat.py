# car_1 ={'model':'jentra','rang':'qora','yil':'2024'}
# print(car_1['model'],car_1['rang'],car_1['yil'])

# mevalar={'olma':'10000','qovun':'20000','tarvuz':'50000'}
# print(f"olmani narxi{mevalar['olma']}so`m")

# talaba={'ism':"avazov olimjon",'yosh':25,'t_yil':2000}
# print(f"{talaba['ism'].title()},\
#       {talaba['t_yil']}-yilda tugilgan\
#         {talaba['yosh']}yoshda")
# talaba['kurs']=1
# talaba['fakultet']='Intelektuala tizimlar'
# talaba['yunalish']='suniy entelekt'
# talaba['ism']='Abdulloh'
# print(talaba)


# talaba = {}
# talaba['ism']="ehsmatov toshmat"
# talaba['yoshi']=20
# talaba['kurs']=2
# print(talaba)
# #print(f"talaba{talaba['ism'].title()} {talaba['kurs']} kursda {talaba['yoshi']} yoshda")
# talaba['kurs']=5
# print(f"talaba{talaba['ism'].title()} {talaba['kurs']} kursda {talaba['yoshi']} yoshda")

# talaba_1={'isim':'murod eshmatov','yosh':20,'t_yil':2000}
# #print(talaba_1)
# del talaba_1['t_yil']
# print(talaba_1)



#lugatlarni bi nechra qatorlarga yozish
telefonlar={
    'Rsad':'Redmi',
    'Jurabek':'Samsung',
    'Marjona':'Iphone',
    'Dilso`z':'Iphone15'
}
# get metod
tel=telefonlar['Dilso`z']
#print(f"Dilso`zni telefoni :{tel}")
tel=telefonlar.get('hasan','Bunday isim mavjud emas')
print(tel)