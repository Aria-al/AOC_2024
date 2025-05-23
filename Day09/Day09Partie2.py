from Day09Partie1 import lireInput, traduitInput, calculeChecksum

def libereEspaceDisqueP2 (fichier : list[tuple[int, int]]) -> list[str] : 
    premierEspaceVide : int = 0 
    dernierFichierNonBouge : int = len(fichier) - 1

    n, _ = fichier[dernierFichierNonBouge]
    while (n == -1) : 
        dernierFichierNonBouge -= 1 
        n, _ = fichier[dernierFichierNonBouge]
    
    n, _ = fichier[premierEspaceVide]
    while (n != 1) : 
        premierEspaceVide += 1 
        n, _ = fichier[premierEspaceVide]


    def chercheEspaceLibreTailleCorrespondant (taille : int) -> int : 
        # Recherche la première position correspondante à 
        i = 0 
        while i <= dernierFichierNonBouge : 
            n, t = fichier[i]
            if (n == -1) and (t >= taille):
                return i
            i += 1
        return -1
    
    while 0 < dernierFichierNonBouge : 
        n, taille = fichier[dernierFichierNonBouge]
        pos = chercheEspaceLibreTailleCorrespondant(taille)
        if (pos != -1) : 
            # On a trouvé une position valide 
            v, t = fichier[pos]
            if (v != -1) : 
                print("Erreur")
                return False 
            newTaille = t - taille 
            fichier[dernierFichierNonBouge] = (-1, taille)
            if (newTaille == 0) : 
                # On a rempli tout l'espace vide 
                fichier[pos] = (n, taille)

            else : 
                # On a un fichier de plus grande taille que prévu
                fichier[dernierFichierNonBouge] = (-1, taille)
                debut, fin = fichier[:pos], fichier[pos + 1:]
                debut.append((n, taille))
                debut.append((-1, newTaille))
                fichier = debut + fin                 
            
            dernierFichierNonBouge -= 1
        else : 
            dernierFichierNonBouge -= 1
        
        n, _ = fichier[dernierFichierNonBouge]
        while (n == -1) and (premierEspaceVide <= dernierFichierNonBouge): 
            dernierFichierNonBouge -= 1 
            n, _ = fichier[dernierFichierNonBouge]
        
        
    return fichier

print(traduitInput(libereEspaceDisqueP2(lireInput("./Day09/test"))))
print(calculeChecksum(traduitInput(libereEspaceDisqueP2(lireInput("./Day09/input")))))