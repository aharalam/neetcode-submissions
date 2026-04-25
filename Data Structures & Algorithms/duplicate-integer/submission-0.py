from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_of_each_object_in_nums = Counter(nums)
        print(f"All counts: {number_of_each_object_in_nums}")

        duplicates = []

        for item, count in number_of_each_object_in_nums.items():
            if count > 1:
                duplicates.append(item)
        
        print(len(duplicates))

        if len(duplicates) > 0:
            return True
        else:
            return False
