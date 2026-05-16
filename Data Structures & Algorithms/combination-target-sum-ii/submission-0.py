class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates.sort()

        def recur(i, arr, total):
            if total == target:
                result.add(tuple(arr))
                return
            if i>=len(candidates) or total > target:
                return
            arr.append(candidates[i])
            recur(i+1, arr, total + candidates[i])
            arr.pop()
            recur(i+1, arr, total)
            

        recur(0, [], 0)

        return [list(combination) for combination in result]

