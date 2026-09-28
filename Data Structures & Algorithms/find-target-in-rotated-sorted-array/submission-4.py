class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            #if the left side is sorted, we add equal sign because we might get an array with one length
            if nums[left] <= nums[mid]:
                #check if the target is in the left side or right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            #if the right is sorted
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1



        '''
        Given an array length n which is orginal sorted but at somepoint rotated between 1 and n times. 
        [1,2,3,4,5] = eg:1 [3,4,5,1,2] eg:2 [5,6,1,2,3,4]

        this techincally is two strictly increasing two segemnets 3,4,5 and 1,2
        so techincally we can use binary search to check if the target we are looking for is in the left 
        half or the right half or mid? and if can't find it we return -1

        so let us have left right and mid
        if target is mid then just return that index ( mid )
        if target is greater than mid (it should be on the right side) but less than left then 
        we know it is not on the left side and it has been rotated to be in the right eg:2 (target = 4)
        but if it is greater than mid and greater than left then we should check left side eg:2 (target =6)

        the other case is if target is less than mid and greater than the most right eg:1 target = 3
        we check the left side
        if target is less than mid and less than left we check right eg:1 target = 1 

        if all this cases don't meet we just return -1
        '''



































        # left , right = 0, len(nums) - 1
        # #incase we get nums = [1]
        # while left <= right:
        #     mid = (left + right) // 2
        #     # let us check if mid is target 
        #     if target == nums[mid]:
        #         return mid
        #     #left sorted portion
        #     if nums[left] <= nums[mid]:
        #         #if the target value is greater than middle or if target is less than the smallest value in the left we check right
        #         if target > nums[mid] or target < nums[left]:
        #             left = mid + 1
        #         #the target is less than middle but greater than left that means we will search the left
        #         else:
        #             right = mid - 1
        #     #right sorted
        #     else:
        #         #if target is less than middle but greater than the most right we need to go left to find the pivot
        #         if target < nums[mid] or target > nums[right]:
        #             right = mid - 1
        #         #tragrte is greater than mid but less than right
        #         else:
        #             left = mid + 1
        # return -1


        '''
        Since all numbers are unique, we can use multiple apporaches so solve in O(N) Time and space 
        even better in O[N] time and constant space using two pointers or just a single pass / linear search

        given that this list is rotated after it is sorted we can see that there are two segements in there that are both ascending 
        but at an infliction point. so we can perfom binary search to find that point and also to find it within those two segemnts
        so for example 

        [3,4,5,6,1,2] we can't pick a mid point and ignore the other half becuase this is not strictly increasing
        but we can still use bianry search to find that infliction point

        [3,4,5,6,1,2] target is 1   [3,5,6,0,1,2] tagret = 4
               l m  r                   
 
        if nums[l] < nums[mid] which is normal we know infliction point is on right
            so we move left to mid and do a normal binary search  
        if nums[mid] < nums[r] which is normal we know infliction point is on left
            so we move right to mid and find a new mid and find infliction point 
        now target 
        '''