# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        store_in = []
        output = False
        while True:
            if tail != None:
                if tail in store_in:
                    output = True
                    break
                store_in.append(tail)
                tail = tail.next
            else:
                output = False
                break
        
        return output
