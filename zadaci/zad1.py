def savrsen(n):
    a = 1
    b = 1

    for a in range(2, n):
        for b in range(2, n // 2):
            if a ** b == n:
                return True
    return False


print(savrsen(127))