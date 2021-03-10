# wyszukiwanie binarne - warto umić
from typing import List, Optional


def search(items: List[int], target: int) -> Optional[int]:
    left, right = 0, len(items) - 1
    count = 0
    while left <= right:                #złożonośc logarytm dwójkowy od n: log2 n
        count += 1
        #middle = (right + left) // 2     #<- python sobie poradzi w innych jezykach moze dojsc do przepelnienia
        middle = left + (right-left)//2     # tutaj w innychj językach nie dojdzie do przepełnienia (np. int16)

        if items[middle] == target:
            print(count)
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


if __name__ == '__main__':
    data = list(range(1000))

    assert search(data, 1001) is None
    assert search(data, 10) == 10

    print("Succes")
