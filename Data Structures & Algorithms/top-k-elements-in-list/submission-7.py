from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequencyList = list(counter.items())  # [(num, freq), ...] ✅

        top_k_numbers = []
        top_k_freqs = []

        for number, frequency in frequencyList:  # safe to unpack now
            if len(top_k_numbers) < k:
                top_k_numbers.append(number)
                top_k_freqs.append(frequency)
            else:
                # Find the smallest frequency
                min_index = 0
                for i in range(1, k):
                    if top_k_freqs[i] < top_k_freqs[min_index]:
                        min_index = i

                if frequency > top_k_freqs[min_index]:
                    top_k_numbers[min_index] = number
                    top_k_freqs[min_index] = frequency

        return top_k_numbers

