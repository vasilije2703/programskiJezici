#rijec sa najvise samoglasnika u recenici

recenica = input()

def broj_samoglasnika(rijec):
    broj = 0
    samoglasnici = 'AEIOUaeiou'

    for i in range(len(rijec)):
        if rijec[i] in samoglasnici:
            broj += 1
   
    return broj

def najvise_samoglasnika(recenica):
    lista_rijeci = recenica.split()
    najvise_s = ""
    max_s = -1

    for rijec in lista_rijeci:
        rijec1 = rijec.strip(":;,.!?")
        broj = broj_samoglasnika(rijec)
        if broj > max_s:
            max_s = broj
            najvise_s = rijec

    return najvise_s

print(najvise_samoglasnika(recenica))
