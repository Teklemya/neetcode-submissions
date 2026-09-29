class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # lowest = float('inf')
        # for num in nums:
        #     lowest = min(lowest, num)
        # return lowest
        while left < right:
            mid = (left + right) // 2
            #infliction is to the right and the mid can not be minmum or anything to the left 
            if nums[mid] > nums[right]:
                left = mid + 1
            #inbfliction to the left and mid can be that mimumum 
            if nums[mid] <= nums[right]:
                right = mid
        return nums[left]

        
        '''
        Whenever you analyze a rotated array problem:

        Avoid cross-comparing all three points (left, mid, right) simultaneously.

        Anchor on one reference point (usually right). If nums[mid] > nums[right], 
        the break is to the right; otherwise, it's at mid or to the left.

        
        Given an array length n which is orginal sorted but at somepoint rotated between 1 and n times. 
        [1,2,3,4,5] = eg:1 [3,4,5,1,2] eg:2 [5,6,1,2,3,4] find the min eg:3 [3,2,1]
         l                  l       r        l         r
        this techincally is two strictly increasing two segemnets 3,4,5 and 1,2
        we need to have a run varibale lowest that keep tracks of the lowest and gets updated
        we can use binary search to search on which side that digits could be using left, mid and right pointer
        we know if nums[mid] > nums[right] the infliction is to the right so we should go right
        left = mid + 1
        if nums[mid] <= nums[right] we know infliction is to the left so we move 
        right = mid

        finally return nums[left]

        '''