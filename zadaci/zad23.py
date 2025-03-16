
p = [0, 0.5, -1, 1] 
q = [1.5, -2, 2] 
def mnozenje_polinoma(p,q):
    proizvod = [sum(p[i] * q[j] for i in range(len(p)) for j in range(len(q))  if i + j == k) for k in range(len(p) + len(q) -1)]
    return proizvod

print(mnozenje_polinoma(p,q))