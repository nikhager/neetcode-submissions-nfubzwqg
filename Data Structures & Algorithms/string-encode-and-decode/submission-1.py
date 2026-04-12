class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += (str(len(s)) + "#" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        left = right = 0
        while right < len(s):
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            strs.append(s[ (right + 1) : (right + 1 + length) ])
            left = right = right + 1 + length
                
        return strs