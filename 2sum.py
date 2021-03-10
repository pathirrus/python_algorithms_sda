# https://leetcode.com/problems/two-sum/


from typing import List, Tuple



def two_sum(nums: List[int], target: int) -> Tuple[int, int]:



#     Rozwiązanie od kogos nmieefektywne, 2 petle to n^2
#     for idx1, num1 in enumerate(nums):
#         for idx2, num2 in enumerate(nums):
#             if idx1 >= idx2:
#                 continue
#             if num1 + num2 == target:
#                 return [idx1, idx2]
#     return None
#



#########################

    # z powodu "in" enumerate to n^2
    # seen = {}
    # for i, val in enumerate(nums):
    #     if target - val in seen:
    #         return [seen[target - val], i]
    #     seen[val] = i
    # return []


 ########################

    # n liniowy
    i, j = 0, len(nums)-1
    data = sorted(nums)
    while i <j:
        value = data[i]+data[j]
        if value > target:
            j -= 1
        if value < target:
            i += 1

        if value == target:
            break
    idx1 = nums.index(data[i])
    if data[i] == data[j]:
        idx2 = nums.index(data[j], idx1+1)
    else:
        idx2 = nums.index(data[j])
    return idx1, idx2

