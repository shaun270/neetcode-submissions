import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_arr = []
        for i in points:
            element = (math.sqrt(i[0] ** 2 + i[1] ** 2))
            l = 0
            r = len(min_arr) - 1
            while l <= r:
                mid = (l + r) // 2
                mid_val = math.sqrt(min_arr[mid][0] ** 2 + min_arr[mid][1] ** 2)
                if mid_val > element:
                    r = mid - 1
                else:
                    l = mid + 1
            min_arr.insert(l, i)
            
        return min_arr[:k]