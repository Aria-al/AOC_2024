

# Mal expliqué, il faudrait spécifier que à chaque espace de donné on attribue le numéro, pas un chiffre




def lireInput (filePath : str) -> list[tuple[int,int]] : 
    s = open(filePath, "r")
    ligne = s.readline()
    numFichier = 0 
    estFichier = True
    res = []
    def estTailleNul () -> bool : 
        return int(c) == 0
    for c in ligne : 
        if c == '\n'  : 
            break 
        elif estFichier : 
            res.append((numFichier, int(c)))
            numFichier += 1
            estFichier = False 
        else : 
            res.append((-1, int(c)))
            estFichier = True 
    return res 




def donneValeurBase10 (lst : list[int], base : int) -> int : 
    i = 1
    res = 0 
    while (i < len(lst) + 1) : 
        res += lst[-i] * (base**(i-1))
        i += 1
    return res 

def donneFormatBaseN (n : int, base : int) -> list[int] : 
    """
    Calcule la représentation de n dans une base donnée 
    """
    def borneSup () -> int : 
        """
        Donne la puissance de base 
        """
        i = 0 
        while (0 <= n - (base ** i)) : 
            i += 1
        return i 
    
    res = []
    i = 0 
    acc = 0
    while (i < borneSup()) : 
        res.append((n - acc) % (base**(i+1)) // (base**i))
        acc += (n - acc) % (base**(i+1))
        i += 1
    res.reverse()
    return res

N = 18 
assert N == donneValeurBase10(donneFormatBaseN(N, 16), 16)

def transformeListe (lst : list[tuple[int, int]]) -> list[str] : 
    res = []

    def imprimeString (t : tuple[int, int]) -> list[str] : 
        n, longueur = t 
        res1 = []
        base_10_de_n = ["0"]

        if (n == -1) : 
            base_10_de_n = ["."]
        elif (n == 0) :
            base_10_de_n = ["0"]
        else : 
            base_10_de_n = [str(v) for v in donneFormatBaseN(n, 10)]

        for i in range (longueur) : 
            res1.append(base_10_de_n[i % len(base_10_de_n)])
        return res1 

    for tpl in lst : 
        res += imprimeString(tpl)

    return res

def traduitInput (lst : list[tuple[int, int]]) -> list[str] : 
    res = []

    for tpl in lst : 
        n, taille = tpl
        if (n == -1) : 
            c = "."
        else : 
            c = str(n)

        for i in range(taille) : 
            res.append(c)

    return res

def libereEspaceDisque (fichier : list[str]) -> str : 
    premierEspaceVide : int = 0 
    dernierEmplacementFichier : int = len(fichier) - 1

    while premierEspaceVide <= dernierEmplacementFichier : 
        
        if fichier[premierEspaceVide] == "." and fichier[dernierEmplacementFichier] != "." : 
            fichier[premierEspaceVide] = fichier[dernierEmplacementFichier]
            fichier[dernierEmplacementFichier] = "."

        else : 
            if fichier[premierEspaceVide] != "." : 
                premierEspaceVide += 1
            
            if fichier[dernierEmplacementFichier] == "." : 
                dernierEmplacementFichier -= 1 
    
    return fichier

def calculeChecksum (fichier : list[str]) -> int : 
    i = 0 
    res = 0 
    while (i < len(fichier)) : 
        if (fichier[i] != ".") : 
            res += (int(fichier[i]) * i)
        i += 1
    return res


    

print(calculeChecksum(libereEspaceDisque(traduitInput(lireInput("./Day09/input")))))
