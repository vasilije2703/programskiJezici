

def rotacija_za_devedeset(matrix):
   n = len(matrix)
   nova_matrica = [[matrix[n - j - 1][i]for j in range(n)] for i in range(n)]
   return nova_matrica

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

new = rotacija_za_devedeset(matrix)

for i in range(len(matrix)):
   for j in range(len(matrix)):
       print(new[i][j], end = " ")
   print()
