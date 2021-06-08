"""
Cek golongan usia menggunakan loop
- loop cek inputan range usia harus >0-100
- loop run program (ok)
"""
#Cek Golongan Usia
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print ("=========================")
    print("    CEK GOLONGAN USIA ")
    print ("=========================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Usia : ")
        #cek batasan inputan usia 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts="GOLONGAN USIA : LANSIA"
            elif int(u)>=35: sts="GOLONGAN USIA    : DEWASA"
            elif int(u)>=18: sts="GOLONGAN USIA    : PEMUDA"
            elif int(u)>=15: sts="GOLONGAN USIA    : REMAJA"
            else:
                sts="GOLONGAN USIA    : ANAK"
            print (sts)

            JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
            if JawabUlang=="t" or JawabUlang=="T":
                break
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break