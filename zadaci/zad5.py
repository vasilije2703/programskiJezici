#najduzi podstring koji je palindrom

def palindrom(string):
    n =len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
        
    return True

def najduzi_polindrom(string):
    max_d = 0
    najduzi = ""
    n = len(string)

    for d in range(n,0,-1):
        for i in range(n):
            substring = string[i:d]
            # print(substring)
            if palindrom(substring) and len(substring) > max_d:
                max_d = len(substring)
                najduzi = substring

    return najduzi
                
            

print(najduzi_polindrom('noonracecarlevel'))