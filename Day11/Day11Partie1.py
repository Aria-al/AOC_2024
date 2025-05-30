def lireInput (filePath : str) -> list[str] : 
    f = open(filePath, "r")
    res = f.read()
    return res.split(" ")


def ruleOfRock (lst : list[str], index : int) -> tuple[list[str], bool] : 
    val = lst[index]
    if int(val) == 0 : 
        lst[index] = "1"
        return (lst, False) 
    elif len(val) % 2 == 0 : 
        v1, v2 = val[:len(val)//2], str(int(val[len(val)//2:]))
        l1, l2 = lst[:index], lst[index + 1:]
        l1.append(v1)
        l1.append(v2)
        return (l1 + l2, True)
    else : 
        lst[index] = str(int(val) * 2024)
        return (lst, False)

def uneIter (lst : list[str]) -> list[str] : 
    i = 0 
    while i < len(lst) : 
        lst, isNew = ruleOfRock(lst, i)
        if (isNew) : 
            i += 1
        i += 1 
    return lst 

rockFile = lireInput("./Day11/input")
for i in range(25) : 
    rockFile = uneIter(rockFile)
    print(len(rockFile))
print(len(rockFile))
