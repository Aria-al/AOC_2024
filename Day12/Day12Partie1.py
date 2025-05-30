def afficheMat (m : list[list]) -> None : 
    """
    Affiche la matrice passée en paramètres 
    """
    for l in m : 
        s = ""
        for e in l : 
            s = s + str(e) + " "
        print(s)

def lireInput (filePath : str) -> list[list[str]] : 
    f = open(filePath, "r")
    res = []
    for line in f : 
        l = []
        for c in line : 
            if c != "\n" : 
                l.append(c)
        res.append(l)
    return res 

listDirCard = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sommePos (a : tuple [int, int], b : tuple[int, int]) -> tuple[int, int] : 
    ya, xa = a
    yb, xb = b 
    return (ya + yb, xa + xb)

def estDansMat (mat : list[list], pos : tuple[int, int]) -> bool : 
    y, x = pos 
    return (0 <= y) and (0 <= x) and (y < len(mat)) and (x < len(mat[0]))

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

def donnePoint (mat : list[list], pos : tuple[int, int]) : 
    yPos, xPos = pos 
    return mat[yPos][xPos]
    

def trouveRegion (pos : tuple[int, int], mat : list[list[tuple[str], bool]]) -> tuple[tuple[int, int], list[list[tuple[str, bool]]]] : 

    def creepSpread(p : tuple[int, int]) -> tuple[list[tuple[int, int]], int] : 
        """
        Fonction récusive qui calcule l'aire de la zone contigue possédant la même plante, ainsi que le périmètre de la zone 
        """
        aireRes = 1 
        perimetreRes = 0 
        yPosition, xPosition = p 
        ancienChamp, ancienVisite = donnePoint(mat, p)

        if (ancienVisite == True) : 
            return (0, 0)
        
        mat[yPosition][xPosition] = (ancienChamp, not ancienVisite)

        for d in listDirCard : 
            # On considère une des parcelles adjacentes à p 
            nouvelleParcelle = sommePos(d, p)

            if (estDansMat(mat, nouvelleParcelle)) : 
                nouveauChamp, nouveauVisite = donnePoint(mat, nouvelleParcelle)

                # Si cette parcelle a la même plante que p 
                if (nouveauChamp == ancienChamp) : 

                    # Si le champ n'as pas encore été visité 
                    if (not nouveauVisite) : 

                        # On va explorer la sous-zone qui s'étend à partir de nouvelleParcelle 
                        aireTemp, perimTemp = creepSpread(nouvelleParcelle)
                        aireRes += aireTemp
                        perimetreRes += perimTemp
                
                # La parcelle n'as pas la même plante que p 
                else : 
                    # On a donc un nouveau morceau du périmètre 
                    perimetreRes += 1 
            else : 
                perimetreRes += 1 

        return (aireRes, perimetreRes)

    return (creepSpread(pos), mat)
            


def transformeMatrice (mat : list[list[str]]) -> list[list[tuple[str, bool]]] : 
    res = []
    for l in mat : 
        ligne = []
        for e in l : 
            ligne.append((e, False))
        res.append(ligne)
    return res 

            

def calculateFenceArea (mat : list[list[str]]) -> list[tuple[str, int, int]] : 
    # On définit un triplet de res comme étant (nom de plante, aire, périmètre)
    res = []
    matrice = transformeMatrice(mat)
    for j in range (len(matrice)) : 
        for i in range(len(matrice[0])) : 
            lettre, estVisite = matrice[j][i]
            if (not estVisite) : 
                coupleVal, matrice = trouveRegion((j, i), matrice)
                aire, perimetre = coupleVal
                res.append((lettre, aire, perimetre))
    return res 

    

carte = lireInput("./Day12/input")

print(calculateFenceArea(carte)) 

def calculeCout (l : list[tuple[str, int, int]]) -> int : 
    res = 0 
    for e in l : 
        _, aire, perim = e 
        res += aire * perim
    return res 

print(calculeCout(calculateFenceArea(carte)))