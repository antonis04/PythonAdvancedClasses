import string

tekst = input("Wpisz dowolny tekst: ")

litery = [znak for znak in tekst if znak.isalpha()]
znaki_interpunkcyjne = [znak for znak in tekst if znak in string.punctuation]

print(f"a) Liczba liter: {len(litery)}")
print(f"   Liczba znaków interpunkcyjnych: {len(znaki_interpunkcyjne)}")

spacje = tekst.count(' ')
print(f"b) Liczba spacji: {spacje}")

wyrazy = [wyraz for wyraz in tekst.split() if wyraz]
print(f"c) Liczba wyrazów: {len(wyrazy)}")

if wyrazy:
    czestosc = {}
    for znak in tekst:
        if znak.isalpha():
            znak = znak.lower()
            czestosc[znak] = czestosc.get(znak, 0) + 1
    print("d) Częstotliwość liter:")
    for litera, ile in sorted(czestosc.items()):
        print(f"   {litera}: {ile}")
else:
    print("d) Brak liter do analizy.")