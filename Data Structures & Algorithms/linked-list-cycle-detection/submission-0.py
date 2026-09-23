# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

        '''
        we can solve this by using a hash set to check for duplicates / visted and if there is any as we treverse 
        then we know there is a cycle 

        we can use two pointers fast and slow where fast goes double the steps slow does; so if there is a cycle
        since the fast goes double it will ctach up to the slow eventually

        If there is no cycle then fast will end up becoming null

        So given 1 -> 2 -> 3 -> 4 and there is a cycle at index 1 
                      s
                                    f

                1 -> 2
                        f
                s

        '''