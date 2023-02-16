#12.02.2023
#modullar

#modullarni import qilishning usullari quyidagilar:

import avto_info_mod           #avto_info_mod faylini (modulini) chaqiramiz

avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)



#import avto_info_mod as aim    #avto_info_mod ni qisqa nom aim bilan chaqiramiz

#avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#aim.info_print(avto1)



#from avto_info_mod import avto_info, info_print

#avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#info_print(avto1)



#from avto_info_mod import avto_info as ainfo, info_print as iprint

#avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
#iprint(avto1)


import math  # math modulini import qilish 

x=400
print(math.sqrt(x))  # sqrt() qavs ichidagi sonning ildizini chiqarish funksiyasi
print(math.sqrt(9))


x = 2
y = 3
print(pow(x,y)) # pow funksiyasi x ning y - darajasini qaytaradi.
                # bunda math modulini bir marta import qilish yetarli
                
from math import pi # bunda math modulidagi pi o'zgaruvchisi import qilinadi
print(pi)                

#https://docs.python.org/3/library/math.html#module-math