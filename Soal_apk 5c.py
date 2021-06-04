# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:37:21 2021

@author: Indrian Wahyu K - 20083000017
                  ---- STATUS NILAI ----
"""

#Input Status Nilai
print("---- STATUS NILAI ----")
Nilai = int(input ("Masukkan Nilai Anda : "))

#Read Nilai
if Nilai >=80:
    print ("Status : Baik Sekali")
elif Nilai >=65:
     print ("Status : Baik")
elif Nilai >=55:
    print ("Status : Cukup")
elif Nilai >=40:
    print ("Status : Kurang")
else:
    print("Status : Kurang Sekali")