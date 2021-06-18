"""
Created on Thu Jun 17 13:25:00 2021

@author: Indrian Wahyu K - 20083000017
UTS - ALGORITMA
SEMESTER 2
"""

#import waktu (tanggal dan jam)
import datetime


JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("========================================================================")
    print("                          TOKO BANGUNAN UD ")
    print("                   TRANSAKSI BIAYA BAHAN BANGUNAN ")
    print("========================================================================")
    waktu = datetime.datetime.now()
    print("Tanggal / Jam Transaksi : " , waktu)
    print(" ")
    print("                    >>> DAFTAR BAHAN BANGUNAN <<<")
    print("             a : Asbes Gelombang             @ Rp 60.000")
    print("             b : Cat Tembok Dulux 1Galon     @ Rp250.000")
    print("             c : Cat Tembok Avian 1 Galon    @ Rp350.000")
    print("             d : Aquaproof 5 Kg              @ Rp 50.000")
    print("             e : Seng 2mm                    @ Rp 70.000")
    print("             f : Spandeks 1mm                @ Rp 92.000")
    print(" ")
#Nilai Awal
    kode =['a','b','c','d','e','f']
    BhnBngunan = ['Asbes Gelombang ','Cat Tembok Dulux 1Galon', 'Cat Tembok Avian 1 Galon', 'Aquaproof 5 Kg', 'Seng 2mm', 'Spandeks 1mm']
    HrgSat = [60000,250000,350000,50000,70000,92000]
    persenDiskon = 0.05
    ppn = 0.02
    minDiskon =  500000
    TotalAwal = 0
    NilaiDiskon = 0

    #Input kode Bahan Bangunan
    pilihan = input(">> Masukkan Kode Bahan Bangunan yang dibeli   = ")    

    #identifikasi Indeks list berdasarkan pilihan
    idx = 0
    while idx < len(kode):
        if kode[idx] == pilihan:

            print(">> Pilihan Bahan Bangunan                     = " + BhnBngunan[idx])
            print(">> Harga Bahan Bangunan                       = Rp " + str (HrgSat[idx]))

            
    #Hitung Total Awal
            Qty = int(input(">> Masukkan Jumlah Bahan Bangunan yang dibeli = "))
            
            if Qty > 0:
                TotalAwal = HrgSat[idx] * int(Qty)
                print(">> Total Awal                                 = Rp " + str (TotalAwal))
            
            ppn = 0.02 * HrgSat[idx] * Qty
            print(">> PPN 2%                                     =     " + str (ppn))
            
    #Cek Nilai Diskon
            if (TotalAwal) > minDiskon:
                NilaiDiskon = int(TotalAwal) * float(persenDiskon)
                print(" Selamat Anda Mendapat Diskon 5% karena Pembelanjaan diatas Rp 500.000")
                print(">> Nilai Diskon                               =     " + str (NilaiDiskon))
                
            else: 0

    #Total Bayary
            TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
            print(">>> Total yang harus dibayarkan               = Rp " + str (TotalBayar))
            print()
            print("========================================================================")
            
        idx = idx + 1

    #inputan untuk break
    print(" ")
    print(" ^^ Note : Masukkan Kode Bahan Bangunan yang tertera ^^")
    JawabUlang = input(">>> Apakah Anda ingin melakukan transaksi lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break