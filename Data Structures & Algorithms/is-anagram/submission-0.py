from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # An anagram is a string that contains the exact same characters as another string,
        # but the order of the characters can be different.

        charactersInS = []
        charactersInT = []

        for character in s:
            charactersInS.append(character)
        
        for character in t:
            charactersInT.append(character)
        
        charactersInS.sort()
        charactersInT.sort()

        return Counter(charactersInS) == Counter(charactersInT)
            


        