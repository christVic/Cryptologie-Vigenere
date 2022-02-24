#!/usr/bin/python3
import string

def chiffrement(alphabet,texte,cle,chiffrer):
    """Chiffre/Dechiffre un texte par la méthode de Cesar

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - texte (string) : le texte à chiffrer/dechiffrer
            - cle (int) : la clé utilisée pour chiffrer/dechiffrer le texte
            - chiffrer (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (string) : le texte obtenu après le chiffrement/dechiffrement
    """

    resultat = ""
    if not chiffrer:
        cle = cle*(-1)

    for caractere in texte:
        caractere_lower = caractere.lower()
        if caractere_lower in alphabet:
            index_nouveau_caractere = (alphabet.index(caractere_lower)+cle)%len(alphabet)
            if caractere.isupper():
                resultat += alphabet[index_nouveau_caractere].upper()
            else:
                resultat += alphabet[index_nouveau_caractere]
        else:
            resultat += caractere

    return resultat
