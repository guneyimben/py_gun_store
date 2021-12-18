import os
import sys
from user import User
from weapons.rifle import Rifles
from weapons.smg import SMGs

os.system('mode con: cols=86 lines=40')
os.system("color a")


def main():       
    os.system("cls")
    print("======================================================================================")
    print("==                               GÜNEY SİLAHCILIK                                   ==")
    print("==                               Kullanıcı Girişi                                   ==")
    print("======================================================================================\n\n")
    username = input("          Kullanıcı Adı Giriniz: ")
    password = input("          Şifre Giriniz: ")
    user = User(username, password, True)
    isLoggedIn = user.Login()

    if isLoggedIn == True:
        while True:
            os.system("cls")
            print("======================================================================================")
            print("==                               GÜNEY SİLAHCILIK                                   ==")
            print("==                                   Envanter                                       ==")
            print("======================================================================================\n\n")
            print("         Lütfen görmek istediğiniz silahı seçiniz: \n")
            print("         1-) Kar98k")
            print("         2-) Uzi")
            print("         3-) M16A4")
            print("         4-) AWM")
            print("         5-) AK-47")
            print("         X-) Çıkış\n")
            choice = input("         Seçim Yapınız: ")
            os.system("cls")
            print("======================================================================================")
            print("==                               GÜNEY SİLAHCILIK                                   ==")
            print("==                                Bilgi Bankası                                     ==")
            print("======================================================================================")
            if choice == "1":
                Rifles.kar98k("New")
            elif choice == "2":
                SMGs.uzi("New")
            elif choice == "3":
                Rifles.m16a4("New")
            elif choice == "4":
                Rifles.awm("New")
            elif choice == "5":
                Rifles.ak47("New")
            elif choice == "X" or choice == "x":
                os.system("cls")
                sys.exit()
            else:
                print("\n\n         Hatalı Giriş!")
            print("\n")
            os.system("pause")
    else:
        os.system("pause")
        main()

main()



