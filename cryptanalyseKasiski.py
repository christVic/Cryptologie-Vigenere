import math
import string
import re
from analyseFrequentielle import get_langues
from analyseFrequentielle import analyse_frequentielle
from chiffrement import chiffrement



def pgcd(x,y):
    """
    Calcule le pgcd de deux valeurs
    Args:
    - x (int) : la première valeur
    - y (int) : la seconde valeur
    Returns:
    - un entier (int)
    """
    if x>=0 and y>=0:
        return math.gcd(x,y)
    else:
        print("l'une des valeurs (ou les deux valeurs) est(sont) négative(s)")
        return -1

def calculer_longueur_cle(texte):
    """
    Calcule la longueur de la clé utilisée pour chiffrer le texte (test de Kasiski)
    Args:
    - texte (string) : le texte à attaquer
    """
    longueur_cle = 0
    longueur_sous_chaine = 3
    longueurs =[0 for k in range(len(texte))]
    while longueur_sous_chaine < len(texte):

        for index_texte in range(len(texte)-longueur_sous_chaine+1):
            # on recupere la sous-chaine de taille "longueur_sous_chaine" à partir de "position_texte"
            index_debut_sous_chaine = index_texte
            index_fin_sous_chaine = index_debut_sous_chaine + longueur_sous_chaine
            sous_chaine = texte[index_debut_sous_chaine:index_fin_sous_chaine]

            # on cherche la premiere occurence de cette sous_chaine dans texte après\la sous-chaine
            """
                # texte_de_recherche est la portion de texte située après la sous-chaine
                # index_occurrence_dans_texte_de_recherche est l'index de la premiereoccurence dans "texte_de_recherche"
                # index_occurence_dans_le_texte_entier est l'index de l'occurrencetrouvée dans le texte entier
            """
            texte_de_recherche = texte[index_fin_sous_chaine:]
            index_occurrence_dans_texte_de_recherche = texte_de_recherche.find(sous_chaine)

            # cas où une occurence est trouvée
            if index_occurrence_dans_texte_de_recherche != -1:
                # on calcule la position de cette occurrence dans le texte en entier
                index_occurence_dans_le_texte_entier = index_occurrence_dans_texte_de_recherche + index_fin_sous_chaine

                # on calcul la distance entre l'index de la sous-chaine et l'index de l'occurrence trouvée
                distance = index_occurence_dans_le_texte_entier - index_debut_sous_chaine

                #print(sous_chaine,distance)
                #on met à jour le tableau des longueurs de clé possibles
                for val in range(2,distance+1):
                    if distance % val == 0:
                        # on incremente la case associée au diviseur de distance
                        longueurs[val] += 1

        longueur_sous_chaine += 1

    # la longueur de la clé à la case(diviseur) qui la le plus grand nombre
    longueur_cle = longueurs.index(max(longueurs))
    return longueur_cle

def deduction_cle(alphabet,texte,langue):
    """
    Déduit la clé utilisée pour chiffrer le texte par analyse de frequence
    Args:
    - texte (string) : le texte à attaquer
    - langue (string) : la langue du texte
    Returns:
        - cle (string) : la clé déduite
    """
    cle = ""
    longueur_cle = calculer_longueur_cle(texte)
    categories = ["" for i in range(longueur_cle)]

    if longueur_cle > 0:
        # on decoupe le message par categorie de caractere (ceux chiffrés par cle[0],cle[1],...,cle[longueur_cle])
        for index_texte in range(len(texte)):
            idx = index_texte % longueur_cle
            categories[idx]+=texte[index_texte]

        # on trouve retrouve la clé finale
        for categorie in categories:
            # on trouve la clé (int) utilisé pour chiffrer la ligne
            cle_ligne = analyse_frequentielle(alphabet,langue,categorie)

            # cle_ligne correspond à l'index du caractere dans l'alphabet
            cle += alphabet[cle_ligne]
    else:
         print("Pas de clé trouvée!")

    return cle

def attaque_kasiski(texte,langue):
    # on supprime la ponctuation et les espaces
    alphabet = string.ascii_lowercase
    texte = re.sub(r'[^\w\s]','',texte)
    texte = texte.replace(" ","")

    cle = deduction_cle(alphabet, texte, langue)
    if cle != "":
        resultat = chiffrement(alphabet, texte ,False, cle)
        return cle,resultat
    return "",""

chaine0="kqowéfv, jpujuunukglmekjin?mwuxfqmkjbgwrlfn! fghudwuumbsvlpsncmuekqcteswreekoyssiwctua xyotapxplwpntcgojbgfqhtdwxizaygffnsxcseynctsspntujnytggwzgrwuunejuuqeapymekqhuiduxfpguytsmtffshnuoczgmruweytrgkmeedctvrecfbdjqcuswvbpnlgoylskmtefvjjtwwmfmwpnmemtmhrspxfsskffstnuoczgmdoeoyeekcpjrgpmurskhfrseiuevgoycwxizaygosaanydoeoyjlwunhamebfelxyvlwnojnsiofrwucceswkvidgmucgocruwgnmaaffvnsiudekqhceucpfcmpvsudgavemnymamvlfmaoyfntqcuafvfjnxklneiwcwodcculwriftwgmuswovmatnybuhtcocwfytnmgytqmkbbnlgfbtwojftwgntejkneedcldhwtvbuvgfbijg"

