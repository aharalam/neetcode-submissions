class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        buckets = []
        max_possible_frequency = len(nums)

        for i in range(max_possible_frequency + 1):
            buckets.append([])

        for num, freq in frequencies.items():
            buckets[freq].append(num)
        
        result = []

        current_index = len(buckets) - 1

        while current_index > 0:
            bucket = buckets[current_index]

            for num in bucket:
                result.append(num)
            
            if len(result) == k:
                return result
        
            current_index -= 1
        
        return result