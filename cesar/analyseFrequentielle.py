#!/usr/bin/python3
import string
from cesar.bruteForceCesar import force_brute

def read_frequences():
    """Lit les frequences dans un fichier frequences.txt et les stockent dans un dictionnaire
    Returns:
    - frequences (dictionnaire) : contient la liste des frequences des lettres de l'alphabet d'une langue donnée
    """

    frequences = {}
    f = open('frequences.txt',"r")
    fichier = f.read().strip()
    #ex : Francais=a/b/c/d/.../z;
    lignes = fichier.split(";")
    f.close()

    for ligne in lignes:
        langage = ligne.split("=")
        key = langage[0]
        value = langage[1].split("/")
        frequences[key] = value

    return frequences

def get_langues():
    """Retourne la liste de langues disponibles pour les frequences
    """
    return list(read_frequences().keys())

def get_frequences(alphabet,texte):
    """Calcule les frequences d'apparition de chaque lettre de l'alphabet dans le texte
    Args:
    - alphabet (string ou liste de caractere): l'alphabet
    - texte (string) : le texte à attaquer
    Returns:
    - frequences (liste) : contient les frequences d'apparition de chaque lettre de l'alphabet dans le texte
    """
    longueur_texte = len(texte)
    frequences = []*len(alphabet)

    for lettre in alphabet:
        nb_apparition = texte.count(lettre) # ni
        frequence = nb_apparition/longueur_texte*100 #fi=ni/n
        frequences.append(frequence)

    return frequences

def analyse_frequentielle(alphabet,langue,texte):
    """Effectue la cryptanalyse du texte à attaquer
    Args:
    - langue (string) : la langue du texte d'origine
    - texte (string) : le texte à attaquer
    Returns:
    - cle (int) : la clé trouvée
    """

    #alphabet  = string.ascii_lowercase
    longueur_alphabet = len(alphabet)

    # frequences de la langue
    frequences_langues = read_frequences()
    frequences_langue = frequences_langues[langue]

    # calcul de la frequence de chaque lettre de l'alphabet
    frequences_texte = get_frequences(alphabet,texte)

    # on trouve tous les chiffrements possible du texte
    resultats = force_brute(alphabet,texte,True)
    coincidence = [0]*longueur_alphabet

    for i in range(longueur_alphabet):
        # on trouve les frequences des lettres du texte
        freq = get_frequences(alphabet,resultats[i])
        k = 0
        for j in range(longueur_alphabet):
            k += freq[j]*float(frequences_langue[j])#k+=f*fi
        coincidence[i] = k

    # la clé correspond au plus haut indice de coincidence
    cle = coincidence.index(max(coincidence))
    return cle
