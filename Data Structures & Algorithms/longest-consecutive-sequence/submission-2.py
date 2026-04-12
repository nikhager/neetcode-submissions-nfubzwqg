class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Given an array of integers nums, 
        # return the length of the longest consecutive sequence of elements that can be formed.

        # A consecutive sequence is a sequence of elements in which 
        # each element is exactly 1 greater than the previous element.
        # The elements do not have to be consecutive in the original array.
        
        nums_set = set(nums)
        best = 0

        for n in nums_set:
            if n-1 not in nums_set:  # only start counting at sequence starts
                length = 1
                while n + length in nums_set:
                    length += 1
                best = max(best, length)

        return best