# silnia 5! = 5*4*3*2*1 = 120


# silnia liczona iteracyjnie
def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1

    p = 1
    for i in range(2, n+1):
        p *= i
    return p

#Wersja rekurencyjna (rekurencja: funkcja wywołuje sama siebie):
#n!= n * (n-1)!

def factorial_2(n) -> int:
    if n in [0, 1]:
        return 1
    return n*factorial_2(n-1)


if __name__ == '__main__':
    print(factorial_2(5))
