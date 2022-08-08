# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:58:13 2022

@author: HP
"""

#print("hello world")
#print(78559*84/54)
#print("telegram messenger")
#ism = "aleksandr"
#yosh = 33
#print(ism)
#print(yosh)
#ism = "muhammad"
#print(ism)
#a = 5
#b = 6
#c = (a+b)**2
#print(c)
#
#a = "hello world" 
#print(a)

#xabar = "are u stupid, man"
#print(xabar)
#radius = 5
#pi = 3.14159
#aylana_yuzi = (pi * radius)**2
#print(aylana_yuzi)
#print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
 
#ism = "otabek"
#shahar = "navoiy"
#tuman = "karmana"
#smayl = "😘"
#ism = "abdusattorjohn"
#print("mening ismim"  +' ' + ism)
#ism = "otabek"
#familiya = "razzoqov"
#print(ism + ' ' + familiya)
#ism_sharif = "{ism} {familiya}"

#ism = "jim"
#familiya = "carrey"
#print(f"salom, mening ismim {familiya}. {ism} {familiya} ")
#print("hello world")
#print("hello \tworld")
#print("hello \nworld")
#
#ism = "kehlani"
#sharif = "open"
#ism_sharif = f"{ism} {sharif}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

#meva = "   olma    "
#print(meva)
#print(" men " + meva.lstrip()+ " yaxshi ko'raman")
#print(" men " + meva.rstrip() +" yaxshi ko'raman" )
#print(" men " + meva.strip() + " yaxshi ko'raman")

#ism = input("ismingiz nima?\n__")
#print(" assalom alaykum , " + ism.capitalize())




#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
#print(kocha + " ko'changiz, " + mahalla + " mahallangiz, " + \
    #  tuman + " tumaningiz " + viloyat + " viloyatingiz")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
#print("Iltimos, quyidagi ma'lumotlarni kiriting:")
#kocha = input("Ko'changiz: ")
#mahalla = input("Mahallangiz: ")
#tuman = input("Tumaningiz: ")
#viloyat = input("Viloyatingiz: ")
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      #tuman + " tumani, " + viloyat + " viloyati")   

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
#print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
   #   tuman + " tumani,\n" + viloyat + " viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
#manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
#print(manzil.upper())
#print(manzil.lower())
#print(manzil.title())
#print(manzil.capitalize())

#a = 20
#b = 5.5
#temp = 36.6
#print(type(a))

#aholi_soni = 7_333_333_333
#print("AHOLINING SONI:", aholi_soni)

#x, y, z = 33, 22.5, -11
#c= x*y

#radius = 20
#PI = 3.14159
#diametr = 2*radius
#print("Aylana uzunligi = ", PI*diametr)

#ism = "Sobir"
#yosh = 44
#xabar = ism + ' ' + str(yosh) + '  '+ 'yoshda '
#print(xabar)

#t_yil = int(input("date:"))
#yosh = 2022 - t_yil
#print("siz", yosh)

#a =  int("10")
#b = float("10")
#emp = str(36.6)


#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
#x = int(input("Istalgan son kiriting:\n>>>"))
#print(x, " ning kvadrati ", x**2, " ga teng")
#print(x, " ning kubi ", x**3, " ga teng")

# Foydalanuvchining yoshini so'rang, 
# va uning tug'ilgan yilini hisoblab, konsolga chiqaring.
#yosh = int(input("Yoshingiz nechida? \n>>>"))
#t_yil = 2020-yosh
#print("Siz ", t_yil, " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, 
# kiritilgan sonlarning yig'indisi, ayirmasi, 
# ko'paytmasi va bo'linmasini chiqaruvchi dastur
#a = float(input("Birinchi sonni kiriting: "))
#b = float(input("Ikkinchi sonni kiriting: "))
#print(f"{a}+{b}=", a+b)
#print(f"{a}-{b}=", a-b)
#print(f"{a}x{b}=", a*b)
#print(f"{a}/{b}=", a/b)

#20.05.2022 

#fruits = ["apple", 'banana' , 'peach' , 'melon', 'grapes'] #words can be written
#prices = [5000 , 6000 , 7000 , 8000 , 9000] #numbers can be written 
#numbers = ["one" , "two" , "three" , 4 , 5] #numbers and words can be written
#names = [] #blank list

#fruits.append('qovun')
#fruits.insert(0, 'tarvuz')
#del fruits(0)
#fruits.remove('banana')
#thing = fruits.pop(0)

#23.05.2022

#putting things in order.

cars = ['lacetti', 'bugatti', 'bmw', 'mercedes-benz', 'tesla', 'tiko' , 'audi']
#sonlar = [1, 2, 22, 23, 31, 33, 34, 77, -11, -12, -13]
#sonlar.sort(reverse=True)
#print(sonlar)
#sorted(sonlar)
#print(sorted(sonlar))
#print(sonlar.sort(reverse=True))
#cars.reverse()
#print(cars)
#len(cars)
#uzunlik = len(sonlar)

#range(0,10)
#list(range(0,10))
#sonlar = list(range(0,10))
#print(sonlar)
#juft_sonlar = list(range(2,41,2))
#print(juft_sonlar)
#oq_sonlar = list(range(1,41,2))
#print(toq_sonlar)
#sanash = list(range(0,101,10))
#print(sanash)
#maximum_qiymat = max(toq_sonlar)
#print(maximum_qiymat)

#narxlar = [5600, 11000, 19000, 33000, 44000, 115000]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("eng arzon narx", arzon, "eng qimmat narx" , qimmat, "jami:", jami)

#print(cars[0:3])
#print(cars[2:5])
#print(cars[:4])
#print(cars[1:])

#my_cars = cars[:]
#print(my_cars)
#my_cars.remove('tesla')
#print(my_cars)

#toys = ("car", "lizard", "bear", "cat", "doggo")
#toys = list(toys)
#toys.append("chumoli")
#print(toys)
#toys = tuple(toys)
#print(toys)


#JUNE 20. 2022****************************************************************




#mehmonlar = ['ali' , 'vali' , 'hasan' , 'husan' , 'olim']
#for mehmon in mehmonlar:
#    print("salom", mehmon)
#    print("hayr", mehmon)


#mehmonlar = ['ali' , 'vali' , 'hasan' , 'husan' , 'olim']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon} sizni 11 avgust kuni majlisga taklif etamiz")
#    print("hurmat bilan thompsonlar oilasi\n")
    
    

#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")




#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#    
#    print(sonlar)
#    print(sonlar_kvadrati)


#dostlar = []
#print("5 ta eng yaqin dostingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-dostingizni ismini kiriting:"))
#print(dostlar)

###################### Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar = ['Ali','Vali','Hasan','Husan','Olim']
#for ism in ismlar:
#    print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
#print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#sonlar = list(range(11,100,2))
#for son in sonlar:
#    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5 ta sevimli kinoingiz qaysilar?")
#for k in range(5):
#    kinolar.append(input(f"{k+1}-kino:"))
#print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
#n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
#ismlar = []
#for n in range(n_people):
#    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
#print(ismlar)



#JULY 11, 2022 ***************************************************************


#avtolar = ['kia', 'hyundai', 'audi', 'bmw', 'volvo']
#for avto in avtolar:
#    print(avto.title())
    

#for avto in avtolar:
#    if avto == 'bmw':  #agar avto bmw ga teng bo'lsa
#        print(avto.upper())
#    else:
#        print(avto.title())
#
#ism = 'Ali'
#
#ism.lower() == 'ali' #kichik harflarda yozish
#a = 5
#a == 5 # a, 5 ga tengmi?
#a != 5 # a, 5 ga teng emasmi?



#ism = input('ismimgiz nima?\n>>>')   # foydalanuvchi ismini so'rash
#if ism.lower() != 'ali':   #agar ism ali ga teng bo'lmasa
#    print(f" uzr, {ism.title()} biz alini kutayapmiz")
#else:
#     print("salom, Ali")
    


#javob = float(input("12x6 nechiga teng?>>>"))    
#if javob !=72:
#     print("javobingiz xato")    
#else:
#     print("javobingiz to'g'ri")    
 



#yosh = int(input("Yoshingiz nechida?>>>"))   #integer = int butun son
#if yosh>=18: #yosh 18 dan katta yoki teng bo'lsa
#      print("Xush kelibsiz!")
#else:
#      print("kirish mumkin emas!")
      
 
#login = input('yangi login tanlang:') 
#if len(login)<=5:     #len= so'z uzunligi
#    print('login 5 ta belgidan koproq bolishi shart')
 

#yil = int(input("tug'ilgan yilingizni kiriting:"))
#if 2022-yil<18:
#    print(f"yoshingiz {2022-yil} da ekan.")
#    print("kirishingiz mumkin emas!")
#else:
#    print("Xush kelibsiz!")   



#yosh = int(input("yoshingizni kiriting:"))
#if yosh>65: print("siz COVID-19 risk guruhida ekansiz") 
#else: print(f"siz {2022-yosh} yilda tug'ilgan ekansiz va sizda covid yoq")


#x, y = 25, 50 #x=25, y =50
#print("x>y") if x>y else print("x<y")  #if va else ni bir qatorga joylash


#cars = ['toyota', 'hyundai', 'mazda', 'gm', 'kia']
#for car in cars:
#    print(car.title())
    
#for car in cars:
#   if car == 'gm':
#    print(car.upper())
#else: 
#    print(car.title())




#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#  if car=='gm':
#    print(car.upper())
#  else:
#    print(car.title())
#
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#  if car!='gm':
#    print(car.title())
#  else:
#    print(car.upper()) #
#
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
#login = input("Login kiriting: ")
#if login.lower() == 'admin':
#  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#  print(f"Xush kelibsiz {login.title()}!")
#
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting:"))
#if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
#son = float(input("Istalgan son kiriting:"))
#print("Son manfiy") if son<0 else print("Son musbat")


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
#son = float(input('Istalgan son kiriting: '))
#print(son**(1/2)) if son>0 else print('Musbat son kiriting')


#JULY12, 2022*****************************************************************

#son = float(input('ISTALGAN SONNI KIRITING:>>>'))
#if son<0:
#    print('MANFIY SON')
#elif son == 0:
#    print('son 0 ga teng')
#else:
#    print('MUSBAT SON') 
    
    
    
#yosh = int(input('yoshingiz nechida?'))
#if yosh<=4:
#    print('sizga kirish bepul')
#elif yosh<=12:   #YANGI SHART KIRITISH
#    print('sizga kirish 5000 uzs')
#elif yosh<=18:
#    print('sizga kirish 10000 uzs')
#else:
#    print('sizga kirish 15000uzs')
    
    
#yosh = int(input('yoshingiz nechida?>>>'))
#if yosh<=4:
#    narx = 0
#elif yosh<=12:
#    narx = 5000
#elif yosh<18:
#    narx = 1000
#else:
#    narx =15000
    
#print(f"SIZGA KIRISH {narx} UZS")    
    
#kun = input("BUGUN KUN NIMA?>>>")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba": # OR u yoki bu shartdan biri tog'ri bo'lsa
#
#    print('BUGUN DAM OLISH KUNI')
#else:
#    print("BUGUN ISH KUNI")

    
#kun = input("BUGUN KUN NIMA")
#harorat = int(input("HAVO HARORATI QANDAY?"))
#
#if kun.lower()=='yakshanba' and harorat>=30:  # AND ikkala shart tog'ri bo'lganda
#    print("CHO'MILGANI KETDIK!")
#elif kun.lower()=='yakshanba' and harorat<30:
#    print('uyda dam olamiz!') 
 
   
#kun = input("BUGUN KUN NIMA? ")
#harorat = int(input("BUGUN HARORAT QANDAY? "))
#
#if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#    print("CHO'MILGANI KETDIK!")
#elif (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<30:
#    print("uyda qolamiz!")    
#else:
#    print("ISHGA KETDIK!")

#narx = 15000 #MIJOZ 15000 UZS GA OSH SOTIB OLDI
#salat = True  #MIJOZ SALAT HAM OLDI ***MANTIQIY MA'LUMOT TURI
#choy = False  #MIJOZ CHOY OLMADI ***MANTIQIY MA'LUMOT TURI

#if salat and choy: #AGAR SALAT VA CHOY OLGAN BO'LSA
#    narx = narx + 1000
#elif salat or choy:
#   narx = narx + 5000 #AGAR SALAT YOKI CHOY SOTIB OLGAN BO'LSA
#    
#print(f"JAMI NARX {narx} UZS, HARIDINGIZ UCHUN RAHMAT!")
    
#narx = 15000  
#salat = True #1
#choy = False #0
#non = True   #1
#kompot = True   #1
#assorti = True   #0 

#QUYIDAGI HAR BIR SHART ALOHIDA TEKSHIRILADI VA BIR BIRIGA BOG'LIQ EMAS!
#if salat:
#    print("MIJOZ SALAT OLDI")
#    narx = narx + 3000
#if choy:
#    print("MIJOZ CHOY OLDI")
#    narx = narx + 4000
#if non:
#    print("MIJOZ NON SOTIB OLDI")
#    narx = narx + 5000
#if kompot:
#    print("MIJOZ KOMPOT SOTIB OLDI")
#    narx = narx + 6000
#if assorti:
#    print("MIJOZ ASSORTI SOTIB OLDI")
#    narx = narx  +7000
#   
#print(f"jami {narx} UZS")
    
#menu = ['osh', 'manti', 'qozonkabob', 'shashlik', 'somsa', 'norin']
#ovqat = input("NIMA TAOM XOXLAYSIZ?")
#if ovqat.lower() in menu:  #AGAR OVQAT MENYU TARKIBIDA BO'LSA
#    print("BUYURTMA QABUL QILINDI!")
#else:
#    print("AFSUSKI BIZDA BUNDAY TAOM YO'Q")
#    
#menu = ['osh', 'manti', 'qozonkabob', 'shashlik', 'somsa', 'norin']
#ovqat = input("NIMA TAOM XOXLAYSIZ?")
#f ovqat.lower() not in menu:  #AGAR OVQAT MENYU TARKIBIDA BO'LSA
#
#   print("AFSUSKI BIZDA BUNDAY TAOM YO'Q!")
#else:
#    print("BUYURTMA QABUL QILINDI")
    
#IKKITA RO'YXATNI BIR-BIRI BILAN SOLISHTIRISH
#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

#if buyurtmalar: #MENYUDA ELEMENTLAR BOR YO'QLIGINI TEKSHIRISH
#    for taom in buyurtmalar:
#        if taom in menu:
#         print(f"MENYUDA {taom} BOR")
#    else:
#       print(f"uzr, menyuda {taom} yo'q")
#else:
#    print('SAVATCHANGIZ BOSH')

    
#son = float(input("Juft son kiriting: "))
#if son%2:
#    print('Bu son juft emas.')
#else:
#    print("Rahmat!") 

#son = float(input('toq sonni kiriting:'))  
#if son%3:
#    print('TRUE')
#else:
#    print('FALSE')   


#yosh = int(input("YOSHINGIZ NECHIDA?>>>")) 
#if yosh<=4 or yosh>=60:
#    print('SIZGA KIRISH BEPUL')
#elif yosh>4 and yosh<18:  print('KIRISH 15000 UZS')  
#elif yosh>=18 and yosh<60: print('SIZGA KIRISH 20000 UZS')  

#x = int(input("BIRINCHI SONNI KIRITING: "))
#y = int(input("IKKINCHI SONNI KIRITING: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")


#y = int(input("BIRINCHI SONNI KIRITING: "))
#z = int(input("IKKINCHI SONNI KIRITING: "))
#if y==z: print(f"{z}={y}")
#elif y>z: print(f"{z}<{y}")
#else:     print(f"{z}>{y}") 

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q")



#son = int(input("Istalgan butun son kiriting: "))
#
#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")




#12 DARS                             29.07.2022          

#yosh = int(input("YOSHINGIZNI KIRITING:>>>"))
#if yosh <= 18:
#    print('sizga kirish 15000uzs')
#elif yosh == 18:
#    print('sizga kirish 20000uzs')
#elif yosh > 18:
#    print('sizga kirish 25000uzs')

 
#print('45 gacha sanaymiz:')
#for n in range(45):
#    print(n+1)
#    
#son = int(input('istalgan sonni kiriting: '))    
#print(f"{son} ning kvadrati {son**2}ga teng" )

#mevalar = ['olma','shaftoli']
#for meva in mevalar:
#    print(meva)

#13 DARS                            01.08.2022
#GITHUB



#14DARS                             02.08.2022

#car_0 = {'model' : 'ferrari','rang' : 'qizil'}  #lug'at   kalit:qiymat 
#print(car_0['model'])
#print(car_0['rang'])


#eng_uz = {'apple' : 'olma', 'apricot': 'orik', 'banana' : 'banan'}
#print(eng_uz)
#print(eng_uz['apple'])
#print(eng_uz['apricot'])
#print(eng_uz['banana'])

#mevalar = {'olma': 10000, 'tarvuz': 8000, 'qovun': 10000}
#print(f"olmaning narxi {mevalar['olma']} uzs")

# lug'atlarda qiymat turli shaklda bo'lishi mumkin.(matn,son)
#talaba_0 = {'ism' : 'razzoqov otabek', 'yoshi' : 26, 'tugilgan yili': 1996}
#print(f"{talaba_0['ism'].title()},\
#      {talaba_0['tugilgan yili']}-yilda tugilgan\
#          {talaba_0['yoshi']} yoshda")

#YANGI KALIT SO'Z VA QIYMAT QO'SHISH
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = 'informatika'
#print(talaba_0)
#talaba_0['ism'] = 'elbek'
#print(talaba_0)

#bo'sh lug'at yaratish

#talaba_1 = {}
#talaba_1['ism'] = 'elbek razzoqov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 20
#print(talaba_1)
#print(f" Talaba {talaba_1['ism'].title()}\
#     {talaba_1['yosh']}-yoshda")
      
#QIYMATNI YANGILASH

#talaba_1['yosh'] = 21
#print(f" Talaba {talaba_1['ism'].title()}\
#      {talaba_1['yosh']}-yoshda")
      
#KALIT SO'Z QIYMATNI O'CHIRIB TASHLASH
#talaba_0 = {'ism' : 'razzoqov otabek', 'yoshi' : 26, 'tugilgan yili': 1996}
#print(talaba_0)
#del talaba_0['yoshi']  #istalgan elementni kalit so'zi yordamida o'chirish
#print(talaba_0)

#eng_uz = {'apple' : 'olma', 'apricot': 'orik', 'banana' : 'banan'}
#print(eng_uz)
#del eng_uz['apple']
#print(eng_uz)

#LUG'ATNI BIR NECHTA QATORDA YOZISH
#telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#   }
#print(telefonlar['ali'])



#get() metodi


#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")

#phone = telefonlar['hasan']
#print(f"Hasanning telefoni {phone}")
#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)

#phone = telefonlar.get('hasan')
#print(phone)


#15DARS                    03.08.2022

#LUG'ATLAR BILAN ISHLASH

# .items()
#talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
#
#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")





#telefonlar = {
#     'ali':'iphone x',
#    'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'elbek' : 'samsung galaxy A31' ,
#     'orif':'nokia 3310'
#     }

#for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")






# # .keys()
#mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

#print(mahsulotlar.keys())
#
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
#
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar:
#     print(mahsulot.title())
#
#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
         
         
         
         
         
         
        
# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# print("Do'konimizdagi mahsulotlar:")    
# for mahsulot in sorted(mahsulotlar): #LUG'AT ICHIDAGI ELEMENTLARNI TAXLASH ALIFBO TARTIBIDA
#     print(mahsulot.title())
    








# # .values()  #LUG'ATLARDAN FAQAT QIYMATLAR OLINADI
#print(telefonlar.values())

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#     print(tel)


# # set  #ELEMENTLARNI TAKRORLAMAGAN HOLDA

#telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#     print(tel)
    
# # set
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#     print(tel)

#toys = {"ball","car","lamp","ball"}


#python_words = {
#    'integer':'Butun son',
#    'float': "O'nlik son",
#    'boolean':"Mantiqiy qiymat",
#    'for':"Biror amalni qayta-qayta bajarish tsikli",
#    'if':'Shartlarni tekshirish operatori'}
#
#for key, value in sorted(python_words.items()):
#    print(f"{key.title()} - {value}")
    
    
    
    
    
#davlatlar = {
#    "o'zbekiston":'toshkent',
#    'aqsh':'washington d.c.',
#    'rossiya':'moskva',
#    'tojikiston':'dushanbe',
#    "qirg'iziston":'bishkek',
#    'qozog\'iston':'nursulton',
#    'malayziya':'kuala-lumpur',
#    'singapur':'sungapur',
#    'italiya':'rim'}

#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
#    print(davlat.upper())

#print('\nDavlatlarning poytaxtlari')
#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.title())

#country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
#capital = davlatlar.get(country)
#if capital==None:
#    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
#else:
#    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")




#menu = {
#        'osh':20000,
#        "lag'mon":22000,
#        'non':4000,
#        'choy':5000,
#        'shashlik':12000,
#        'somsa':6000,
#        'tabaka':15000
#        }

#print('3 ta taom buyurtma bering.')
#buyurtmalar = []
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-taom:").lower())
#
#for buyurtma in buyurtmalar:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz, bizda {buyurtma} yo'q.")







#16DARS               05.08.2022
#LUG'ATLAR RO'YXATI

#car0 = {
#        'model':'lacetti',
#        'rang':'oq',
#        'yil':1999,
#        'narx':13000,
#        'km':50000,
#        'korobka':'avtomat'
#        }

#car1 = {
#        'model':'nexia 3',
#        'rang':'qora',
#        'yil':2015,
#        'narx':9000,
#        'km':89000,
#        'korobka':'mexanika'
#        }

#car2 = {
#        'model':'gentra',
#        'rang':'qizil',
#        'yil':2019,
#        'narx':15000,
#        'km':20000,
#        'korobka':'mexanika'
#        }


#car = car0
#print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

#car = car1
#print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

#car = car2
#print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")
#  
#cars = [car0, car1, car2]
#for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narx']}$")

#print(cars[0]['model'])
#
#print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")
#
#print(f"{cars[0]['rang'].capitalize()}")
#print(f"{cars[2]['km']*22}")







#malibus=[]
#for n in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None, # rangi noaniq
#        'yil':2020,
#        'narh':None,
#        'shina' : 19,
#        'km':0,
#       'korobka':'avto'
#        }
#    malibus.append(new_car)
#
#for malibu in malibus:
#     print(malibu)

#for malibu in malibus[:3]:
#    malibu['rang']='qizil'

#for malibu in malibus:
#   print(malibu)

#for malibu in malibus[3:6]:
#    malibu['rang']='qora'

#for malibu in malibus:
#     print(malibu)

#   malibu['rang']='qora'
#   malibu['korobka']='mexanika'

#for malibu in malibus:
#     print(malibu)
     
#for malibu in malibus[:10]:
#    malibu['shina']=20
    
#for malibu in malibus:
#    print(malibu)    
         
     

#for malibu in malibus:
#    if malibu['korobka']=='avto':
#        malibu['narh']=40000
#    else:
#        malibu['narh']=35000
#    
#for malibu in malibus:
#    print(malibu)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')
    
    
    
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())    