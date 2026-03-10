from datetime import date

dane_wejsciowe = input("Podaj swoje imię (pełne, nie zdrobnienie) i nazwisko (w jednej linii): ")
czesci = dane_wejsciowe.split()

imie = czesci[0]
nazwisko = " ".join(czesci[1:])

rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

aktualny_rok = date.today().year
wiek = aktualny_rok - rok_urodzenia
dlugosc_imienia = len(imie)
dlugosc_nazwiska = len(nazwisko)
nazwisko_duze = nazwisko.upper()

if imie.endswith('a'):
    plec = "kobieta"
else:
    plec = "mężczyzna"

if wiek >= 18:
    roznica = wiek - 18
    info_pelnoletnosc = f"Jesteś pełnoletni/a od {roznica} lat."
else:
    roznica = 18 - wiek
    info_pelnoletnosc = f"Nie jesteś jeszcze pełnoletni/a. Do pełnoletności brakuje Ci {roznica} lat."

print("\n" + "="*40)
print("Twoje dane:")
print("="*40)
print(f"Imię: {imie}")
print(f"Nazwisko: {nazwisko}")
print(f"Nazwisko dużymi literami: {nazwisko_duze}")
print(f"Długość imienia: {dlugosc_imienia} litery/ów")
print(f"Długość nazwiska: {dlugosc_nazwiska} litery/ów")
print(f"Rok urodzenia: {rok_urodzenia}")
print(f"Wiek: {wiek} lat")
print(f"Prawdopodobna płeć: {plec}")
print(f"Pełnoletność: {'Tak' if wiek >= 18 else 'Nie'}")
print(f"-> {info_pelnoletnosc}")
print("="*40)