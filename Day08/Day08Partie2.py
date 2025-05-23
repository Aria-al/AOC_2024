def traduitString (j : int, s : str, d : dict) : 
    i = 0 
    for c in s : 
        if (c != ".") and (c != "\n"): 
            if c in d.keys() : 
                listPosition = d[c] 
                listPosition.append((j, i))
            else : 
                d[c] = [(j, i)]
        
        i += 1 
    return d 

def traduitInput (filepath : str) : 
    fichier = open(filepath, "r")

    dictRes = dict()
    j = 0 
    i = 0 
    for line in fichier : 
        dictRes = traduitString(j, line, dictRes)
        j += 1 
        i = len(line)
    return (j, i), dictRes

def nbAntinodeTotaux (antennePositions : dict[str, list[tuple[int, int]]], dimensions : tuple[int, int]) -> int : 
    xMax, yMax = dimensions
    def dansMatrice (point : tuple[int, int]) -> bool : 
        """
        Retourne point est dans le plan 
        """
        x, y = point 
        return (x >= 0) and (y >= 0) and (xMax > x) and (yMax > y)  
    

    def calculeVecteur (p1 : tuple[int, int], p2 : tuple[int, int]) -> tuple[int, int] : 
        """
        Calcule le vecteur p1->p2
        """
        x1, y1 = p1 
        x2, y2 = p2 
        return (x2 - x1, y2 - y1)
    
    
    def antinodeDansMatrice (p1 : tuple[int, int], p2 : tuple[int, int], lstPoints : list[tuple[int, int]]) -> list[tuple[int, int]] : 
        
        vct = calculeVecteur(p1, p2) 
        # On teste si p1 + 2 * vct = p2 + vct est dans la matrice 
        x2, y2 = p2
        x1, y1 = p1
        dx, dy = vct 
        pointTemp = (x1, y1)
        while (dansMatrice(pointTemp)) : 
            if (pointTemp not in lstPoints) : 
                lstPoints.append(pointTemp)
            u, v = pointTemp
            pointTemp = (u + dx, v + dy)

        dx, dy = vct 
        dx, dy = -dx, -dy
        pointTemp = (x2, y2)
        while (dansMatrice(pointTemp)) : 
            if ((pointTemp not in lstPoints)) : 
                lstPoints.append(pointTemp)
            u, v = pointTemp
            pointTemp = (u + dx, v + dy)

        return lstPoints
    
    def antinodeParLettre (lstPoints : list[tuple[int, int]], lstAntennes : list[tuple[int, int]]) -> list[tuple[int, int]] : 
        for i in range(len(lstAntennes)) : 
            for j in range(i + 1, len(lstAntennes)) : 
                lstPoints = antinodeDansMatrice(lstAntennes[i], lstAntennes[j], lstPoints)
            print("==========================")
        return lstPoints
    
    sommetVisites = [] # Liste des points déja considérés comme antinode 
    for c in antennePositions.keys() : 
        sommetVisites = antinodeParLettre(sommetVisites, antennePositions[c])
    print(sommetVisites)
    return len(sommetVisites)

dim, d = traduitInput("./Day08/input")
print(dim)
print(d)
print(nbAntinodeTotaux(d, dim))