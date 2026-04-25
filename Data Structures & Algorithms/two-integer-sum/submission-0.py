class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index1, number1 in enumerate(nums):
            for index2, number2 in enumerate(nums):
                if index1 != index2 and number1 + number2 == target:
                    return [index1, index2]
                    break
    
        return sum