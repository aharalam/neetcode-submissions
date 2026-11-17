class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums)-1

        while p1 <= p2:
            mid = (p1+p2)//2

            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: # we know the target is on the right side of the current number
                p1 = mid + 1
            elif nums[mid] > target: # we know the target is on the left side of the current number
                p2 = mid - 1
        
        return -1