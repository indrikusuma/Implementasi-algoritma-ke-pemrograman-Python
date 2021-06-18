"""
Created on Thu Jun 17 08:45:05 2021

@author: Indrian Wahyu K - 20083000017
UTS - ALGORITMA
SEMESTER 2
"""

#import waktu (tanggal dan jam)
import datetime

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==========================================================================")
    print("                             BENGKEL MOTOR UD ")
    print("                           TRANSAKSI BIAYA OLI ")
    print("==========================================================================")
    waktu = datetime.datetime.now()
    print("Tanggal / Jam Transaksi : " , waktu)
    print(" ")
    print("                           >>> DAFTAR OLI <<<")
    print("                 a : Duration SW20 1L        @ Rp53.000")
    print("                 b : Castrol Magnatec 1L     @ Rp50.000")
    print("                 c : Federal Supreme XX 1L   @ Rp54.000")
    print("                 d : Yamalube 1L             @ Rp45.000")
    print("                 e : Shell 1L                @ Rp46.000")
    print(" ")
#Nilai Awal
    kode =['a','b','c','d','e']
    oli = ['Duration SW20 1L','Castrol Magnatec 1L', 'Federal Supreme XX 1L', 'Yamalube 1L', 'Shell 1L']
    HrgSat = [53000,50000,54000,45000,46000]
    persenDiskon = 0.05
    ppn = 0.01
    minDiskon =  200000
    TotalAwal = 0
    NilaiDiskon = 0

    #Input kode OLI
    pilihan = input(">> Masukkan Kode Oli Oli yang dibeli      = ")    

    #identifikasi Indeks list berdasarkan pilihan
    idx = 0
    while idx < len(kode):
        if kode[idx] == pilihan:

            print(">> Pilihan Oli                            = " + oli[idx])
            print(">> Harga Oli                              = Rp " + str (HrgSat[idx]))

            

    #Hitung Total Awal
            Qty = int(input(">> Masukkan Jumlah Oli yang dibeli        = "))
            
            if Qty > 0:
                TotalAwal = HrgSat[idx] * int(Qty)
                print(">> Total Awal                             = Rp " + str (TotalAwal))
            
            ppn = 0.01 * HrgSat[idx] * Qty
            print(">> PPN 1%                                 =      " + str (ppn))
            
    #Cek Nilai Diskon
            if (TotalAwal) > minDiskon:
                NilaiDiskon = int(TotalAwal) * float(persenDiskon)
                print(" Selamat Anda Mendapat Diskon 5% karena Pembelanjaan diatas Rp 200.000")
                print(">> Nilai Diskon                           =     " + str (NilaiDiskon))
                
            else: 0

    #Total Bayary
            TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
            print(">>> Total yang harus dibayarkan           = Rp " + str (TotalBayar))
            print()
            print("==========================================================================")
            
        idx = idx + 1

    #inputan untuk break
    print(" ")
    print(" ^^ Note : Masukkan Kode Oli yang tertera ^^")
    JawabUlang = input(">>> Apakah Anda ingin melakukan transaksi lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break