#!/usr/bin/python3
import string
import re

def chiffrement(alphabet,texte ,chiffrer, cle):
    """
        Chiffre/Dechiffre un texte par la méthode de Vigenere

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - texte (string) : le texte à chiffrer/dechiffrer
            - cle (string) : la clé utilisée pour chiffrer/dechiffrer le texte
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (string) : le texte obtenu après le chiffrement/dechiffrement
    """
    # on supprime toutes les ponctuations et les espaces
    texte = re.sub(r'[^\w\s]','',texte)
    texte = texte.replace(" ","")
    cle = re.sub(r'[^\w\s]','',cle)
    cle = cle.replace(" ","")

    taille_cle = len(cle)

    # le ième caractère du texte
    index_caractere_courant_texte = 0

    resultat = ""

    for caractere_texte in texte:
        if caractere_texte.lower() in alphabet:
            # on trouve le caractere de la clé à utiliser
            caractere_cle = cle[index_caractere_courant_texte%taille_cle].lower()

            # cas où le caractere de la clé à utiliser est dans l'alphabet
            if caractere_cle in alphabet:
                # on recupere l'index du caractere_cle et du caractere courant du texte  dans l'alphabet
                index_caractere_cle = alphabet.index(caractere_cle)
                index_caractere = alphabet.index(caractere_texte.lower())

                # on calcule l'index du nouveau caractere obtenu apres chiffrement
                if chiffrer == True:
                    index_nouveau_caractere = (index_caractere+index_caractere_cle)%len(alphabet)
                else:
                    index_nouveau_caractere = (index_caractere-index_caractere_cle)%len(alphabet)

                # cas où le caractere du texte est une lettre majuscule
                if caractere_texte.isupper():
                    resultat+=alphabet[index_nouveau_caractere].upper()
                else:
                    resultat+=alphabet[index_nouveau_caractere]
            else:
                resultat += caractere_texte
        else:
            resultat += caractere_texte

        index_caractere_courant_texte += 1

    return resultat

def chiffrer_texte(chiffrer):
    """
        Chiffre/Dechiffre un texte saisi par l'utilisateur par la méthode de Vigenere

        Args:
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
    """
    alphabet = string.ascii_lowercase

    if chiffrer:
        print("Chiffrer un texte\n*********************")
        texte_input = "\tSaisissez le texte à chiffrer\n\t>"
        texte_resultat = "\tTexte chiffré"
    else:
        print("Déchiffrer un texte\n**********************")
        texte_input = "\tSaisissez le texte à déchiffrer\n\t>"
        texte_resultat = "\tTexte déchiffré"


    cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")
    while not cle:
        print("\tLa clé ne doit pas etre vide")
        cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")

    print("\tLe texte est formé à partir des lettres de l'alphabet et peut contenir des lettres majuscules.")
    texte=input(texte_input)
    while not texte:
        print("\tLe texte ne doit pas etre vide")
        texte=input(texte_input)

    resultat=chiffrement(alphabet, texte, chiffrer, cle)
    print(texte_resultat,"\n\t>",resultat)

# print(chiffrement.__doc__)
# print(chiffrer_texte.__doc__)
