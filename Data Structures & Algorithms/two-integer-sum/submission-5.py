class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print("nums:", nums)
        #print("TARGET:", target)
        for i in range(len(nums)):
            #print("i:", i, "nums[i]:", nums[i])
            for j in range(i+1, len(nums)):
                #print("j:", j, "nums[j]:", nums[j])
                #print("nums[i] + nums[j] =", nums[i] + nums[j])
                if nums[i] + nums[j] == target:
                    #print("FOUND:", "i:", i, "j:", j, "nums[i] + nums[j] =", nums[i] + nums[j])
                    #print(j)
                    #print(nums[j])
                    return [i, j]
        
        return [i, j]
