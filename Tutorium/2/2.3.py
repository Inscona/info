import math
hypotenuse = float(input("Geben Sie einen Wert für die Länge der Hypotenuse an: "))
angle_deg = float(input("Geben Sie einen Wert für den Winkel im Gradmaß ein: "))

angle_rad = angle_deg * (math.pi / 180)

gegkath = math.sin(angle_rad) * hypotenuse
ankath = math.cos(angle_rad) * hypotenuse

umfang = gegkath + ankath + hypotenuse
flaeche = 0.5 * gegkath * ankath

print("Der Umfang beträgt: ", umfang)
print("Die Fläche beträgt: ", flaeche)