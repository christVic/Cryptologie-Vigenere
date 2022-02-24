#!/usr/bin/python3
from chiffrement import chiffrer_texte
from cryptanalyseKasiski import cryptanalyse_kasiski

import string

alphabet=string.ascii_lowercase#+"0123456789"
print("************************************\nBienvenue dans le projet Vigenere\n************************************")
while True:
    print("************************************************************************")
    print("[1]Chiffrer un texte [2]Déchiffrer un texte [3]Cryptanalyser un texte par la méthode de Kasiski [4]Quitter")
    action=int(input("Que voulez-vous faire?(Saisissez le numero correspondant à l'action)\n>"))

    if action==1:
        chiffrer_texte(alphabet,True)
    elif action==2:
        chiffrer_texte(alphabet,False)
    elif action==3:
        cryptanalyse_kasiski()
    else:
        exit()
