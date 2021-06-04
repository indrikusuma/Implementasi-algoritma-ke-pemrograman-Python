# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:16:00 2021

@author: Indrian Wahyu K - 20083000017
                  ---- KATEGORI USIA ----
"""

#Input Usia
print("---- KATEGORI USIA ----")
Usia = int(input ("Masukkan Usia Anda : "))

#Read Usia
if Usia >=60:
    print ("Status : Lansia")
elif Usia >=35 and Usia <=59:
     print ("Status : Dewasa")
elif Usia >=18 and Usia <=34:
    print ("Status : Pemuda")
elif Usia >=15 and Usia <=17:
    print ("Status : Remaja")
else:
    print("Status : Anak")