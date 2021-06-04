# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:38:58 2021

@author: Indrian Wahyu K - 20083000017
                  ---- TRANSAKSI PEMBELIAN PRINTER EPSON T20 ----
"""
# Nilai awal variable JmlBeli = Harga 1 Printer
HargaPrint = 660000

# Input Jumlah Beli
print("---- TRANSAKSI PEMBELIAN PRINTER EPSON T20 ----")
JmlBeli = input ("Jumlah Printer Epson T20 Yang Dibeli = ")

# Proses Hitung Total
Total = int(HargaPrint)*int(JmlBeli)

# Tampil
print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
