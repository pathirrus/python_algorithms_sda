#VER2 błędna sekwencja -> ([)] itp
# poprawna sekwencja {} [] () ||

def validate(sequence: str) -> bool:
    stack = []
    for char in sequence:
        if char not in ["(", ")"]:
            continue
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    assert validate("(()){}[]") == True
    assert validate("())") == False
    assert validate("))(") == False
