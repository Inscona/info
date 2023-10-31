print("Herzlich Willkommen zum Galgenraten!")

wort = input("Bitte geben Sie das zu erratende Wort ein: ")
guess = input("Bitte geben Sie ihren ersten Tipp ab: ")
stelle = 0
Tipp = wort[stelle]

while True :
    if guess == wort :
        print("Sie haben das Wort erraten!")
        break

    else :
        print("Leider haben Sie das Wort nicht erraten! Hier ist ein Tipp:")
        print(Tipp)
        stelle += 1
        Tipp += wort[stelle]

        guess = input("Bitte geben Sie ihren nächsten Tipp ab: ")