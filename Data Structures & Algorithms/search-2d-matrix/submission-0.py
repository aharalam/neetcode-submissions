class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix[0]) * len(matrix) - 1

        while p1 <= p2:
            mid = (p1 + p2) // 2

            arr = matrix[mid // len(matrix[0])]
            midVal = arr[mid%len(matrix[0])]

            if midVal == target:
                return True
            elif midVal < target: # we know at this point that it will be for sure to the left of target if true
                p1 = mid + 1
            elif midVal > target: # we know at this point that it will be for sure to the right of target if true
                p2 = mid - 1
        
        return False

