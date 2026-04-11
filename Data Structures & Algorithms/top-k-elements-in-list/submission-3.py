class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I will first set up the dict
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        print(count)
        # By the end we should have sth like
        # count = {1:1, 2:2, 3:3}

        #Then we convert this pairs into list, and sort to get largest count 
        #at the end
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print(arr)
        #End we should have [[1,1],[2,2],[3,3]]

        #Then now i want to grab last elem and grab the num to return the answer
        # while len(res) < k
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        print(result)
        return result



        '''
        U - We get a list of int as an input and we have to return the k 
            most frequent elements within the array (The one with the 
            most duplicates) then return the most freq num < k. 

            Output is list of nums

            Edge case: k !> num in nums

        M - Maybe keep track of freq count then return a list 

        P -  
            We need to keep track of count in a freq map 
            add the pairs in a list so that we can sort the one with the most 
            count and pop to grab the "num" until the length of the arr < k

        '''
