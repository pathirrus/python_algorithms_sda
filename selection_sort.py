# sortowanie selekcyjne minimum

def sort(data: list) -> list:
    for pos in range(len(data)):
        min_idx = pos

        for i in range(pos+1, len(data)):
            if data[i] <= data[min_idx]:
                min_idx = i
        data[pos], data[min_idx] = data[min_idx], data[pos]
        print(data)
    return data


if __name__ == "__main__":
    resoult = sort([10, 1, 4, 9, 20, 15])
    print(resoult)




# zad dom zrobić na max
