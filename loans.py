def calculate_loan_installments(loan_amount, years, annual_interest, installment_type):
    miesiecy = years * 12
    oproc_mies = annual_interest / 100 / 12

    print("\nParametry kredytu:")
    print(f"Kwota: {loan_amount:.2f} zł")
    print(f"Lata: {years}")
    print(f"Oprocentowanie roczne: {annual_interest:.2f}%")
    print(f"Typ raty: {installment_type}")

    if installment_type == "stałe":
        if annual_interest == 0:
            rata_stala = loan_amount / miesiecy
            suma_odsetek = 0
        else:
            czynnik = (1 + oproc_mies) ** miesiecy
            rata_stala = loan_amount * (oproc_mies * czynnik) / (czynnik - 1)
            suma_odsetek = rata_stala * miesiecy - loan_amount
        print(f"Całkowity koszt kredytu (odsetki): {suma_odsetek:.2f} zł\n")
        print("Nr | Część kapitałowa | Część odsetkowa | Rata | Kapitał pozostały")
        pozostaly = loan_amount
        for i in range(1, miesiecy + 1):
            if annual_interest == 0:
                czesc_odsetkowa = 0
                czesc_kapitalowa = rata_stala
            else:
                czesc_odsetkowa = pozostaly * oproc_mies
                czesc_kapitalowa = rata_stala - czesc_odsetkowa
            if i == miesiecy:
                czesc_kapitalowa = pozostaly
                rata_stala = czesc_kapitalowa + czesc_odsetkowa
            pozostaly -= czesc_kapitalowa
            if pozostaly < 0:
                pozostaly = 0
            print(f"{i:2d} | {czesc_kapitalowa:10.2f} | {czesc_odsetkowa:10.2f} | {rata_stala:10.2f} | {pozostaly:10.2f}")

    else:  # malejące
        stala_czesc_kapitalowa = loan_amount / miesiecy
        raty = []
        pozostaly_temp = loan_amount
        suma_odsetek = 0
        for i in range(1, miesiecy + 1):
            czesc_odsetkowa = pozostaly_temp * oproc_mies
            czesc_kapitalowa = stala_czesc_kapitalowa
            if i == miesiecy:
                czesc_kapitalowa = pozostaly_temp
            rata = czesc_kapitalowa + czesc_odsetkowa
            pozostaly_temp -= czesc_kapitalowa
            if pozostaly_temp < 0:
                pozostaly_temp = 0
            raty.append((i, czesc_kapitalowa, czesc_odsetkowa, rata, pozostaly_temp))
            suma_odsetek += czesc_odsetkowa
        print(f"Całkowity koszt kredytu (odsetki): {suma_odsetek:.2f} zł\n")
        print("Nr | Część kapitałowa | Część odsetkowa | Rata | Kapitał pozostały")
        for nr, kap, odsetki, rata, pozostaly in raty:
            print(f"{nr:2d} | {kap:10.2f} | {odsetki:10.2f} | {rata:10.2f} | {pozostaly:10.2f}")


while True:
    try:
        kwota = float(input("Podaj kwotę kredytu: "))
        if kwota <= 0:
            raise ValueError
    except ValueError:
        print("Kwota kredytu musi być liczbą dodatnią!")
        continue

    try:
        lata = int(input("Podaj liczbę lat: "))
        if lata <= 0:
            raise ValueError
    except ValueError:
        print("Liczba lat musi być liczbą dodatnią!")
        continue

    try:
        procent = float(input("Podaj procent w skali roku: "))
        if procent < 0:
            raise ValueError
    except ValueError:
        print("Procent w skali roku musi być liczbą nieujemną!")
        continue

    typ_raty = input("Podaj typ raty (stałe/malejące): ")
    if typ_raty not in ["stałe", "malejące"]:
        print("Typ raty to 'stałe' albo 'malejące'!")
        continue

    calculate_loan_installments(kwota, lata, procent, typ_raty)
    break