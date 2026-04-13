# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


        '''
        Given a singly linked list i am given the head and asked to reverse it'

        i will treverse through and have three pointers prev, curr and next and that way
        as i tervese i will make curr point to prev and then move prev to curr and curr to next and 
        keep going until there is no curr


        '''
        