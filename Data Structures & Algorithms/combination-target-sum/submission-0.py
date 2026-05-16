class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def recur(i, arr, total):
            if total == target:
                result.append(arr.copy())
                return
            if total > target or i>=len(nums):
                return
            arr.append(nums[i])
            recur(i, arr, total + nums[i])
            arr.pop()
            recur(i+1, arr, total)

        recur(0, [], 0)
        return result