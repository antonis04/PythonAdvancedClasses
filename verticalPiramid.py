def main():
    try:
        wysokosc = int(input("Podaj wysokość piramidy (liczba całkowita dodatnia): "))
        if wysokosc <= 0:
            print("Wysokość musi być liczbą dodatnią.")
            return
        for y in range(wysokosc - 1, -1, -1):
            for x in range(1, 2 * wysokosc):
                if x > y and x < (2 * wysokosc - y):
                    print('#', end='')
                else:
                    print(' ', end='')
            print()
    except ValueError:
        print("Błąd: Należy podać liczbę całkowitą.")

if __name__ == "__main__":
    main()