#!/usr/bin/python3
import string

def chiffrement(alphabet, texte ,chiffrer, cle):
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
    taille_cle = len(cle)
    if not cle:
        cle = "cle"
    # le ième caractère du texte
    index_caractere_courant_texte = 0

    resultat = ""

    chiffrer = 1
    if not chiffrer:
        chiffrer = -1

    for caractere_texte in texte:
        # cas où le caractere du texte est dans l'alphabet
        if caractere_texte.lower() in alphabet:
            # on trouve le caractere de la clé à utiliser pour chiffrer/dechiffre
            caractere_cle = cle[index_caractere_courant_texte%taille_cle].lower()

            # cas où le caractere de la clé à utiliser est dans l'alphabet
            if caractere_cle in alphabet:
                # on trouve l'index du caractere_cle dans l'alphabet
                index_caractere_cle = chiffrer*alphabet.index(caractere_cle)+chiffrer

                # on calcule l'index du caractere obtenu apres chiffrement
                index_nouveau_caractere = (alphabet.index(caractere_texte.lower())+index_caractere_cle)%len(alphabet)

                # cas où le caractere du texte est une lettre majuscule
                if caractere_texte.isupper():
                    resultat+=alphabet[index_nouveau_caractere].upper()

                # cas où le caractere du texte est une lettre minuscule
                else:
                    resultat+=alphabet[index_nouveau_caractere]

            # cas où le caractere de la clé à utiliser n'est pas dans l'alphabet
            else:
                resultat += caractere_texte

        # cas où le caractere du texte n'est pas dans l'alphabet
        else:
            resultat += caractere_texte
        index_caractere_courant_texte += 1

    return resultat

def chiffrer_texte(alphabet,chiffrer):
    """
        Chiffre/Dechiffre un texte saisi par l'utilisateur par la méthode de Vigenere

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (string) : le texte obtenu après le chiffrement/dechiffrement
    """
    if chiffrer:
        print("Chiffrer un texte\n*********************")
        texte_input = "\tSaisissez le texte à chiffrer\n\t>"
        texte_resultat = "\tTexte chiffré"
    else:
        print("Déchiffrer un texte\n**********************")
        texte_input = "\tSaisissez le texte à déchiffrer\n\t>"
        texte_resultat = "\tTexte déchiffré"

    print("\tPour utiliser l'alphabet par defaut(",alphabet,"), laisser vide et appuyer sur Entrer ")
    alphabet_input = input("\tQuel alphabet souhaitez-vous utiliser?(les lettres en miniscules!Pas de majuscule)\n\t>")
    if alphabet_input:
        alphabet = alphabet_input

    cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")
    while not cle:
        print("\tLa clé ne doit pas etre vide")
        cle=input("\tQuelle clé(un caractere, un mot, une phrase, un texte,..) souhaitez-vous utiliser?\n\t>")

    print("\tLe texte est formé à partir des mots de l'alphabet choisi et peut contenir des lettres majuscules.")
    texte=input(texte_input)
    while not texte:
        print("\tLe texte ne doit pas etre vide")
        texte=input(texte_input)

    resultat=chiffrement(alphabet, texte, chiffrer, cle)
    print(texte_resultat,"\n\t>",resultat)

# print(chiffrement.__doc__)
# print(chiffrer_texte.__doc__)
