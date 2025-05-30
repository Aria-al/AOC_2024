def afficheMat (m : list[list]) -> None : 
    """
    Affiche la matrice passée en paramètres 
    """
    for l in m : 
        s = ""
        for e in l : 
            s = s + str(e) + " "
        print(s)

def traduitInput (filepath : str) -> list[list[int]] : 
    f = open(filepath, "r")
    res = []
    for line in f : 
        l = []
        for c in line : 
            if (c != "\n") : 
                l.append(int(c))
        res.append(l)
    return res



def sommePos (a : tuple [int, int], b : tuple[int, int]) -> tuple[int, int] : 
    ya, xa = a
    yb, xb = b 
    return (ya + yb, xa + xb)

def union (A : list, B : list) : 
    def eq (u1, u2) : 
        y1, x1 = u1
        y2, x2 = u2
        return (y1 == y2) and (x1 == x2)

    res = A 
    for e1 in B : 
        estPresent = True 
        for e2 in res : 
            estPresent = estPresent and not eq(e1, e2)
        if (estPresent) : 
            res.append(e1)

    return res 
        


print(union([(1, 1), (2, 2)], [(1, 1), (3, 3)]))

def estDansMat (mat : list[list], pos : tuple[int, int]) -> bool : 
    y, x = pos 
    return (0 <= y) and (0 <= x) and (y < len(mat)) and (x < len(mat[0]))

def cheminsPossibles (mat : list[list[int]], pos : tuple[int, int]) -> int : 
    def mouvementSuivant (pos1 : tuple[int, int]) -> int : 
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        res = 0
        yPos, xPos = pos1
        for d in directions : 
            newPos = sommePos(pos1, d)
            y, x = newPos
            if estDansMat(mat, newPos) and (mat[y][x] == (mat[yPos][xPos] + 1)) : 
                if (mat[y][x] == 9) : 
                    res += 1 
                else : 
                    res += mouvementSuivant((y, x))
        return res 
    
    return mouvementSuivant(pos)

def scoreCarte (filePath : str) -> int : 
    mat = traduitInput(filePath)
    res = 0 
    for y in range (len(mat)) : 
        for x in range(len(mat[0])) : 
            if (mat[y][x] == 0) : 
                res += cheminsPossibles(mat, (y, x))
    return res 

print(scoreCarte("./Day10/input"))