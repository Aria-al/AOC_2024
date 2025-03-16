import re 

fichier = open("./Day1/input", "r")
left, right = [], []
for ligne in fichier : 
    l, r = re.split("   ", ligne)
    left.append(int(l)) 
    right.append(int(r)) 

left.sort()
right.sort()
total = 0 



# Stocke le nombre de fois que arr[i] est présent 
arr = [-1] * 100000
for i in range (len(left)) : 
    if (arr[left[i]] != -1) : 
        total += left[i] * arr[left[i]] 
    else : 
        v = 0 
        for j in range (len(left)) : 
            if (right[j] == left[i]) : 
                v += 1 
        arr[left[i]] = v 
        total += left[i] * v 

print(total)