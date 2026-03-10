from itertools import combinations

niu = "127859"

cyfry = list(set(int(c) for c in niu))
print("Unikalne cyfry z NIU:", cyfry)

try:
    x = int(input("Podaj liczbę: "))
except ValueError:
    print("To nie jest poprawna liczba.")
    exit()

pary_sum = []
pary_prod = []

for a, b in combinations(cyfry, 2):
    if a + b == x:
        pary_sum.append((a, b))
    if a * b == x:
        pary_prod.append((a, b))

print(f"\nDla liczby {x}:")
if pary_sum:
    print(f"a) Istnieją pary cyfr, których suma daje {x}:")
    for a, b in pary_sum:
        print(f"   {a} + {b} = {x}")
else:
    print("a) Brak pary cyfr o takiej sumie.")

if pary_prod:
    print(f"b) Istnieją pary cyfr, których iloczyn daje {x}:")
    for a, b in pary_prod:
        print(f"   {a} * {b} = {x}")
else:
    print("b) Brak pary cyfr o takim iloczynie.")