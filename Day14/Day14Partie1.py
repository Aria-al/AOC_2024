import re 


def lireInput (filePath : str) -> list[tuple[tuple[int, int], tuple[int, int]]] : 
    regSearch = "-?\\d+"
    f = open(filePath, "r")
    res = []
    for e in f : 
        l = [int(i) for i in re.findall(regSearch, e)]
        res.append(((l[0], l[1]), (l[2], l[3])))
    return res 


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

def bougeRobots (l : list[tuple[tuple[int, int], tuple[int, int]]]) -> list[tuple[int, int]] : 
    res = []
    def mouvementSuivant (p : tuple[int, int], v : tuple[int, int]) -> tuple[int, int] : 
        x, y = p 
        vx, vy = v 
        return (additionModulo(x , vx, xMax), additionModulo(y, vy, yMax))

    def positionApresMoments(p : tuple[int, int], v : tuple[int, int], t : int) -> tuple[int, int] : 
        x, y = p 
        vx, vy = v 
        return (additionModulo(x , multiplicationModulo(vx, t, xMax), xMax), additionModulo(y, multiplicationModulo(vy, t, yMax), yMax))

    for trajectoire in l : 
        pos, velocite = trajectoire
        pos = positionApresMoments(pos, velocite, 100)
        res.append(pos)
    
    return res


def calculeQuadrantsValue (l : list[tuple[int, int]]) -> int : 
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
    print(reponseA)
    res = 1 
    for i in reponseA : 
        res = res * i 
    
    return res 


liste = lireInput("./Day14/input")
liste = bougeRobots(liste)

print(calculeQuadrantsValue(liste))