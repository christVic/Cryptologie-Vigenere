#!/usr/bin/python3
import string
from cesar.chiffrementCesar import chiffrement

def force_brute(alphabet,texte,casser):
    """Réalise une attaque par force brute sur le texte

        Args:
            - alphabet (string ou liste de caractere): l'alphabet
            - texte (string) : le texte à chiffrer/dechiffrer
            - casser (booleen) : indique si l'on veut effectuer un chiffrement (True) ou un dechiffrement (False).
        Returns:
            - resultat (dictionaire) : les textes obtenus après le chiffrement/dechiffrement selon les differentes clés possibles
    """

    resultats={}

    chiffrer=True
    if casser:
        chiffrer=False

    for k in range(len(alphabet)):
        resultats[k]=chiffrement(alphabet,texte,k,chiffrer)

    return resultats
