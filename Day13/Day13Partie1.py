from dataclasses import dataclass


@dataclass
class machine : 
    boutonA : tuple[int, int]
    boutonB : tuple[int, int]
    recompense : tuple[int, int]
    def toStr(self) : 
        return "Bouton A : " + str(self.boutonA) + "\n" + "Bouton B : " + str(self.boutonB) + "\n" + "Récompense : " + str(self.recompense) + "\n"
    
    


def lireInput (filePath : str) -> list[machine] : 
    f = open(filePath, "r")
    i = 0 
    s = f.readline()
    res = []
    boutonA, boutonB, recompense = (0, 0), (0, 0), (0, 0)
    while (s != "") : 
        x = s.split(" ")

        valX, valY = (0, 0)
        if (len(x) > 1) : 
            valX = int(x[-2][2:-1])
            valY = int(x[-1][2:-1])

        match i : 

            case 0 : 
                # Bouton A
                boutonA = (valX, valY)

            case 1 : 
                # Bouton B
                boutonB = (valX, valY)

            case 2 : 
                # Récompense 
                recompense = (valX, valY)

            case 3 : 
                res.append(machine(boutonA, boutonB, recompense))

        s = f.readline()
        i = (i + 1) % 4
    f.close()
    return res



"""
Soit (xR, yR) la position de l'objetif, et soient (xA, yA) et (xB, yB) 
les distances en x et y que les boutons A et B font parcourir à la grue. 
On cherche une solution au problème suivant : 
min s = a * 3 + b
xR = xA * a + xB * b
yR = yA * a + yB * b
à faire pour la partie 2 
"""

def calculeCout (s : tuple[int, int]) : 
    a, b = s 
    return a * 3 + b

def estEgal (p1 : tuple[int, int], p2 : tuple[int, int]) -> bool  : 
    """
    Retourne si p1 == p2
    """
    x1, y1 = p1
    x2, y2 = p2 
    return (x1 == x2 and y1 == y2)

def chercheSol (prob : machine) -> tuple[int, int] : 
    def calcPos (a, b) :
        xA, yA = prob.boutonA
        xB, yB = prob.boutonB
        return (xA * a + xB * b, yA * a + yB * b)
    
    
    
    maxA, maxB = 100, 100
    coutMin = 300 + 100 
    nbA, nbB = 100, 100

    for i in range(maxA) : 
        for j in range(maxB) : 
            newPos = calcPos(i, j)
            if estEgal (prob.recompense, newPos) and calculeCout((i, j)) < coutMin : 
                nbA = i 
                nbB = j 
                coutMin = calculeCout((i, j))
    
    if (not estEgal(prob.recompense, calcPos(nbA, nbB))) : 
        return (-1, -1)

    return (nbA, nbB)
                
liste = lireInput("./Day13/input")

nbToken = 0 
for e in liste : 
    sol = chercheSol(e)
    if (not estEgal((-1, -1), sol)) : 
        nbToken += calculeCout(sol)
print(nbToken)