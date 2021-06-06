# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:16:05 2021

@author: Indrian Wahyu K - 20083000017
                  ---- PENENTUAN KELULUSAN ----
"""

#cek kelulusan, jika nilai > 60 maka status Lulus
Jawab = "y"
while Jawab=="y" or Jawab=="Y":
    print ("=========================")
    print(" CEK KELULUSAN ")
    print ("=========================")
    #setiap value yg diinputkan, secara default bertipe data STRING
    n = input(">> Masukkan Nilai = ")
    #cek nilai
    if int(n)>60:
        Status = "LULUS"
    else:
        Status="ULANG"
    print(Status)

    #inputan untuk break
    Jawab = input(">> Mulai lagi ? y/t = ")
    if Jawab== "t" or Jawab =="T":
        break