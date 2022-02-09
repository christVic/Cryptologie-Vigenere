#!/usr/bin/python3
import string

def chiffrement(alphabet,texte,cle,chiffrer):
    tailleCle = len(cle)
    if tailleCle>0:
        indexTexte = 0#le ième caractère du texte
        k = 1
        resultat = ""

        if not chiffrer:
            k = -1

        for caractere in texte:
            #cas où le caractere du texte est dans l'alphabet
            if caractere.lower() in alphabet:
                #on trouve le caractere de la clé à utiliser
                carCle=cle[indexTexte%tailleCle].lower()
                #cas où le caractere de la clé à utiliser est dans l'alphabet
                if carCle in alphabet:
                    #on trouve l'index du caractere de la clé à utiliser dans l'alphabet
                    indexCle = k*alphabet.index(carCle)+k
                    #on trouve l'index du caractere obtenu apres chiffrement
                    indexNewCar = (alphabet.index(caractere.lower())+indexCle)%len(alphabet)
                    if caractere.isupper():
                        resultat+=alphabet[indexNewCar].upper()
                    else:
                        resultat+=alphabet[indexNewCar]
                else:
                    resultat+=caractere
            #cas où le caractere du texte n'est pas dans l'alphabet
            else:
                resultat+=caractere
            indexTexte+=1

        return resultat

    return "Erreur: La clé de chiffrement ne peut pas etre vide!"

def chiffrerTexte(alphabet,chiffrer):
    if chiffrer:
        print("Chiffrer un texte\n*********************")
        texteInput="\tSaisissez le texte à chiffrer\n\t>"
        texteResultat="\tTexte chiffré"
        ftexte="texteAChiffrer.txt"
    else:
        print("Déchiffrer un texte\n**********************")
        texteInput="\tSaisissez le texte à déchiffrer\n\t>"
        texteResultat="\tTexte déchiffré"
        ftexte="texteChiffre.txt"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabetInput=input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabetInput:
        alphabet=alphabetInput

    cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")
    while not cle:
        cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    print("\t[0]Lire le fichier \"",ftexte,"\"\n\t[1]Saisir le texte\n\t")
    choix=int(input("\tQue choisissez-vous?\n\t>"))
    if choix==0:
        f=open(ftexte,"r")
        #à modifier
        texte=f.read().strip()
        f.close()
    else:
        texte=input(texteInput)

    resultat=chiffrement(alphabet,texte,cle,chiffrer)
    print(texteResultat,"\n\t>",resultat)
