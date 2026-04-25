from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # An anagram is a string that contains the exact same characters as another string,
        # but the order of the characters can be different

        anagrams = []

        for i, string1 in enumerate(strs):
            group = [] # ["cat", "act"]

            for j, string2 in enumerate(strs):
                if sorted(string1) == sorted(string2):
                    group.append(string2)

            anagrams.append(group)
        
        # Delete duplicate groups in anagrams
        unique_anagrams = []
        for group in anagrams:
            sorted_group = sorted(group)
            if sorted_group not in [sorted(g) for g in unique_anagrams]:
                unique_anagrams.append(group)
        
        return unique_anagrams