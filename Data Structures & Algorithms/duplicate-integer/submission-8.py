class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if any value appears more than once in the array, return true 
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)

        # otherwise return false.
        return False