import random


def sort(data: list, left: int, right: int) -> list:
    if left>=right:
        return data

    pivot = data[random.randint(left, right)]  # wiodący element
    print(f"Pivot: {pivot}, {data}")


    # data[i] <= pivot < data[i]
    i, j = left, right
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    sort(data, left, j)
    sort(data, i, right)

    return data

def quick_sort(data: list) -> list:
    return sort(data, 0, len(data)-1)


if __name__ == "__main__":
    data = [6, 3, 1, 9, 2]
    result = quick_sort(data)
    print(result)
