#n duzina liste
#broj k sa kojim je n djeljivo
#podijeliti na disjunktne liste od po k elemenata prvo for petljama pa list comprehensionom

lista = [1,2,3,4,5,6]
k = 3




def petlje_res(lista,k):
    nova_lista = []
    broj_listi = len(lista) // k
    
    for i in range(broj_listi):
        manja_lista = []
        for j in range(k):
            manja_lista.append(lista[j])
        
        nova_lista.append(manja_lista)
        lista = lista[k:]
    
    return nova_lista

def list_comp(lista,k):
    nova_lista = [[lista[j] for j in range(i, i + k)] for i in range(0, len(lista), k)]

    return nova_lista

print(*petlje_res(lista,k))
print(*list_comp(lista,k))

    