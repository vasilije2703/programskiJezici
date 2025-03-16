m = 4
n = 6
h = 2
w = 3
matrix = [[1,1,1,2,2,2],
 [3,3,3,4,4,4],
 [5,5,5,6,6,6],
 [7,7,7,8,8,8]]


def podijeli(matrix, m, n, h, w):
    izdjeljene = [[[matrix[k + i][l + j] for l in range(w)] for k in range(h)] for i in range(0,m-1,h) for j in range(0, n - 1, w)]
    print(izdjeljene)
       

podijeli(matrix,m,n,h,w)