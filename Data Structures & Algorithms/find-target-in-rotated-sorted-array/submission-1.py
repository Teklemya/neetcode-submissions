class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        '''
        Since all numbers are unique, we can use multiple apporaches so solve in O(N) Time and space 
        even better in O[N] time and constant space using two pointers or just a single pass
        '''