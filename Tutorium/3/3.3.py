import time

zeit = int(input("Bitte geben Sie die Zeit in Sekunden ein: "))
print("Die Zeit läuft...")

for t in range(zeit, 0, -1):
    print(t)
    time.sleep(1)

print("Die Zeit ist abgelaufen!")