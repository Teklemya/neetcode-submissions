import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)   
        while left <= right:
            currentSpeed = (left + right) // 2  
            totalHour = 0
            for pile in piles:
                totalHour += math.ceil(pile / currentSpeed)
            if totalHour <= h:
                res = min(res, currentSpeed)
                right = currentSpeed - 1
            else:
                left = currentSpeed + 1
        return res


        '''
        Give piles which is a pile of bananas i and h is amount of hours allowed
        decide the mimumum speed you need to eat at to finish all bananas on time
        banana eating speed = pile / hour
        hour = pile / speed 

        h >= len(piles) always becuase i can only eat a one pile an hr
        my top speed can be set to the max pile becuase if i findh that an hour i can finish the rest

        so lets say k = max(pile) now inorder to find the mimumim k i need to check from 1 -> k
        and return the minmum number that will satisify the case 


        M - Brute force is check all k from 1 - k for speed in range(1, k): ..
            or i can use a binary search apporach to cut k in half everytime to get to the right solution

        P - set left -> 1 and right to the max(pile)
            res could be float(inf) but in this case the highest it can be is max(piles)
            then do a binary search on k 
            while left <= right:
                k = left + right // 2
                then check for each pile the total hour it would take to eat for that k
                totalhour = 0
                for pile in piles:
                    totalhour += math.celi(pile / k)
                # now i have total hour it took me to eat at that speed i can check if i am i the time limit
                if totalHour <= h:
                    # i have found one work i will update my result but that might not be the lowest
                    res = min(res, k)
                    #since i updated my res by mid i don't need to recheck it but i need to check the lower
                    right = mid - 1
                else:
                    it is on the upper range so
                    left = mid + 1
            finally return the result
            return res

        '''