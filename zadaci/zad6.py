#k preplitanje stringova

def k_preplitanje(string1, string2, k):
    n1 = len(string1) // k
    n2 = len(string2) // k

    novi_string = ""

    iterator = 0
    while(iterator < k):

        for i in range(n1):
            novi_string += string1[i]
        
        for j in range(n2):
            novi_string += string2[j]

        iterator += 1
        string1 = string1[n1:]
        string2 = string2[n2:]

    return novi_string


string1 = 'nizovi'
string2 = 'stringovi'
print(k_preplitanje(string1, string2, 3))