fichier = open("./Day4/input", "r")

dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
XMAS = "XMAS"

def retourneValeur (i, j, mat) : 
    if (i < 0) or (i >= len(mat)) : 
        return 'd'
    elif (j < 0) or (j >= len(mat[0])) : 
        return 'd'
    #print(i, j)
    return mat[i][j]

def estPresent (i, j, mat) : 
    nbMatches = 0 
    for v1, v2 in dir : 
        iTemp, jTemp = i, j
        isMatched = True 
        for k in range (1, 4) : 
            iTemp += v1 
            jTemp += v2 
            if (retourneValeur(iTemp, jTemp, mat) != XMAS[k]) : 
                isMatched = False 
        if (isMatched) : 
            nbMatches += 1 
    return nbMatches 

def Part1 () : 
    mat = []
    for ligne in fichier : 
        mat.append(ligne)
    """
    
    """
    res = 0 
    for j in range(len(mat)) : 
        for i in range(len(mat[j])) : 
            if (mat[j][i] == "X") : 
                res += estPresent(j, i, mat)
    return res 

print(Part1())