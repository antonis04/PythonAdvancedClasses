def main():
    while True:
        try:
            a = int(input("Podaj wysokość pierwszego słupka (a): "))
            if a <= 0 or a >= 20:
                print("Wysokość musi być większa od 0 i mniejsza niż 20.")
                continue
            c = int(input("Podaj wysokość trzeciego słupka (c): "))
            if c <= 0 or c >= 20:
                print("Wysokość musi być większa od 0 i mniejsza niż 20.")
                continue
            if a == c:
                print("Wysokości słupków muszą być różne.")
                continue
            break
        except ValueError:
            print("Podaj liczby całkowite.")

    b = round((a + c) / 2)
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