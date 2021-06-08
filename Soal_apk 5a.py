# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:16:05 2021

@author: Indrian Wahyu K - 20083000017
    ---- CEK KELULUSAN ----
"""
#cek kelulusan, jika nilai > 60 maka status Lulus
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("=================================")
    print("           CEK KELULUSAN ")
    print ("=================================")
    #setiap value yg diinputkan, secara default bertipe data STRING
    n = input(">> Masukkan Nilai = ")
    #cek nilai
    if int(n)>60:
        sts = "Keterangan        = LULUS"
    else:
        sts = "Keterangan        = ULANG"
    print(sts)

    #inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break