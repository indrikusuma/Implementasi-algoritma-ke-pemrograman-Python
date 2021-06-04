# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:47:27 2021

@author: Indrian Wahyu K - 20083000017
                  ---- KATEGORI NILAI ----
"""

#Input Kategori Nilai
print("---- KATEGORI NILAI ----")
Nilai = int(input ("Masukkan Nilai Anda : "))

#Read Nilai
if Nilai >=91 and Nilai <=100:
    print ("Kategori Penilaian : A")
elif Nilai >=81 and Nilai <=91:
     print ("Kategori Penilaian : B")
elif Nilai >=71 and Nilai <=81:
    print ("Kategori Penilaian : C")
else:
    print("Kategori Penilaian : D")