chaine1="kqowefv jpujuunukglmekjinmwuxfqmkjbgwrlfnfghudwuumbsvlpsncmuekqcteswreekoyssiwctuaxyotapxplwpntcgojbgfqhtdwxizaygffnsxcseynctsspntujnytggwzgrwuunejuuqeapymekqhuiduxfpguytsmtffshnuoczgmruweytrgkmeedctvrecfbdjqcuswvbpnlgoylskmtefvjjtwwmfmwpnmemtmhrspxfsskffstnuoczgmdoeoyeekcpjrgpmurskhfrseiuevgoycwxizaygosaanydoeoyjlwunhamebfelxyvlwnojnsiofrwucceswkvidgmucgocruwgnmaaffvnsiudekqhceucpfcmpvsudgavemnymamvlfmaoyfntqcuafvfjnxklneiwcwodcculwriftwgmuswovmatnybuhtcocwfytnmgytqmkbbnlgfbtwojftwgntejkneedcldhwtvbuvgfbijg"
chaine2="wmfwepnfkrtlrjrtaqykzuolbfarmxyvrypdwanxwigyqplrmxcurypqznhzlqfypzvgzlcurokrwhpbcvrgbybpydzciyoymzykeiyfbrcnhqwiqyclqgyapvbmxcurypdmfnjtarholxcioeiiyzwmahbxqcirckrmppzyyzzuouqnmenbdvbopldbhppbrhlfafijxmfmrmurldpacuowisionmzyzlvvkrpbrlopaglbpbnyotmahbomyykymzcfynvhfxmanmwcfkrptrooywzvopkrmlybyypnpnlpwmfustwamilbnwqtyhyapanfipunhadyhckzcfzlybeyzftrlzpabhqwmfwelzffbdiiclyayuqlkgcnfmqypltyyjlvqmnfqbhqdcejotaaipnprzplccifybqyipangbymefxzcvfppvfikeihdlfzqbrtuncpwmqyoyqrljzbrmqttqcqwmfjbciawbowvnbwtrxfdxnlxdbeyillrzxtbrypemyfbomscktbvpbywawozgrtjzqzifbcvplfacuowmrhzzvaufdanhzplrwxfaryqgwhmatadobcqrhkpagjbclhjlfzyucciawbwmfgbxmfgljmamnfqairdwanslqawrdxrospvgzxtzrpbyqeokuwhlildvwqzqeyzlzyucciawbymfnmlafyrwmrfipvrmqaifmbftryiwmaypexnmppcyybwtrurydnmqpmzjfcmqyocqrlbptyybwtrjbfbsufcmoflniiyzwmzjfcmolfeiahfbcrkrtbvyketngbcmgwlybvhrptnfrebryiwmcyrekbgjptnhdwmgyocmhnfwqfyodiamituvnbdtvgjpvfyfylhmqcqrxbdmguqdcacpnmgnbrcrlopvrmqaifffxqgyblcgyocqgifcmzuismhlbffqykzbeymlgfwbebrarpzeykpagjxdbeuknprymlzyuylbnciwmqycciawbnmgnbrcrlopmfnrymtobczrglylvuipbboqpayypqihnbdbbopwmflbeiexpewhnbdtrmpzcszolvpypymzjbnprhqaifkrttlualvffryqiyodbbopwmfgljmamkpkrmplqeypawhlbnznmbccadlfzaippvayjtasirozbsbdihdlfzqbrtxnlilnblzpurwxyqdobywhmmzcellyaiufykeyalvffxgmacoaieokpnblzpurwxyqdobdccyotmhlbwmqypeqaxrxwaxbpagfxxwvabymeuiomturwtruzecrfipurhqltbhacmfdfydvnbwmficqqpcbcarnipafiioigmcciawxtadofdmgllfdrhqpvgyocqgifcmolfeiahfbcrirbcvpfpvqlxtmanxdggllfdrlxgmpfbfzfuoxmfirdiamipcemxcurmgtvicqptrmfyorhfpcembetrmlfdecbcafjbnqnffdbrmapavhafaglfpaquoxmzykeyhcppbeirgmanbybrlotbbcopjecqlvacnfmbonfqicbyleufpvgupjbeirgmeuppurnqcmrholxcioeiiyzxwvkrzqdofwielfgmyucwizgbomyuopavmqlvpycciawxtarhbowvnmlafyqpqaxopmghbdmgyfyleumlaqyjlqawlxururuwhlascvdbaiefbcivuilznxfzlrflyleyp"


def cryptanalyse_kasiski():
    """Réalise une attaque de Kasiski sur un un texte chiffré (Vigenere) saisi par l'utilisateur
    """

    print("Cryptanalyser un texte par la méthode de Kasiski\n**********************************")
    alphabet = string.ascii_lowercase
    langue = "Français"
    langues = get_langues()

    texte_langue = ""
    for i in range(len(langues)):
        texte_langue += "\t["+str(i)+"]"+langues[i]+"\n"
    print(texte_langue)
    langue_input = int(input("\tQuelle est la langue du texte d'origine?\n\t"))
    """if langue_input == 1:
        langue = "Anglais"""
    if langue_input>0:
        langue = langues[langue_input]

    print("\tLe texte à attaquer ne doit contenir que des lettres de l'alphabet(",alphabet,") peut importe la casse")
    texte = input("\tSaisissez le texte à attaquer\n\t>")
    while not texte:
        print("le texte ne peut pas etre vide")
        texte = input("\tSaisissez le texte à attaquer\n\t>")

    cle,resultat = attaque_kasiski(texte,langue)

    print("\t>La clé est : ",cle,"\n\t>Le resultat est : ",resultat)
