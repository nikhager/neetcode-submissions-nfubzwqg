class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Given a string s, return true if it is a palindrome, otherwise return false.

        # A palindrome is a string that reads the same forward and backward. 
        # It is also case-insensitive and ignores all non-alphanumeric characters.

        s_clean = ''.join(filter(str.isalnum, s)).lower()
        
        for i in range(len(s_clean)//2):
            if s_clean[i] != s_clean[-(i+1)]:
                return False
        
        return True