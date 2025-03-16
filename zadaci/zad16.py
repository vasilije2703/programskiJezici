#najcescu podsekvencu duzine k u binomu


binom = 'CTGACTGTTGCAATGCTG'
k = 3

def najcesci(binom, k):
    max_br = -1
    max_string = ""
    recnik = {}

    for i in range(len(binom)):
        podstring = binom[i:i+k]
        broj_p = binom.count(podstring, i, len(binom) - 1)
        if podstring not in recnik:
            recnik[podstring] = broj_p


    for key, value in recnik.items():
        if value > max_br:
            max_br = value
            max_string = key


    return max_string

print(najcesci(binom,k))