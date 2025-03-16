n = 3
matrix =[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]




matrix2 = [[2, 1, 3, 4],
 [1, 3, 4, 2],
 [3, 4, 2, 1],
 [4, 2, 1, 3]]



def validna(matrix,n):
    celije_sudoku = [
             [matrix[i+k][j+l] for l in range(n)for k in range(n)] for i in range(0,n**2,n) for j in range(0,n**2,n)
        ]
    celije = all(len(lista) == len(set(lista)) for lista in celije_sudoku)
    vrste = all(len(vrsta) == len(set(vrsta)) for vrsta in matrix)
    kolone = all(len(kolona) == len(set(kolona)) for kolona in list(zip(*matrix)))
    
    return celije and vrste and kolone 



print(validna(matrix2,2))

































# def podijeli(matrix):
#     podjeljena = [[[matrix[i + k][j + l] for l in range(n)] for k in range(n)] for i in range(0,n**2,n) for j in range(0, n**2, n)]
#     return podjeljena

# def stampa(matrix):
    
#     flag = 0
#     if n == 2:
#         flag = 5
#     else:
#         flag = 7  


#     pola = len(matrix) // 2
#     for index, lista in enumerate(matrix):
#         if index % n == 0 and index != n ** 2 and index != 0:
#             for k in range(n*flag):
#                print('-', end="")
#             print()
        
#         for k in range(len(lista)):
#             print(*lista[k], end = " ")

#             if k != len(lista) - 1:
#                 print("|", end = " ")          

#         print()    

# def validan_sudoku(podijeljena):
#     dimenzija = len(podijeljena)
#     provjera_celija = all( lista1[k] != lista2[k] for row  in podijeljena for i,lista1 in enumerate(row) for j, lista2 in enumerate(row) 
#                           if i != j for k in range(len(lista1)))
#     #provjera_celija1 = sum(element for row in podijeljena for lista in row for element in lista)
#     print(provjera_celija)




# #print(n**2*(n**2+1)/2)
# #validan_sudoku(podijeli(matrix))
