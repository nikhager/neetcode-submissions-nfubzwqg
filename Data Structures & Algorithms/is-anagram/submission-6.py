class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Given two strings s and t, 
        # return true if the two strings are anagrams of each other,
        size = len(s)
        if size != len(t):
            return False

        seen = defaultdict(int)
        
        for i in range(size):
            seen[s[i]] += 1
            seen[t[i]] -= 1
        for val in seen.values():
            if val != 0:
                return False
        return True