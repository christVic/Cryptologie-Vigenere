# Cryptologie-Vigenere-python
Cryptographie ( chiffrement et dechiffrement ) <!--et cryptanalyse -->du chiffrement de Vigenere en Python.

Ce Programme permet de
* chiffrer un message par la méthode de Vigenère
* déchiffrer un message chiffré par la méthode de Vigenère
<!--* décrypter un message chiffré par la méthode de Vigenère-->

## Lancement du programme
python3 main.py

* L'utilisateur peut definir son propre alphabet ou laisser l'alphabet par defaut (si c'est demandé).
* Le fichier "texteAChiffrer.txt" contient un texte en clair
* Le fichier "texteChiffre.txt" contient un texte chiffré par la méthode de Vigenere.

## Chiffrement et déchiffrement (chiffrement.py)
* L'utilisateur peut definir son propre alphabet.
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* L'utilisateur doit definir un clé de chiffrement/dechiffrement(caractere,mot,phrase,...).
* Le texte à traiter peut contenir des lettres majuscules. ex:Il était une Fois
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour chiffrer(dechiffrer) un texte, le booleen "chiffrer" doit etre à True(False).
```
from chiffrement import chiffrement
alphabet="abcdefghijklmnopqrstuvwxyz"
texte="cryptographie"
chiffrer=True
cle="cle"
resultat=chiffrement(alphabet,texte,cle,chiffrer)
print(resultat)
```
<!--## Cryptanalyse (cryptanalyse.py)-->
