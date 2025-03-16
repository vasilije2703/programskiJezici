


def najvise_casova(raspored):
    dan = ""
    max_br_casova = 0

    for key, list in raspored.items():
        broj = 0
        for tuple in list:
            broj += tuple[1]
        
        if broj > max_br_casova:
            dan = key
            max_br_casova = broj
    

    return dan, max_br_casova




recnik = {
    "ponedeljak" : [('Strukture podataka' , 3)],
     "utorak" : [("Matematika" , 2)],
     "srijeda" : [('Principi programiranja' , 3)],
     "četvrtak" : [("Matematika" , 2) , ("Principi programiranja" , 3)],
     "petak" : [("Programski jezik Python" , 2), ("Principi programiranja" , 2)]
}

print(najvise_casova(recnik))