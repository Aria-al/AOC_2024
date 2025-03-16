import re 

fichier = open("./Day07/input", "r")

"""
Une expression est un tableau T = [u1, ..., un] avec des opérateurs O = [o1, ..., o(n-1)]: 
u1 = u2 o1 u3 o2 ... o(n-1) un

Un opérateur est soit '+', soit '*'
"""

rule1 = r"\d+"
equa = []
longueurMax = 0 
# On lit chaque ligne comme étant v: u1 u2 ... un
for line in fichier : 
    temp = re.findall(rule1, line)
    for i in range(len(temp)) : 
        temp[i] = int(temp[i])

    if len(temp) - 1 > longueurMax : 
        longueurMax = len(temp) - 1

    equa.append((temp[0], temp[1:]))
    print(str(equa[-1]))

def combiTotales (totalLength : int) : 
    """
    Retourne l'ensemble des combinaisons de liste de {0, 1} de taille donnée
    """    
    def copyList (l : list) : 
        res = []
        for i in l : 
            res.append(i)
        return res 

    def rec (l : list) : 
        if len(l) == totalLength : 
            return [l]
        else : 
            t1 = copyList(l)
            t1.append(0)
            l1 = rec(t1)
            t2 = copyList(l)
            t2.append(1)
            l2 = rec(t2)
            return l1 + l2 
        
    return rec([])

def equationValide (val : int, equa : list[int], listeOperateurs : list[int]) : 
    def binCalc (a : int , b : int, op : int) : 
        if op == 1 : 
            return a * b 
        return a + b 
    
    def calc (e : list[int], opL : list[int]) : 
        res = e[0]
        for i in range(1, len(e)) : 
            res = binCalc(res, e[i], opL[i - 1])
        return res 

    return calc(equa, listeOperateurs) == val

def existeListeValide (val : int, equa : list[int], lOpTotal : list[list[int]]) : 
    for l in lOpTotal : 
        print(l)
        print(equa)
        if equationValide(val, equa, l) : 
            return True
    return False

listeOpTotales = [combiTotales(i) for i in range(longueurMax)] 

res = 0 
for leftPart, rightPart in equa : 
    print(len(rightPart) - 1)
    if existeListeValide(leftPart, rightPart, listeOpTotales[len(rightPart) - 1]) : 
        res += leftPart

print(res)
