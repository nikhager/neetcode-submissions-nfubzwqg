class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = []
        for c in s:
            if c in seen:
                seen = seen[(seen.index(c) + 1):]
            seen.append(c)
            longest = max(len(seen), longest)
        return longest