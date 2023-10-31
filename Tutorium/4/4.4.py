min = int(input("Untere Grenze: "))
max = int(input("Obere Grenze: "))
sum = 0

if min > max:
    min, max = max, min

for i in range(min, max + 1):
    sum += i

print(sum)