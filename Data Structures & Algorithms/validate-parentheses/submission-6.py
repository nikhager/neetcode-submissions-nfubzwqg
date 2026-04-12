class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        obrac = ['(','{','[']
        cbrac = [')','}',']']
        pair = dict(zip(cbrac,obrac))
        stack = []

        for c in s:
            if c in pair:
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0