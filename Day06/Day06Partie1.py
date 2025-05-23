def traduitInput (filePath : str) -> list[list[int]] : 
    fichier = open(filePath, "r")
    listeBlocs = []

    def ligneTraduit (ligne : str) -> list[int] : 
        res = []
        for c in ligne : 
            if (c != "\n") : 
                res.append(c)
        return res 
    
    for line in fichier : 
        listeBlocs.append(ligneTraduit(line))
    return listeBlocs

def dansMat (_pos : tuple[int, int], mat : list[list[int]]) -> bool : 
    """
    Retourne si le couple de coordonnées est dans la matrice 
    """
    xMax, yMax = len(mat), len(mat[0])
    xPos, yPos = _pos 
    return (xPos >= 0 and xPos < xMax and yPos >= 0 and yPos < yMax)

def calculeTrajectoire (pos : tuple[int, int], 
                        mat : list[list[int]], dir : int) -> tuple[list[list[int]], tuple[int, int]] : 
    """
    Va effectuer le movement du garde de pos dans la direction donnée
    """
    dx, dy = 0, 0
    match dir : 
        case 0 : 
            # On va en haut 
            dx, dy = -1, 0
        case 1 : 
            # On va à droite 
            dx, dy = 0, 1
        case 2 : 
            # On va en bas
            dx, dy = 1, 0
        case 3 : 
            # On va à gauche 
            dx, dy = 0, -1 
    
    def estObstacle (_pos : tuple[int, int]) -> bool : 
        """
        On suppose que _pos décrit un set de coordonnées correctes 
        Retourne si cette case est un obstacle 
        """
        xPos, yPos = _pos
        return mat[xPos][yPos] == "#"

    x, y = pos 
    posPred = pos 
    while dansMat(pos, mat) and (not estObstacle(pos)) : 
        x, y = pos 
        mat[x][y] = "X"
        posPred = (x, y) 
        pos = (x + dx, y + dy)
    
    if dansMat(pos, mat) : 
        # On rencontre un obstacle 
        return (mat, posPred)
    else : 
        return (mat, (-1, -1))

def afficheMat (mat : list[list[int]]) : 
    for ligne in mat : 
        print(ligne)

def simuleMouvement(filepath : str) -> list[list[int]] : 
    mat = traduitInput(filepath)
    def trouveDebut () -> tuple[int, int] : 
        for i in range(len(mat)) : 
            for j in range(len(mat[0])) : 
                if (mat[i][j] == "^") : 
                    return (i, j)

    pos = trouveDebut()
    dir = 0 
    mat, pos = calculeTrajectoire(pos, mat, dir)
    while pos != (-1, -1) : 
        dir = (dir + 1) % 4
        mat, pos = calculeTrajectoire(pos, mat, dir)
    
    def comptePas () -> int : 
        res = 0 
        for ligne in mat : 
            for c in ligne : 
                if (c == "X") : 
                    res += 1 
        return res 
    return comptePas()


print(simuleMouvement("./Day06/input"))
