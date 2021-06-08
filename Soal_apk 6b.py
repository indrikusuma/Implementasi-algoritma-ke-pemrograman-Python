# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:16:05 2021

@author: Indrian Wahyu K - 20083000017
    ---- TRANSAKSI PEMBELIAN PRINTER EPSON T20 (Include Diskon) ----
"""
#Pengulangan Program
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("==============================================================")
    print("     TRANSAKSI PEMBELIAN PRINTER EPSON T20 (Include Diskon) ")
    print ("==============================================================")

    #Nilai Awal
    minDiskon = 1500000
    persenDiskon = 0.15
    HrgSat = 660000
    TotalAwal = 0
    NilaiDiskon = 0

    #Hitung Total Awal
    print ("---- TRANSAKSI PEMBELIAN PRINTER EPSON T20 (Include Diskon) ----")
    Qty = int(input("Masukkan Jumlah Printer yang dibeli = "))
    if Qty > 0:
        TotalAwal = int(HrgSat) * int(Qty)
        print("Total Awal                          = Rp " + str (TotalAwal))
    else:
            print("Cek kembali jumlah Printer yang dibeli")
        
    #Cek Nilai Diskon
    if (TotalAwal) > minDiskon:
        NilaiDiskon = int(TotalAwal) * float(persenDiskon)
        print("Nilai Diskon                        =     " + str (NilaiDiskon))
    else:0

    #Total Bayar
    TotalBayar = int(TotalAwal) - int(NilaiDiskon)
    print("Total yang harus dibayarkan         = Rp " + str (TotalBayar))

    #inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break