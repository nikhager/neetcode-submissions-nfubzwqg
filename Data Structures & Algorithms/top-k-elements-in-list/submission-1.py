class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given an integer array nums and an integer k, 
        # return the k most frequent elements within the array.
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
        
        return sorted(seen, key=seen.get, reverse=True)[:k]

        # The test cases are generated such that the answer is always unique.
        # You may return the output in any order.