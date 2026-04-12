class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Given an array of integers nums, 
        # return the length of the longest consecutive sequence of elements that can be formed.

        # A consecutive sequence is a sequence of elements in which 
        # each element is exactly 1 greater than the previous element.
        # The elements do not have to be consecutive in the original array.
        
        if len(nums) == 0:
            return 0

        nums_sorted = sorted(set(nums))
        seen = {nums_sorted[0]:1}

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i-1]+1:
                seen[nums_sorted[i]] = seen[nums_sorted[i-1]] + 1
            else:
                seen[nums_sorted[i]] = 1

        return max(seen.values())