
while True:
    try:
        broj = int(input("Unesite broj "))
        break
    except ValueError:
        print("Desila se greska prilikom unosa, unesite ponovo")
    