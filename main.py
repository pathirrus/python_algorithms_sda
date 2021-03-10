def asbin(n: int) -> str:
    if n == 0 or n == 1:
        return "0b" + str(n)
    result = []

    while n != 0:
        # reminder = n % 2
        # n = n // 2              # // <- operator do dzielenia w liczbach calkowitych
        n, reminder = divmod(n, 2)  # zastępuje 2 górne linijki
        result.append(str(reminder))

    return "0b" + "".join(result[::-1])


def asternary(n: int) -> str:  # 0t
    if n in [0, 1, 2]:
        return f"0t{str(n)}"
    result = ""

    while n != 0:
        n, reminder = divmod(n, 3)
        result += str(reminder)

    return f"0t{result[::-1]}"


def ashex(n: int) -> str:  # 0x
    mapping = {i: str(i) for i in range(10)}
    mapping.update({
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    })
    if n in mapping:
        return f"0x{mapping[n]}"

    result = ""
    while n != 0:
        n, reminder = divmod(n, 16)
        result += str(mapping[reminder])

    return f"0t{result[::-1]}"




if __name__ == '__main__':
    print(bin(10))
    print(asbin(10))
    print(asternary(10))
    print(ashex(44))
