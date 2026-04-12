class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_s, letters_t = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            letters_s[s[i]] += 1
            letters_t[t[i]] += 1

        return letters_s == letters_t