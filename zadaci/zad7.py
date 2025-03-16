import random 

lista = [random.randint(-5,5) for i in range(10)]
print(lista)

def najcesci(lista):
    max_br = 0
    max_ele = -1
    for element in lista:
       br =  lista.count(element)
       if br > max_br:
           max_br = br
           max_ele = element
    
    return max_ele

print(najcesci(lista))