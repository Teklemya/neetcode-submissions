class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow, slow2 = 0, 0, 0

        while True:
            slow = nums[slow] # slow = 1 : slow = 3 : slow = 3 : slow = 4
            fast = nums[nums[fast]] # fast = nums[1] = 3 : fast = nums[2] = 4 = nums[4] = 4 : fast = 4
            if slow == fast:
                break

        #check if they are equal, that doesn't nessacry mean that is the duplicate however we know there is a cycle
        while True:
            #now we walk our second pointer and move both slows one step , the index where they meet is the entry for the cycle
            slow = nums[slow] #slow = nums[4] = 2 : slow = 4 : slow = 2
            slow2 = nums[slow2] #slow2 = nums[0] = 1 : slow2 = 3 : slow2 = 2

            if slow == slow2:
                return slow2




        # freq = {}

        # for num in nums:
        #     if num in freq:
        #         return num
        #     else:
        #         freq[num] = 1


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

        We can use Floyd's cycle detection becuase as an example let us take [1,2,2,3]
        the index of the array is less than n defined in the constriants
        Since one value is repated, two or more indeices point to that one value 
        so if we were to treat this like a cycle detection we can have a slow and fast pointer and see if the two end up meeting 
        '''