# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        
        dummy = ListNode()
        curr = dummy

        p1, p2 = l1, l2
        carry = 0
        digit = 0

        while p1 or p2 or carry:
            #because there could be a case one of the linkedlist might be pointing at a null
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10
            #since if carry exists or not we will always end up adding digits becuase if total is 8 digit will be 8 since 8 % 10 = 8
            curr.next = ListNode(digit)
            curr = curr.next
            #move the two pointers but what if there is no p1 or p2 since while loop only checks one
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        #finally return next node of dummy
        return dummy.next






        '''

        Givn two linked list i am asked to add them and return a new linkedlist which will be the sum
        now wehn i add if val1 + val2 then i will calclauate a carry which is total % 10 taht will be added to the next total sum and i will grab the 
        frist digit "digit" by doing total // 10 then i will add digit as a node to curr.next and move curr and finally mvoe both p1 n p2
        To keep track of the two linkedlist i will use p1 and p2 to keep track
        cases that i need to consider if p1 exists and p2 doesn't i will just assign the value to a 0 for the sake of addition


        '''