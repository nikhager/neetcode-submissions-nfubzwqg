class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            pair = target - n

            if pair in seen:
                return [seen[pair], i]
                
            seen[n] = i