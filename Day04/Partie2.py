fichier = open("input", "r")

def carMat (i, j, m) : 
    if (i < 0) or (i >= len(m)) : 
        return "b"
    elif (j < 0) or (j >= len(m[i])) : 
        return "b"
    return m[i][j]

def estXMAS (i, j, m) :
    if (carMat(i, j, m) != 'A') :
        return False 
    MAS = "MAS"
    SAM = "SAM"
    dp, do = "" + carMat(i-1, j-1, m) + "A" + carMat(i+1, j+1, m), "" + carMat(i-1, j+1, m) + "A" + carMat(i+1, j-1, m)
    dec = ((dp != MAS) and (dp != SAM)) or ((do != MAS) and (do != SAM))
    return not dec

def part2 () :
    m = []
    for line in fichier : 
        m.append(line)
    nbMatched = 0
    for i in range(len(m)) : 
        for j in range(len(m[0])) : 
            if (estXMAS(i, j, m)) : 
                nbMatched += 1 
    return nbMatched

print(part2())