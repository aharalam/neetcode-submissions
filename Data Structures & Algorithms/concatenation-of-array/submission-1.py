class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for nums_index in range(len(nums)):
                ans.append(nums[nums_index])
        

        return ans