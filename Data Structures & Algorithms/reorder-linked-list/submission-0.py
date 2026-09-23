# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first step is find mid point
        #we will us two pointers slow and fast to find mid point
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the list into two seprate lists
        secondHalf = slow.next
        # First half will end with null
        slow.next = None
        
        #then once we divde them we reverse the second half
        #we can use three pointers prev, curr / secondHalf and nextNode to reverse the second half
        prev, curr = None, secondHalf

        while curr:
            nextNode = curr.next
            #now i will point curr to prev
            curr.next = prev
            #move the prev to curr
            prev = curr
            #move curr to the next 
            curr = nextNode 
        
        #since the second half if either equal or smaller than the first we can easily do an inplace merge
        first, second = head , prev

        while second: 
            #we need to grab all 4 pointers 
            tmp1, tmp2 = first.next, second.next
            #first we want first / head to point to second's head
            first.next = second
            #then we want second to point to the first next which is tmp1
            second.next = tmp1
            #now we move the first and second 
            first = tmp1
            second = tmp2





        '''
        Most naive soltion is take the values of the node put into an array then reorder using two pointers
        and then create a new linked list which create extra space and time 

        1-> 2 -> 3 -> 4 ->5
        we want 1 -> 5 -> 2 -> 4 -> 3
        this techincally means bsaically cut the linked list into two halves a then reverse the right side 

        first half 1 -> 2 or even add 3 if you want since it is odd length 
        then right side is 3 - > 4 -> 5

        now when reversed it is 5 -> 4 -> 3 now we can walk the two linked list and have two pointer p1 and p2 and 
        basically sew it back togther 

        How do we get a midpoint? we can use a fast and slow pointer to get the midpoint. the node the slow ends up on
        is always the midpoint

        1 - > 2 and  5 -> 4 -> 3 

        '''