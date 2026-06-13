class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        hashMap = {i:[] for i in range(n)}
        for i, j in edges:
            hashMap[i].append(j)
            hashMap[j].append(i)
        out = 0
        glob_visit = set()
        def dfs(node, par, visit):
            if node in visit:
                return True

            visit.add(node)
            glob_visit.add(node)
            for nei in hashMap[node]:
                if nei == par:
                    continue
                
                if not dfs(nei, node, visit):
                    return True

            return True

        for i in hashMap:
            visit = set()
            if i not in glob_visit:
                dfs(i, -1, visit)
                out += 1

        return out
