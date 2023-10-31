# Dieses erste Beispielprojekt soll die grundlegende Arbeit
# mit PyCharm und Debugger demonstrieren.


# Autor: U. Triltsch
# Erstellt am: 04.10.021
# Letzte Aenderung am: 05.10.2021

# Aufgabe: Quadratwurzel annähern mit Heron-Verfahren
def algorithm(number):

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #HIPO- Principle
    #Input
    number = float(input("Please input a number:\n"))
    #Process  --> What is happening here?
    result = algorithm(number)
    #Output
    print("The result of the operation on: ", number, "is: ", result)