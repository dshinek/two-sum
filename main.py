from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], index]
        num_index[num] = index
    return []