# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:47:27 2021

@author: Indrian Wahyu K - 20083000017
                  ---- KATEGORI NILAI ----
"""

#cek Kategori nilai
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("==================================")
    print("        CEK KATEGORI NILAI ")
    print ("==================================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Nilai    = ")
        #cek batasan inputan nilai 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=91: 
                sts="Kategori Penilaian   = A"
            elif int(u)>=81: sts="Kategori Penilaian   = B"
            elif int(u)>=71: sts="Kategori Penilaian   = C"
            else:
                sts="Kategori Penilaian = D"
            print (sts)

            JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t = ")
            if JawabUlang=="t" or JawabUlang=="T":
                break
        else:
            pesan=">>> Masukkan Nilai 0-100 saja"
            print(pesan)
            break