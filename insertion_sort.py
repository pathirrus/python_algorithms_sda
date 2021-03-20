def sort(data: list) -> list:
    for current in range(len(data)):
        key = data[current]
        i = current - 1  # ostatni elementy posortowanej listy

        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = key
    return data


if __name__ == "__main__":
    resoult = sort([10, 1, 4, 9, 20, 15])
    print(resoult)
