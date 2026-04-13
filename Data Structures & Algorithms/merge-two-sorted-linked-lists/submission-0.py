# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode()
        curr = sortedList
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        if p1:
            curr.next = p1
        else:
            curr.next = p2
        
        return sortedList.next


        '''
        Given the head of two linked list list1 and list2 i am asked to a new list that is sorted
        I will be using two pointer p1 and p2 to point to each heads and compare them while p1 and p2
        exisits at the same time if p1.val <= p2 then sortedList.next = p1 then move p1 = p1.next
        else other wise let us say one of them got exhuasted fullly 
        if p1: we will add p1 fully else vise versa and then return the sortedList.next
        '''