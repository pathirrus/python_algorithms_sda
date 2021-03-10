from typing import List, Tuple


def belongs(value: float, segment: Tuple[float, float]) -> bool:
    left, right = segment
    return left <= value < right


def merge(segments: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    result = [segments[0]]

    for segment in segments[1:]:
        left, right = segment
        last_segment = result[-1]

        if not belongs(left, last_segment):
            result.append(segment)
            continue

        if not belongs(right, last_segment):
            new_segment = (last_segment[0], right)
            result.pop()
            result.append(new_segment)

    return result


def test_merge_1():
    expected = [(1, 5), (10, 30)]
    result = merge([(1, 5), (2, 4), (10, 20), (12, 30)])

    assert result == expected


def test_merge_2():
    expected = [(1, 2), (3, 4), (10, 20)]
    result = merge([(1, 2), (3, 4), (10, 20)])
    assert result == expected


if __name__ == "__main__":
    test_merge_1()
    test_merge_2()