# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # --- STEP 1: Find the middle of the list ---
        # We use a slow pointer (moves 1 step) and fast pointer (moves 2 steps).
        # When fast reaches the end, slow will be at the middle.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # --- STEP 2: Reverse the second half ---
        # 'second' is the start of the right half.
        second = slow.next
        
        # Sever the tie between the left half and right half
        slow.next = None 
        prev = None
        
        # Standard linked list reversal
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # --- STEP 3: Merge the two halves ---
        # 'first' points to the start of the left half.
        # 'prev' points to the start of the reversed right half.
        first, second = head, prev
        
        while second:
            # Save the next nodes before we break the links
            tmp1, tmp2 = first.next, second.next
            
            # Insert the node from the second half after the node from the first half
            first.next = second
            second.next = tmp1
            
            # Move our pointers forward for the next iteration
            first = tmp1
            second = tmp2