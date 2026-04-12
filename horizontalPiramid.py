def main():
    try:
        wysokosc = int(input("Podaj wysokość piramidy (liczba całkowita dodatnia): "))
        if wysokosc <= 0:
            print("Wysokość musi być liczbą dodatnią.")
            return
        for i in range(1, wysokosc + 1):
            print('#' * i)
        for i in range(wysokosc - 1, 0, -1):
            print('#' * i)
    except ValueError:
        print("Błąd: Należy podać liczbę całkowitą.")

if __name__ == "__main__":
    main()