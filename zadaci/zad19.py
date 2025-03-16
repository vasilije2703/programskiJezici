import random
import math

karte = []
for boja in ['Herc' , 'Karo' , 'Tref', 'Pik']:
    for broj in range(2,11,1):
        karta = '(' + boja + ')' + str(broj)
        karte.append(karta)

for boja in ['Herc' , 'Karo' , 'Tref', 'Pik']:
    for slika in ['J' , 'Q' , 'K' , 'A']:
        karta = '(' + boja  + ')' + slika
        karte.append(karta)

def izvuci_pet(karte):
    random.shuffle(karte)
    izvucene = []
    for i in range(5):
        izvucena = random.choice(karte)
        while izvucena in izvucene:
              izvucena = random.choice(karte)
        izvucene.append(izvucena)
    
    return izvucene

#print(*(izvuci_pet(karte)))

def full_house():
    tri_iste = math.comb(4,3) * math.comb(13,1)
    dvije_iste = math.comb(4,2) * math.comb(12,1)
    sve_moguce = math.comb(52,5)

    return round(tri_iste * dvije_iste / sve_moguce, 6) * 100

#print(full_house())


def dva_para():
    prvi_par = math.comb(4,2) * math.comb(13,1)
    drugi_par = math.comb(4,2) * math.comb(12,1)
    slobodna_karta = math.comb(11,1) * math.comb(4,1)
    sve_moguce = math.comb(52,5)


    return round(prvi_par*drugi_par*slobodna_karta/sve_moguce, 6) * 100

#print(dva_para())




# Definišemo karte u špilu
def kreiraj_spil():
    boje = ['♠', '♣', '♦', '♥']
    vrednosti = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    spil = [f'{v}{b}' for v in vrednosti for b in boje]
    return spil

# Funkcija koja proverava da li ruka ima dva para
def ima_dva_para(ruka):
    recnik = {k[0]:0 for k in ruka}


    for element in ruka:
        recnik[element[0]] += 1


    br_parova = 0
    for key, value in recnik.items():
        if value == 2:
            br_parova += 1
    

    return br_parova == 2


# Funkcija koja simulira izvlačenje ruke N puta
def simulacija_dva_para(N):
    spil = kreiraj_spil()
    broj_dva_para = 0
    
    for _ in range(N):
        # Nasumično biramo 5 karata iz špila
        ruka = random.sample(spil, 5)
        
        # Ako ruka ima dva para, povećavamo broj
        if ima_dva_para(ruka):
            broj_dva_para += 1
    
    # Verovatnoća je broj uspešnih slučajeva (dva para) podeljeno sa ukupnim brojem simulacija
    verovatnoca = (broj_dva_para / N) * 100
    return verovatnoca

# Pokretanje simulacije sa 10,000 izvlačenja
N = 10000
verovatnoca = simulacija_dva_para(N)
print(f"Verovatnoća da se izvuče Dva para nakon {N} simulacija je: {verovatnoca:.6f}%")


