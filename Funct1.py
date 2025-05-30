def afficheMat (m : list[list]) -> None : 
    """
    Affiche la matrice passée en paramètres 
    """
    for l in m : 
        s = ""
        for e in l : 
            s = s + str(e) + " "
        print(s)

