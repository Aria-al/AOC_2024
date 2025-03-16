import re 

fichier = open("./Day3/input", "r") 

def Part1 () : 

    rule1 = r"mul\(\d+,\d+\)"
    rule2 = r"mul\((\d+),(\d+)\)"
    res = 0 
    for l in fichier : 
        array = re.findall(rule1, l)
        # 
        for el in array : 
            temp = re.findall(rule2, el)
            a, b = int(temp[0][0]), int(temp[0][1])
            res += a * b 
    print(res)