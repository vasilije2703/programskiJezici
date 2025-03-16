import random

def popuni_matricu(m,n,k):
    matrix = [[random.randint(-k,k) for j in range(n)] for i in range(m)]
    return matrix


matrix = popuni_matricu(4,5,10)
print(*matrix, end='\n')