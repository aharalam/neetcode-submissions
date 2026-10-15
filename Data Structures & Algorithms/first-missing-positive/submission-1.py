class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        missing = 1

        for num in nums:
            print(num)
            if num < missing:
                continue

            if num == missing:
                # return the first positive number that's not in the array:
                missing += 1
            
            if num > missing:
                # return the first positive number that's not in the array:
                return missing
        
        

        return missing