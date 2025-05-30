import re 
import os

def lireInput (filePath : str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] : 
    regSearch = "-?\\d+"
    f = open(filePath, "r")
    resPos, resVect = [], []
    for e in f : 
        l = [int(i) for i in re.findall(regSearch, e)]
        resPos.append((l[0], l[1]))
        resVect.append((l[2], l[3]))
    return (resPos, resVect)


def additionModulo (a : int, b : int, n : int) -> int : 
    """
    Calcule a + b mod n
    """
    a = a % n
    b = b % n
    return (a + b + n) % n

def multiplicationModulo (a : int, b : int, n : int) -> int : 
    """
    Calcule a * b mod n
    """
    a = a % n
    b = b % n
    return (((a + n) % n) * ((b + n) % n)) % n

xMax, yMax = 101,103

def bougeRobots (l : tuple[list[tuple[int, int]], list[tuple[int, int]]]) -> list[tuple[int, int]] : 
    res = []
    def mouvementSuivant (p : tuple[int, int], v : tuple[int, int]) -> tuple[int, int] : 
        x, y = p 
        vx, vy = v 
        return (additionModulo(x , vx, xMax), additionModulo(y, vy, yMax))
    lPos, lVect = l 
    for i in range(len(lPos)) : 
        res.append(mouvementSuivant(lPos[i], lVect[i]))
    return res

def trouveNbVal (p  : tuple[int, int], l : list[tuple[int, int]]) -> int : 
    res = 0 
    def egalVal (a, b) : 
        xa, ya = a
        xb, yb = b
        return (xa == xb) and (ya == yb)
    for e in l : 
        if (egalVal(e, p)) : 
            res += 1
    return res 

def afficheMatrice (l : list[tuple[int, int]]) -> None : 
    for i in range(xMax) : 
        s = ""
        for j in range(yMax) : 
            nbInstances = trouveNbVal((j, i), l)
            if (nbInstances == 0) : 
                s += "."
            else : 
                s += str(nbInstances)
        print(s)
    
def calculeQuadrantsDistance (l : list[tuple[int, int]]) -> int : 
    reponseA = [0, 0, 0, 0]
    midX, midY = xMax // 2, yMax // 2
    for e in l : 
        x, y = e
        if (x < midX) : 
            if (y < midY) : 
                reponseA[0] += 1
            elif (y > midY) : 
                reponseA[1] += 1 
        elif (x > midX) : 
            if (y < midY) : 
                reponseA[2] += 1
            elif (y > midY) : 
                reponseA[3] += 1 
    
    res = [(e - (len(l) // 4))**2 for e in reponseA]
    return res

def boucleSimulation (l : tuple[list[tuple[int, int], list[tuple[int, int]]]]) -> int : 
    cond = True 
    nbIterSup = int(input("Combien d'itérations par valeurs : "))
    listPos, vectRobots = l 
    nbIter = 0 
    def toleranceMax (l : list[int], tolerance : int) -> bool : 
        for e in l :
            if e > tolerance : 
                return False 
        return True 
    while cond : 
        for i in range(nbIterSup) : 
            listPos = bougeRobots((listPos, vectRobots))
            listeDistances = calculeQuadrantsDistance(listPos)
            if (toleranceMax(listeDistances, 25)) : 
                print("Itération " + str(nbIter))
                afficheMatrice(listPos)
            nbIter += 1 
        cond = int(input("Continuer la simulation : (1 pour oui/0 pour non)"))
        if cond == 0 :
            cond = False
        elif cond == 1 : 
            cond = True 
        else : 
            cond = False 
        os.system('cls' if os.name == 'nt' else 'clear')
            



liste = lireInput("./Day14/input")
boucleSimulation(liste)