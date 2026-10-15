class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        current_number = 1

        for num in nums:
            print(num)
            if num < current_number:
                continue

            if num == current_number:
                # return the first positive number that's not in the array:
                current_number += 1
            
            if num > current_number:
                # return the first positive number that's not in the array:
                return current_number
        
        

        return current_number