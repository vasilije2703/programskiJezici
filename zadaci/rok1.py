

def palindrom(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string)-1-i]:
            return False
        
    return True



def izbaci_parne_cifre(n):
    lista = []
    listap = []
    while n > 0:
        lista.append(n % 10)
        if (n % 10) % 2 == 0:
            listap.append(n % 10)

        n = n // 10
    
    for broj in listap:
        lista.remove(broj)
    
       

    k = 0
    broj = 0
    for br in lista:
        broj += br*(10**k)
        k += 1

    return broj





#provjerava je li uneseni string oblika a**2n-b**n
def provjera_stringa(string):    
    br = string.count('-')
    if br != 1:
        return 'NE'
    
    index = string.find('-')
    if string[index-1] != 'a' or string[index+1] != 'b':
        return 'NE'
    
    for slovo in string:
        if slovo not in ['a' , 'b', '-']:
            return "NE"
        
    brb = string.count('b')
    bra = string.count('a')

    if bra != 2*brb:
        return 'NE'
    
    return 'DA'


#sortiraj valjak lista
def zapremina(torka):
    r, h = torka
    return r**2 * h

def sortiraj(lista):
    lista = sorted(lista, key=zapremina,reverse=True)
    return lista

#print(palindrom('anavolimiolovana'))
# print(izbaci_parne_cifre(27523221))
# print(provjera_stringa("aaaa-b-b"))
# lista = [(3,5) , (4,4), (2,6), (5,2)]
# print(sortiraj(lista))
import random
from copy import deepcopy
import json

def importujason(recnik):
    n = len(recnik)
    for i in range(1,11,1):
        naziv_fajla = 'config_' + str(i) + '.json'
        index_ime = n
        config = deepcopy(recnik)
        for j in range(n):
            kljuc = 'block_' + str(index_ime)
            index_ime -= 1

            config[kljuc]["kernels"] = random.choice(recnik[kljuc]["kernels"])
            config[kljuc]["filters"] = random.choice(recnik[kljuc]["filters"])
            config[kljuc]["layers"] = random.choice(recnik[kljuc]["layers"])
        
        f = open(naziv_fajla, 'w')
        json.dump(config, f)
        f.close





recnik = {

 "block_1": {"layers": [1, 2], "filters": [8, 16, 32], "kernels": [1, 3]},
 "block_2": {"layers": [1, 2, 3], "filters": [8, 16, 32, 48], "kernels": [1, 3, 5]},
 "block_3": {"layers": [1, 2, 3, 4], "filters": [8, 16, 32, 48, 64], "kernels": [3, 5]}

}
# importujason(recnik)

# for i in range(1,11,1):
#     print(f'Konfiguracija {i}:')
#     ime = 'config_' + str(i) + '.json'
#     f = open(ime, 'r')
#     konfiguracija = json.load(f)
#     for key, item in konfiguracija.items():
#         print(key, item)






from itertools import permutations
import time
import math
def benchmark(n,m):
    perm = list(permutations(range(1,n+1)))

    tpetlje = time.perf_counter()
    for i in range(m):
        lista = []
        for permutacija in perm:
                if permutacija[0] % 2 == 0 and permutacija[-1] % 2 == 1:
                    lista.append(permutacija)

    tpetljekraj = time.perf_counter()    


    prosjecno_vrijeme_petlje = (tpetljekraj - tpetlje) / m
    print(prosjecno_vrijeme_petlje)


    tComp = time.perf_counter()
    for i in range(m):
        izraz = [permutacija for permutacija in perm if permutacija[0] % 2 == 0 and permutacija[-1] % 2 == 1]
    
   
    tCompkraj = time.perf_counter()

    prosjecno_vrijeme_comp = (tCompkraj - tComp) / m

    print(prosjecno_vrijeme_comp)

    return round((abs(prosjecno_vrijeme_comp - prosjecno_vrijeme_petlje) / prosjecno_vrijeme_petlje) * 100, 5)
        


print(benchmark(15,10))    