#lista = [1,2,3,4,5]
#print(*lista)

#d = {"A" : 45, "B" : 'ASfasfasfasf' , "C" : (212121, "asdasd")}

s = "ada sdasd"

def parovi_anagrama(recenica):
    lista_rijeci = recenica.split(" ")
    for index1 in range(len(lista_rijeci) - 1):
        for index2 in range(index1 + 1,len(lista_rijeci)):
            rijec1 = lista_rijeci[index1].strip(":;,.")
            rijec2 = lista_rijeci[index2].strip(";:,.")

            if(sorted(rijec1.lower()) == sorted(rijec2.lower())):
                print(rijec1, " " , rijec2)

recenica = 'Please, be silent and listen to what Dan says'

#parovi_anagrama(recenica)

lista = [x ** 2 for x in range(10)]
# print(lista)

lista2 = [(x, y) for x in [1,2,3] for y in [3, 2 ,4] if x != y]
#print(lista2)


lista_rijeci1 = recenica.split(" ")
n = len(lista_rijeci1)


anagrami = [(lista_rijeci1[i], lista_rijeci1[j]) for i in range(n - 1) for j in range(i + 1, n) if sorted(lista_rijeci1[i].strip(":;.," ).lower()) ==
            sorted(lista_rijeci1[j].strip(":;.," ).lower())]

#print(*anagrami)

matrix = [[[255, 0, 0] , [126, 255, 0]],
            [[127, 255, 128], [255, 255, 255] ]]

rgb2gray = [[sum(row2)/3 for row2 in row] for row in matrix]
#print(rgb2gray

minimum = min([min(row) for row in rgb2gray])
maximum = max([max(row) for row in rgb2gray])
minMaxscale = [[(pix - minimum)/(maximum - minimum) for pix in row]for row in rgb2gray]
#print(minMaxscale)

binarize = [[1 if row[i] > 150 else 0 for i in range(len(row))]for row in rgb2gray]
#print(binarize)

flip = [row[::-1] for row in matrix]
#print(flip)

iterator = list(zip(*matrix))
#print(iterator)

matrix2 = list(zip(*iterator))
#print(matrix2)

torka = ()

a = {x for x in 'abracadabra' if x not in 'abc'}
#print(a)


matrix_proccessor = [[51, 87, 96, 56], [10, 19, 56], [12, 95, 10, 56, 81],
 [90, 61, 25, 10], [25, 82, 61], [86, 93, 25]]

n = len(matrix_proccessor)

pregrijani = {j if j in matrix_proccessor[i+1] and j in matrix_proccessor[i+2] else None  for i in range(n - 2) for j in matrix_proccessor[i] }
pregrijani2 = {j for i in range(n - 2) for j in matrix_proccessor[i] if  j in matrix_proccessor[i+1] and j in matrix_proccessor[i+2]}

#print(pregrijani)
#print(pregrijani2)

id = {x for x in pregrijani if x != None}
#print(id)

overheated = [
    set(matrix_proccessor[i]) & set(matrix_proccessor[i+1]) & set(matrix_proccessor[i+2]) for i in range(n - 2)
]

#print(overheated)
consecutive = [ids for ids in overheated if len(ids) > 0]
consecutive = {id for ids in consecutive for id in ids}      #pomocu skupova rjesenje
#print(consecutive)

histogram = ([1, 2, 3, 2, 4, 3, 5, 4, 6, 1, 2, 5, 3],
[0, 2, 4, 7])
n = len(histogram[1])
d = {(histogram[1][i], histogram[1][i+1]): sum(1 if histogram[1][i]  <= x < histogram[1][i+1] else 0 for x in histogram[0])
 for i in range(n - 1)}
#print(d)

year = 2016
event = "Grand Slam"

# print(f'Results of {year}, {event} are...')

table = {"Mike" : 40002 , "Justin" : 55555, "Joe" : 787878, "Jack" : 74441}

for name, phone in table.items():
    pass
    # print(f'{name:10} ===> {phone:10d}')

# print('We are {} who say "{}"'.format("knights" , "Ni"))

# print('{0} and {1}'.format('eggs' , 'milk'))
# print('{1} and {0}'.format('eggs' , 'milk'))

# print('This {food} is {adjective}'.format(food = 'meat' , adjective = 'dispicable'))

# print('The story of {0} and his {1} was really {adjective}'.format("boy" , "dog" , adjective = "wonderful"))



