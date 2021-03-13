def sort(data: list) -> list:
    right_border = len(data)-1
    sweep = True
    while sweep:
        sweep = False
        for i in range(right_border):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                sweep = True
        right_border -=1
    return data


if __name__ == "__main__":
    print(sort([5, 4, 3, 2, 1]))
    # sort([5, 4, 3, 2, 1])
