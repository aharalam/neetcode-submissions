class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix) * len(matrix[0]) - 1

        while p1 <= p2:
            mid = (p2 + p1) // 2 # index
            arr = matrix[mid // len(matrix[0])] # the array we're currently looking at
            midVal = arr[mid % len(arr)] # value of mid


            if midVal == target:
                return True
            elif midVal < target: # we know for sure that the target is to the right of mid
                p1 = mid + 1
            elif midVal > target: # we know for sure that the target is to the left of mid
                p2 = mid - 1
        
        return False

