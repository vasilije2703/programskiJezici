#da li se rotiranjem ciklicno iz jedne liste moze dobiti sortirana lista
from copy import deepcopy

def rotiraj_za_jedan_l(lista):
    temp = lista[0]
    for i in range(len(lista) - 1):
        lista[i] = lista[i+1]
    
    lista[len(lista) - 1] = temp


def rotiraj_za_k_l(lista,k):
    for i in range(k):
        rotiraj_za_jedan_l(lista)


def rotiraj_za_jedan_d(lista):
    temp = lista[len(lista) - 1]
    for i in range(len(lista) - 1,0,-1):
        lista[i] = lista[i-1]

    lista[0] = temp

def rotiraj_za_k_d(lista, k):
    for i in range(k):
        rotiraj_za_jedan_d(lista)
   

def da_li_sortirana(lista,k):
    lista1 = deepcopy(lista)
    lista2 = deepcopy(lista)

    rotiraj_za_k_d(lista1,k)

    if sorted(lista1) == lista1:
        return True, 'desno'
    
    rotiraj_za_k_l(lista2,k)

    if sorted(lista2) == lista2:
        return True, 'lijevo'
    
    return False
    



lista = [1,2,3,4,5]
print(da_li_sortirana(lista,5))          