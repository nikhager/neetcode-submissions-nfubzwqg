class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []

        for i, n in enumerate(nums):
            target = -n
            seen = {}
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in seen and [n, diff, nums[j]] not in solution:
                        solution.append([n, diff, nums[j]])
                seen[nums[j]] = j

        return solution