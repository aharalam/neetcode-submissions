class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []  # Store results
        
        # For each position, find the max to its right
        for i in range(len(arr)):
            current_greatest_element = -1  # Default for last element
            
            # Look at all elements to the RIGHT of position i
            for j in range(i + 1, len(arr)):
                if arr[j] > current_greatest_element:
                    current_greatest_element = arr[j]
            
            ans.append(current_greatest_element)
        
        return ans