class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def recur(start_index, end_index):
            # Base Case 1: The room is empty (Target not found)
            if start_index > end_index:
                return -1
            
            mid = (start_index + end_index) // 2

            # Base Case 2: Found it!
            if nums[mid] == target:
                return mid
            
            # Recursive Steps: Slam the door on the half we don't need
            if nums[mid] > target:
                # Target is smaller, so move the 'end' to the left of mid
                return recur(start_index, mid - 1)
            else:
                # Target is larger, so move the 'start' to the right of mid
                return recur(mid + 1, end_index)

        return recur(0, len(nums) - 1)