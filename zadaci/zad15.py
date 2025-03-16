#unija recnika

lista_recnika =  [{'a':2, 'b':1, 'c':1}, {'a': 3, 'c': 2}, {'b': 4}]

def unija_recnika(lista):
    novi_rec = {}
    for recnik in lista:
        for key,value in recnik.items():
            if key not in novi_rec:
                novi_rec[key] = value
            else:
                novi_rec[key] += value
    
    return novi_rec


print(unija_recnika(lista_recnika))

