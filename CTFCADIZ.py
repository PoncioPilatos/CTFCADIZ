#!/usr/bin/env python

import os
import time
from time import sleep

def Main():
    print("\033[93m--------------------------------------------")
    print("                CTFCADIZ v1.0                   ")
    print("   The best CTF toolkit made in Cadiz city   ")
    print("                           @PoncioPilatos  ")
    print("--------------------------------------------")
    print("\n[✓1]  Steganography")
    print("[✓2]  Forense")
    print("[✓3]  Reversing")
    print("[✓4]  OSINT")
    print("[✓5]  Cryptography")
    print("[✓6]  Web")
    print("\n[✓99]  Exit")
    Menu1()


def Menu1():
    category = int(input("\nSelect a category: "))
    if category == 1:
        StegoMenu()
    elif category == 2:
        ForenseMenu()
    elif category == 3:
        ReversingMenu()
    elif category == 4:
        OsintMenu()
    elif category == 5:
        CryptoMenu()
    elif category == 6:
        WebMenu()
    elif category == 99:
        os.system('clear')
        print("Goodbye my friend :(")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Select a valid option :)")
        sleep(1)
        os.system('clear')
        Main()