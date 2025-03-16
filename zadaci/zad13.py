#flip oko horizontalne ose 

def flip(matrix):
    n = len(matrix)
    nova_mat = [matrix[n - i - 1] for i in range(len(matrix))]
    return nova_mat

matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]
n = len(matrix[0])
m = len(matrix)
nova = flip(matrix)

for i in range(m):
    for j in range(n):
        print(nova[i][j], end=" ")
    print()


