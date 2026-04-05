NIU = "127859"


def bubble_sort_ascending(numbers):
    arr = numbers.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_descending(numbers):
    arr = numbers.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    original = []
    for c in NIU:
        d = int(c)
        if d not in original:
            original.append(d)

    asc = bubble_sort_ascending(original)
    desc = bubble_sort_descending(original)

    print(f"Lista unikalnych cyfr NIU: {original}")
    print(f"Lista posortowana rosnąco: {asc}")
    print(f"Lista posortowana malejąco: {desc}")


if __name__ == "__main__":
    main()
