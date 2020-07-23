"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_len: int = len(nums)
        for start_idx in range(0, list_len):
            for idx in range(start_idx + 1, list_len):
                if nums[start_idx] + nums[idx] == target:
                    return [start_idx, idx]


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([12, 476, 1, 67, 235], 543) == [1, 3]
