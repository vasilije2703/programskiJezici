from copy import deepcopy
def tabla(n,k):
    #k dimenzija celije sa 1
    # n koliko takvih celija imamo po vrstama i kolonama
    tabla_sah = [[1-(i//k + j//k)%2  for j in range(n*k)] for i in range(n*k)]

    
    for i in range(len(tabla_sah)):
       for j in range(len(tabla_sah[0])):
           print(tabla_sah[i][j] , end= " ")
       print()

tabla(3,2)