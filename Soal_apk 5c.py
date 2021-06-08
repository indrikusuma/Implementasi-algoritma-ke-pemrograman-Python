# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:37:21 2021

@author: Indrian Wahyu K - 20083000017
                  ---- STATUS NILAI ----
"""

#cek status nilai
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("================================")
    print("        CEK STATUS NILAI ")
    print ("================================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Nilai = ")
        #cek batasan inputan nilai 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=80: 
                sts="Status            = Baik Sekali"
            elif int(u)>=65: sts="Status           = Baik"
            elif int(u)>=55: sts="Status           = Cukup"
            elif int(u)>=40: sts="Status           = Kurang"
            else:
                sts="Status            = Kurang Sekali"
            print (sts)

            JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
            if JawabUlang=="t" or JawabUlang=="T":
                break
        else:
            pesan=">>> Masukkan Nilai 0-100 saja"
            print(pesan)
            break