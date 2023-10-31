#Steuerprogramm für Lüftersteuerung
rgm_1 = input("Läuft Rauchgasmelder 1? j/n: ").lower().strip() == "j"
rgm_2 = input("Läuft Rauchgasmelder 2? j/n: ").lower().strip() == "j" 

if rgm_1 == False and rgm_2 == False:
    print("Lüfter 1&2 laufen nicht")
elif rgm_1 == False and rgm_2 == True:
    print("Lüfter 1 läuft, Lüfter 2 läuft nicht")
elif rgm_1 == True and rgm_2 == False:
    print("Lüfter 1 läuft, Lüfter 2 läuft nicht")
else:
    print("Lüfter 1&2 laufen")
