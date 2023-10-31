lower = int(input("Untere Grenze: "))
upper = int(input("Obere Grenze: "))

for i in range(lower, upper + 1):
    if i % 7 == 0:
        print(i)