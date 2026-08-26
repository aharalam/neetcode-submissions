class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        
        # For each position except the last one
        for i in range(len(arr) - 1):
            # Find the max element to the right of index i
            right_elements = arr[i+1:]  # Get everything after index i
            max_number = max(right_elements)  # Find the maximum
            
            # Add this max to our new array
            new_arr.append(max_number)
        
        # The last element should be -1
        new_arr.append(-1)
        
        return new_arr