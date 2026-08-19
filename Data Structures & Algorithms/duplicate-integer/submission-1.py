class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        haveSeen = []

        # To make things even simpler and so you don't need to check
        # if the number is in haveSeen, you can make haveSeen a set()
        # and just call it something like "hashset" (NeetCode's suggestion)
        # or listOfNonDuplicates.
        for number in nums:
            if number not in haveSeen:
                haveSeen.append(number)
            else:
                return True
        
        return False