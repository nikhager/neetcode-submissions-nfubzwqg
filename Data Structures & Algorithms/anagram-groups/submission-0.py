class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for s in strs:
            # count chars in string
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            # group if chars ==
            anagrams[tuple(count)].append(s)

        return anagrams.values()