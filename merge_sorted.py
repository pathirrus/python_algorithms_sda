from typing import Tuple


def merge(a: list, b: list) -> list:
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    # if len(a) > len(b):
    #     return merge(b, a)

    result = []
    size1, size2 = len(a), len(b)
    i, j = 0, 0
    while i < size1 and j < size2:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1

    if i < size1:  # dzięki a[i:] warunek nie jest konieczny, można zostawić samo result.extend
        result.extend(a[i:])
    if j < size2:
        result.extend(b[j:])

    # while i < size1:
    #     result.append(a[i])
    #     i += 1
    # while j < size2:
    #     result.append(b[j])
    #     j += 1

    return result


def partition(data: list) -> Tuple[list, list]:
    middle = len(data) // 2
    return data[:middle], data[middle:]


def sort(data: list) -> list:
    if len(data) == 0 or len(data) == 1:  # inny zapis: if len(data) in [0,1]
        return data

    left, right = partition(data)
    print(left,right)
    return merge(sort(left), sort(right))


if __name__ == "__main__":
    result = sort([10, 11, 22, 1, 3, 0])
    print(result)
