import itertools


def nalazi_se(torka, lista):
    lista_perm = list(itertools.permutations(torka))

    for sekvenca in lista_perm:
        if sekvenca in lista:
            return True
    
    return False


def trougao(m):
    lista = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
               if a + b + c == m and a + b > c and a + c > b and a + c > b and a != 0 and b != 0 and c != 0:
                   torka = (a,b,c)
                   if nalazi_se(torka, lista) == False:
                       lista.append(torka)


    print(*lista)

trougao(12)