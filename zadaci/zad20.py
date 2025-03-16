import json
import math

def pravougaonici():
    f = open('bboxes.txt' , 'r')
    brp = 0
    recnik = {}
    for line in f:
        line = line.strip('\n')
        naziv = 'bbox_' + str(brp)
        brp += 1
        if naziv not in recnik:
           recnik[naziv] = {}
           recnik[naziv]["coords"] = list(line.split(', ')) 

    novi = preklapanja(recnik)
    return recnik

def sadrzi(koordinate1, koordinate2):
    tjeme1 = tuple(koordinate1[:2])
    tjeme2 = tuple(koordinate2[:2])

    sirina1 = int(koordinate1[2])
    visina1 = int(koordinate1[3])

    sirina2 = int(koordinate2[2])
    visina2 = int(koordinate2[3])
    
    razlikax = abs(int(tjeme2[0]) - int(tjeme1[0]))
    razlikay = abs(int(tjeme1[1]) - int(tjeme2[1]))

    if int(tjeme1[0]) < int(tjeme2[0]) and int(tjeme1[1]) > int(tjeme2[1]) and sirina1 > (sirina2 + razlikax) and visina1 > (razlikay + visina2):
        return True
    return False

def preklapanja(recnik):
    for key1, keyUnutrasnji1 in recnik.items():
        for key2, keyUnutrasnji2 in recnik.items():
            if key1 != key2:
                if sadrzi(keyUnutrasnji1["coords"], keyUnutrasnji2['coords']): 
                      if "contains" not in keyUnutrasnji1:
                          keyUnutrasnji1["contains"] = [key2]
                      else:
                          keyUnutrasnji1["contains"].append(key2)    

    return recnik                             




recnik = pravougaonici()
for key, drugiRec in recnik.items():
    print(key, " " , drugiRec)
jsonfile = open("hierarchy.json", 'w')
json.dump(recnik,jsonfile)