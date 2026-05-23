# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_string = ""
        second_string = ""

        while l1 != None and l2 != None:
            first_string = str(l1.val) + first_string
            l1 = l1.next
            second_string = str(l2.val) + second_string
            l2 = l2.next
        
        while l2 != None:
            second_string = str(l2.val) + second_string
            l2 = l2.next

        while l1 != None:
            first_string = str(l1.val) + first_string
            l1 = l1.next
        
        num = int(first_string) + int(second_string)
        print(num)
        new_head = ListNode(num%10)
        tail = new_head
        num //=10
        while num > 0:
            new_node = ListNode(num%10)
            tail.next = new_node
            tail = new_node
            num//=10
        
        return new_head

        