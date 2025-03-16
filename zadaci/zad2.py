def prost(n):
    if n == 1:
        return False
    
    if n == 2:
        return True
    
    for i in range(2, n // 2):
        if n % i == 0:
            return False
        
   
    return True

def desno_skrativ(n):
    if prost(n) == False:
        return 'Ne'
     

    while n > 0:
        n = n // 10
        if prost(n) == False:
            return 'Ne'
        
    return 'Da'


print(desno_skrativ(3118))