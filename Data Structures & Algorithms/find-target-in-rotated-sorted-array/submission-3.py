class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1
        #incase we get nums = [1]
        while left <= right:
            mid = (left + right) // 2
            # let us check if mid is target 
            if target == nums[mid]:
                return mid
            #left sorted portion
            if nums[left] <= nums[mid]:
                #if the target value is greater than middle or if target is less than the smallest value in the left we check right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                #the target is less than middle but greater than left that means we will search the left
                else:
                    right = mid - 1
            #right sorted
            else:
                #if target is less than middle but greater than the most right we need to go left to find the pivot
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                #tragrte is greater than mid but less than right
                else:
                    left = mid + 1
        return -1


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