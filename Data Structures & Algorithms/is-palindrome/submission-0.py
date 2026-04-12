class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = ''.join(filter(str.isalnum, s.lower()))
        size = len(s_filtered)

        for i in range(size//2):
            if s_filtered[i] != s_filtered[size-1-i]:
                return False
        return True