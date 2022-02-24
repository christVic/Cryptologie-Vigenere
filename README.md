# Cryptologie-Vigenere-python
Cryptographie ( chiffrement et dechiffrement ) et cryptanalyse du chiffrement de Vigenere en Python.

Ce Programme permet de
* chiffrer un message par la méthode de Vigenère
* déchiffrer un message chiffré par la méthode de Vigenère
* attaquer un message chiffré par la méthode de Vigenère (Kasiski <!--et attaque par analyse de frequences-->)


## Chiffrement et déchiffrement (chiffrement.py)
* L'alphabet utilisé est "abcdefghijklmnopqrstuvwxyz"
* L'utilisateur doit definir un clé de chiffrement/dechiffrement(chaine de caractere) dont les caracteres doivent appartenir à l'alphabet.
* Le texte à traiter peut contenir des lettres majuscules. ex:Il était une Fois
* Les caracteres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Les espaces et la ponctuation sont supprimés du texte et de la clé ex: "il est la!" devient "ilestla!"
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
Demander à l'utilisateur de saisir le texte à chiffrer/déchiffrer et la clé
```
from chiffrement import chiffrer_texte
alphabet_defaut = "abcdefghijklmnopqrstuvwxyz"
chiffrer = True
chiffrer_texte(chiffrer)
```
## Cryptanalyse par la méthode de Kasiski (cryptanalyseKasiski.py)
* Le texte à attaquer doit être assez long pour avoir un resultat correct
* L'alphabet utilisé est a...z
* Le texte à traiter peut contenir des lettres majuscules.
* Les caracteres du texte qui ne sont pas dans l'alphabet ne sont pas modifiées lors du chiffrement/dechiffrement.
* Les espaces et la ponctuation sont supprimés du texte ex: "il est la!" devient "ilestla"
* Le fichier frequences.txt contient les fréquences d'apparition des lettres a...z en differentes langues
* Les fréquences d'apparition des lettres sont tirées de [wikipedia](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais)
###### Exemple d'utilisation 1
```
from cryptanalyseKasiski import attaque_kasiski
langue = "Français"
texte = "VimjosfmojzyygemjlgupoczamorjwxixvumuwyursiksyRnvsimuhsxvcamrduapgjktkgjvvppawgrsmxhwliklvspjepzbkipdbzzqlqsxghrtpptpgjyjucakdtsMytfntOcevzkvcwslcaxgNflahvhczqfnwbfuhvvxtrtxifkjqjlbswkchocyuérvczgirtlrgesaPvhgvrfnwgljdbzhjlghhbzrughvkfvtdldxfttjbiwiqhhwketbhchkkqsxRovuevcvcmmxkruenébvigerxèfkciqlzxéàjpifkjstlbtqlputwxvltjwqovprxrkjptuaégjbtlvudmtzTiogggxfudaxumrckgaéhédoxuatwzqhtbzgagjmuwvRjezolsRpkitf4péqxztpcmgnzztkhé"
resultat = attaque_kasiski(texte,langue)
print(resultat)
```
###### Exemple d'utilisation 2
```
from cryptanalyseKasiski import cryptanalyse_kasiski
cryptanalyse_kasiski()
```
