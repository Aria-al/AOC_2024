import re 

fichier = open("./Day5/input", "r")

rule1 = r"\d+"
"""
Donne la liste des ordres de pages requises, sachant que les valeurs associées à la clé donne 
l'ensemble des pages qui doivent être imprimées avant celle-ci 
"""
PageOrdering = dict()
PageNumberUpdates = []
mode = 1
for line in fichier : 
    match mode : 
        case 1 : 
            if (line == "\n") : 
                mode = 2 
            else : 
                k, v = re.findall(rule1, line)
                k = int(k) ; v = int(v) ; 
                if (k in PageOrdering.keys()) : 
                    temp = PageOrdering[k] 
                    if (v not in temp) : 
                        temp.append(v) 
                        PageOrdering[k] = temp 
                else : 
                    PageOrdering.update({k : [v]})
        case 2 : 
            Array = re.findall(rule1, line) 
            Array = list(map(int, Array))
            PageNumberUpdates.append(Array)

# Vérifie si la page Array[i] est bien placé, à partir de la loi (Tableau) donnée
def bienPlace (Array, i, Loi) : 
    print(set(Array[:i]) & set(Loi))
    return set(Array[:i]) & set(Loi) ==set()

def bienArrange (Array, Lois) : 
    Cles = Lois.keys()
    for i in range (len(Array)) : 
        if (Array[i] in Cles) and not bienPlace(Array, i, Lois[Array[i]]) : 
            return False 
    return True 

print(PageOrdering)

nb = 0 
for i in range (len(PageNumberUpdates)) : 
    if bienArrange(PageNumberUpdates[i], PageOrdering) : 
        nb += PageNumberUpdates[i][len(PageNumberUpdates[i]) // 2]
print(nb)
# Partie 2, idée : retenir les pages qui sont mal ordonnées, et faire bouger toutes ces pages 
# vers la gauche de 1, jusqu'à ce que on obtienne un bon graphe 

# Renvoie -1 si il n'y a pas de page qui est en conflit avec celle présente, la valeur si oui 
def estFoire (Array, i, Loi) : 
    for j in range (i) : 
        if Array[j] in Loi : 
            return j 
    return -1

# Renvoie la liste constitué des erreurs présentes dans la liste 
def trouveErreurs (Array, Lois) : 
    res = []
    Cles = Lois.keys()
    for i in range (len(Array)) : 
        if (Array[i] in Cles) : 
            temp = estFoire(Array, i, Lois[Array[i]])
            if (temp != -1) and (temp not in res) : 
                res.append(temp)
    print(res) 

# Décale toutes les valeurs de Array dont l'index est dans la liste Changements de 1 pas vers la gauche
def decale1 (Array, Changements) : 
    var = Array[Changements[0]]