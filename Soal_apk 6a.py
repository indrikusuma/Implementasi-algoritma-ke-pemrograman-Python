# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:38:58 2021

@author: Indrian Wahyu K - 20083000017
                  ---- TRANSAKSI PEMBELIAN PRINTER EPSON T20 ----
"""
#Pengulangan Program
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("==============================================================")
    print("            TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
    print ("==============================================================")

    # Nilai awal variable JmlBeli = Harga 1 Printer
    HargaPrint = 660000
    # Input Jumlah Beli
    JmlBeli = input ("Masukkan Jumlah Printer Epson T20 Yang Dibeli = ")

    # Proses Hitung Total
    Total = int(HargaPrint)*int(JmlBeli)

    # Tampil
    print("Total Transaksi Pembelian Printer Epson T20   = Rp " + str (Total))

    #inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break