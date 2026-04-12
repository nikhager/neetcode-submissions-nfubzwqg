class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Given an array of strings strs, 
        # group all anagrams together into sublists. 
        # You may return the output in any order.
        anagrams = defaultdict(list)        # dictionary of lists
        for s in strs:
            s_sorted = ''.join(sorted(s))   # sort string (join chars)
            anagrams[s_sorted].append(s)    # append to sorted list (anagrams)
        return list(anagrams.values())      # return list of values(lists)