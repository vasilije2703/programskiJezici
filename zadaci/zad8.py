#od zadate svaki element ponovi k puta uzastopno

def ponovi_k_puta(lista, k):
    nova = [x for x in lista for i in range(k)]

    return nova

lista = [1,2,3]
print(ponovi_k_puta(lista, 7))