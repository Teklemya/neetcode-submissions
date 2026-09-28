class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = float('inf')
        for num in nums:
            lowest = min(lowest, num)
        return lowest

        
        '''
        Given an array length n which is orginal sorted but at somepoint rotated between 1 and n times. 
        [1,2,3,4,5] = eg:1 [3,4,5,1,2] eg:2 [5,6,1,2,3,4] find the min

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