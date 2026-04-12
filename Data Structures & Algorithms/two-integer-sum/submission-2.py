class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Given an array of integers nums and an integer target, 
        # return the indices i and j such that nums[i] + nums[j] == target and i != j.
        seen = []
        for i, n in enumerate(nums):
            match = target - n
            if match in seen:
                return [seen.index(match), i]
            seen.append(n)

        # You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
        # Return the answer with the smaller index first.