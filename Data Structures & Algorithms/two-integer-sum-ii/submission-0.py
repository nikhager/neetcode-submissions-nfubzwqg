class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Given an array of integers that is sorted in increasing order.
        # Return the indices (1-indexed) of two numbers, [index1, index2], 
        # such that they add up to a given target number target and index1 < index2. 
        # Note that index1 and index2 cannot be equal, 
        # therefore you may not use the same element twice.
        # There will always be exactly one valid solution.
        match = 0
        seen = defaultdict(int)
        for i, n in enumerate(numbers):
            match = target - n
            if match in seen:
                return [seen[match]+1, i+1]
            seen[n] = i