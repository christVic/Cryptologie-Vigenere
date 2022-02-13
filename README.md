# Cryptologie-Vigenere-python
Cryptographie ( chiffrement et dechiffrement ) <!--et cryptanalyse -->du chiffrement de Vigenere en Python.

Ce Programme permet de
* chiffrer un message par la méthode de Vigenère
* déchiffrer un message chiffré par la méthode de Vigenère
<!--* décrypter un message chiffré par la méthode de Vigenère-->


## Chiffrement et déchiffrement (chiffrement.py)
* L'utilisateur peut definir son propre alphabet ou laisser l'alphabet par defaut (si c'est demandé).
* Les lettres de l'alphabet doivent être en minuscule. ex:alphabet="abcdef0123!?"
* L'utilisateur doit definir un clé de chiffrement/dechiffrement(caractere,mot,phrase,...). La clé par defaut est "cle".
* Le texte à traiter peut contenir des lettres majuscules. ex:Il était une Fois
* Les caracteres/lettres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Pour chiffrer(dechiffrer) un texte, le booleen "chiffrer" doit etre à True(False).

###### Exemple d'utilisation 1
```
from chiffrement import chiffrement
alphabet = "abcdefghijklmnopqrstuvwxyz"
texte = "cryptographie"
chiffrer = True
cle = "cle"
resultat = chiffrement(alphabet,texte,chiffrer,cle)
print(resultat)
```
###### Exemple d'utilisation 2
Demander à l'utilisateur de saisir  l'alphabet, le texte à chiffrer/déchiffrer et la clé
```
from chiffrement import chiffrer_texte
alphabet_defaut = "abcdefghijklmnopqrstuvwxyz"
chiffrer = True
chiffrer_texte(alphabet_defaut,chiffrer)
```
<!--## Cryptanalyse (cryptanalyse.py)-->
##
