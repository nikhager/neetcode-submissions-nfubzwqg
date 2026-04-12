class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        L = ("(","[","{")
        R = (")","]","}")

        if len(s) % 2 == 1:
            return False

        if s[0] in R:
            return False

        for c in s:
            if c in L:
                opened.append(c)
            
            if c in R:
                if len(opened) == 0 or L[R.index(c)] != opened[-1]:
                    return False
                opened.pop()
            
        if len(opened) > 0:
            return False

        return True

            