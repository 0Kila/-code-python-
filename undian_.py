#undi
import sys
import os
from time import sleep
from random import randint

def awal():
    print("---------------------")
    print("Undian Acak Sederhana")

    acak = randint(0, 100)
    acak2 = randint(0, 100)
    
    nama1 = raw_input("Masukkan Nama Pertama>> ")
    print("---------------------")
    nama2 = raw_input("Masukkan Nama Kedua>> ")
    print("---------------------")
#    nama3 = raw_input("Masukkan Nama Ketiga>> ")
#    print("---------------------")

    if acak > acak2:
        hasil = "Nama Kamu %s " % nama1 ,"Kamu Disuruh Sama Mamah" # %s" % nama3
        print(hasil)
        sleep(0.5)
        pilih = raw_input("Apakah Anda Ingin Melanjutkan Permainan?(y/n): ")
        if pilih == "y":
            print("permainan dilanjutkan!")
            sleep(0.5)
            awal()
        elif pilih == "n":
            sleep(0.5)
            sys.exit()
        else:
            sys.exit()


     if acak < acak2:
         hasil = "Nama Kamu %s " % nama2 ,"Kamu Disuruh Sama Mamah" # %s" % nama3
         print(hasil)
         sleep(0.5)
         pilih = raw_input("Apakah Anda Ingin Melanjutkan Permainan?(y/n): ")
         if pilih == "y":
             print("permainan dilanjutkan!")
             sleep(0.5)
             awal()
         elif pilih == "n":
             sleep(0.5)
             sys.exit()
         else:
             sys.exit() 
    
awal()
