def main():
    while True:
        try:
            a = int(input("Podaj wysokość pierwszego słupka (a): "))
            b = int(input("Podaj wysokość drugiego słupka (b): "))
            if not (0 <= a < 9 and 0 <= b < 9):
                print("Wysokość każdego słupka musi być większa lub równa 0 i mniejsza niż 9.")
                continue
            if a == b:
                print("Wysokości słupków muszą być różne.")
                continue
            break
        except ValueError:
            print("Podaj liczby całkowite.")

    c = abs(a - b)
    wysokosci = [a, b, c]
    maks = max(wysokosci)
    szerokosc = 5

    for y in range(maks, 0, -1):
        linia = ""
        for h in wysokosci:
            if y > h:
                linia += " " * szerokosc
            elif y == h:
                linia += "+" + "-" * (szerokosc - 2) + "+"
            else:
                linia += "|" + " " * (szerokosc - 2) + "|"
        print(linia)

    dol = ""
    for _ in wysokosci:
        dol += "+" + "-" * (szerokosc - 2) + "+"
    print(dol)

if __name__ == "__main__":
    main()