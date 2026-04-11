class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #{3:0}

        for i in range(len(nums)):
            num = nums[i] # index 0 num is 3, index 1 num is 4
            diff = target - num # 7 - 3 = 4, 7 - 4 = 3
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[num] = i






        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     currSum = nums[left] + nums[right]
        #     if currSum == target:
        #         return [left, right]
        #     elif currSum > target:
        #         right -= 1
        #     elif currSum < target:
        #         left += 1



        ''' 
        U understand - Input is an int array, and we want to look for two numbers 
                        that adds up to a target
                        Output is the indeices of the numbers
        M macth - Two pointers
        P - What we can do is start the left pointer at index 0 and right 
            pointer at last index
            If the sum == target we return the index 
            Elif the sum > target we want to move the right to the left 
            Else the sum < target we want to move the left to right
        I
        R
        E
        '''