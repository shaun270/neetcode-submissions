class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashMap = {i: [] for i in range(n)}

        for node_a, node_b in edges:
            hashMap[node_a].append(node_b)
            hashMap[node_b].append(node_a)        
        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            if hashMap[node] == []:
                return True
            
            
            for connect in hashMap[node]:
                if connect == par:
                    continue
                if not dfs(connect, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n






             