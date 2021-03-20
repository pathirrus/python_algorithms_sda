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


def median(left: list, right: list) -> float:
    data = merge(left, right)
    size = len(data)
    if size == 1:
        return data[0]

    if size % 2 == 1:
        return data[size // 2]

    l, r = (size-1) // 2, (size+1)//2

    return (data[l]+data[r])//2

if __name__ == "__main__":
    a = [1, 11, 13, 34, 100, 101, 102]
    b = [10, 20, 30, 31, 42]

    result = median(a, b)

    print(result)
