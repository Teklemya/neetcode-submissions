class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if num in seen:
                return True
            seen[num] = num
        return False        
        '''
        Understand: Input is an integer array and if any of the values in the array appears more than once we return true else false
                    Edge case: could the list be empty? yes but if empty return false
        Macthing: I would use a dict (hashmap) to check against 
        Plan:
        nums = [2,52,21,92,13,333,3,8,38,73,93,23,33] 
            seen = dict[]
            for num in nums:
                if num in seen: O(1) 
                    return True
                seen[num] = num
            return False

        Review: Dry run through your code
        Evaluate: Time complexity: O(n) - len of array
                  Space Complexity: O(n) 
        '''