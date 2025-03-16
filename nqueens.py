import random
import itertools



sah = {'K' : 1 , 'R' : 2, 'P' : 1, 'k' : 1, 'r' : 1, 'n' : 1, 'p': 2}
tabla = [['.' for j in range(8)] for i in range(8)]
# print(tabla)

for key,value in sah.items():
    for k in range(value):
        i_n = random.choice(range(8))
        j_n = random.choice(range(8))
        while tabla[i_n][j_n] != '.':
            i_n = random.choice(range(8))
            j_n = random.choice(range(8))

        tabla[i_n][j_n] = key    
    
    
# for i in range(8):
#     for j in range(8):
#         print(tabla[i][j], end='|')
#     print()

n = 4
rasporedi = list(itertools.permutations(range(n)))
#print(rasporedi)

def check(raspored):
    for col1, row1 in enumerate(raspored):
        for col2, row2 in enumerate(raspored[col1+1:],col1+1):
            if row1 == row2:
                return False
            
            if abs(col1 - col2) == abs(row1 - row2):
                return False

    return True        

validni_rasporedi = [raspored for raspored in rasporedi if check(raspored)]

def print_raspored(raspored):
    tabla = [['.' for i in range(n)] for j in range(n)]
    
    for col, row in enumerate(raspored):
        tabla[col][row] = 'Q'


    for i in range(n):
        for j in range(n):
            print(tabla[i][j], end=" ")
        print() 



for raspored in validni_rasporedi:
    print_raspored(raspored)         
    print()







