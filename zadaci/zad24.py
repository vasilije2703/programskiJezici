import json
from copy import deepcopy
import random

def importuj_u_jason(obrada_slike):
    duzina = len(obrada_slike)  
   
    for i in range(1,11,1):
        config = deepcopy(obrada_slike)  
        ime_fajla = "config_" + str(i) +'.json'
        br_naziv = duzina
        for j in range(duzina):
            naziv = "block_" + str(br_naziv)
            
            config[naziv]["kernels"] = random.choice(obrada_slike[naziv]["kernels"])
            config[naziv]["filters"] = random.choice(obrada_slike[naziv]["filters"])
            config[naziv]["layers"] = random.choice(obrada_slike[naziv]["layers"])
            
            br_naziv -= 1

        f = open(ime_fajla, 'w')
        json.dump(config, f)
        f.close()
       

recnik = {

 "block_1": {"layers": [1, 2], "filters": [8, 16, 32], "kernels": [1, 3]},
 "block_2": {"layers": [1, 2, 3], "filters": [8, 16, 32, 48], "kernels": [1, 3, 5]},
 "block_3": {"layers": [1, 2, 3, 4], "filters": [8, 16, 32, 48, 64], "kernels": [3, 5]}
}
importuj_u_jason(recnik)

for i in range(1,11,1):
    print(f"Konfiguracija {i}:")
    ime = 'config_' + str(i) + '.json'
    f = open(ime, 'r')
    konfiguracija = json.load(f)
    for key, item in konfiguracija.items():
        print(key, " ", item)
    
    print()
