class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                return num
            else:
                freq[num] = 1


        # visited = set()
        # for num in nums:
        #     if num in visited:
        #         return num
        #     else:
        #         visited.add(num)


        '''
        The naive solution without the constaint is to use a set and check if it is in set or not since set keeps everything uniqe
        Or iterate through the array and create a freq dict the one num with a freq > 1 is a duplicate 

        With the contrisant of not modifying the array nums 
        '''