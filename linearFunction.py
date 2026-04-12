import pylab
import numpy as np

def main():
    print("Program do rysowania wykresu funkcji liniowej f(x) = a*x + b")
    try:
        a = float(input("Podaj współczynnik a: "))
        b = float(input("Podaj współczynnik b: "))
        x_min = float(input("Podaj minimalną wartość x: "))
        x_max = float(input("Podaj maksymalną wartość x: "))
        if x_min >= x_max:
            print("Błąd: x_min musi być mniejsze niż x_max.")
            return
        tytul = input("Podaj tytuł wykresu: ")
        odp = input("Czy wyświetlić siatkę pomocniczą? (tak/nie): ").strip().lower()
        grid = odp == "tak"
    except ValueError:
        print("Błąd: Wszystkie wartości muszą być liczbami.")
        return

    x = np.linspace(x_min, x_max, 200)
    y = a * x + b

    pylab.plot(x, y)
    pylab.title(tytul)
    pylab.grid(grid)
    pylab.show()

if __name__ == "__main__":
    main()