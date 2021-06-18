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
    print("================================================================")
    print("                     EKSPEDISI LORENA MALANG ")
    print("                    TRANSAKSI BIAYA EKSPEDISI ")
    print("================================================================")
    waktu = datetime.datetime.now()
    print("Tanggal / Jam Transaksi : " , waktu)
    print(" ")    
    print("                       >>> DAFTAR KOTA <<<")
    print("                         a : Surabaya")
    print("                         b : Bandung")
    print("                         c : Semarang")
    print("                         d : Denpasar")
    print(" ")

#Looping
    kode =['a','b','c','d']
    kota = ['Surabaya','Bandung', 'Semarang', 'Denpasar']
    jarak = [169,452,385,215]
    ongkirperkm = [2500,4000,3500,4500]

    pilihan = input(">> Masukkan Kode Tujuan = ")

#Identifikasi Indeks list berdasarkan pilihan
    idx = 0
    while idx < len(kode):
        if kode[idx] == pilihan:

            print(">>> Pilihan Tujuan      = " + kota[idx])
            print(">>> Jarak               = " + str(jarak[idx]) + " km")
            print(">>> Ongkir per Km       = Rp. " + str(ongkirperkm[idx]))
#Proses perhitungan biaya
            ongkir = jarak[idx] * ongkirperkm[idx]
#Menampilkan biaya kirim
            print(">>>> Total              = Rp. " + str(ongkir))
            print(" ")
            print("================================================================")
        idx = idx + 1 
        
#Inputan untuk break
    print(" ")
    print(" ^^ Note : Masukkan Kode Kota yang tertera ^^")
    JawabUlang = input(">>> Apakah Anda ingin melakukan transaksi lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break