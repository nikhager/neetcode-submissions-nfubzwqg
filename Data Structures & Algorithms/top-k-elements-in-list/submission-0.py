class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        return list(dict(sorted(count.items(), key=lambda item: item[1], reverse=True)))[:k]