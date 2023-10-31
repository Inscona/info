from matplotlib import pyplot as plt

Modelle = ["Mitsubishi\nOutlander", "BMW 5-er\nSerie", "MINI\nCountryman", "BMW 2-er\nSerie", "Volvo XC60"]
Verkaufszahlen = [34000, 13700, 13400, 13300, 11600]

plt.bar(Modelle, Verkaufszahlen)
plt.title("Verkaufszahlen Plug-In-Hybride 2019")
plt.ylabel("Verkaufszahlen")
plt.xlabel("Modelle")
plt.show()