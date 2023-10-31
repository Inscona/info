import time

zeit = int(input("Bitte geben Sie die Zeit in Sekunden ein: "))
print("Die Zeit läuft...")

while zeit > 0:
    print(zeit)
    zeit -= 1
    time.sleep(1)

print("Die Zeit ist abgelaufen!")