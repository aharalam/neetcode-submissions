from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        unique_elements = list(frequencies.keys())

        unique_elements.sort(reverse=True, key=frequencies.get)

        return unique_elements[:k]

