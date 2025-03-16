import re 

def readReport (string) : 
    l = re.split(" ", string) 
    for i in range(len(l)) : 
        l[i] = int(l[i])
    return l 

print(readReport("1 2 33 2"))

def isSafe1 (arr) : 
    diff = arr[0] - arr[-1]
    # Le rapport est croissant 
    if (diff < 0) : 
        for i in range (len(arr) - 1) : 
            inc = arr[i+1] - arr[i]
            if ((inc < 1) or (inc > 3)) : 
                return False 
        return True 
    # Le rapport est décroissant 
    elif (diff > 0) : 
        for i in range (len(arr) - 1) : 
            dec = arr[i] - arr[i+1] 
            if (dec < 1) or (dec > 3) : 
                return False 
        return True 
    else : 
        return False 

# Copie la liste arr en omettant l'élément r 
def copieOmission (arr, r) : 
    res = []
    d = 0 
    if (r == 0) : 
        d+=1
    for i in range (d, len(arr)) : 
        if (i != r) : 
            res.append(arr[i])
    return res 


def isSafe2 (arr) : 
    diff = arr[0] - arr[-1]
    # Le rapport est croissant 
    if (diff < 0) : 
        for i in range (len(arr) - 1) : 
            inc = arr[i+1] - arr[i]
            if ((inc < 1) or (inc > 3)) : 
                return isSafe1(copieOmission(arr, i+1)) or isSafe1(copieOmission(arr, i))
        return True 
    # Le rapport est décroissant 
    elif (diff > 0) : 
        for i in range (len(arr) - 1) : 
            dec = arr[i] - arr[i+1] 
            if (dec < 1) or (dec > 3) : 
                return isSafe1(copieOmission(arr, i+1)) or isSafe1(copieOmission(arr, i))
        return True 
    else : 
        return False 


fichier = open("./Day2/input", "r") 
nbSafe = 0
for line in fichier : 
    arr = readReport(line) 
    if (isSafe2(arr) == True) : 
        nbSafe += 1 
print(nbSafe)