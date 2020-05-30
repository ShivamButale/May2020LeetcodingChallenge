#We can return False if current node has alreay been visited or any of its adjacent nodes are currently being visited or have been visited    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictionary = defaultdict(list)
        for i, j in prerequisites:
            dictionary[i].append(j)
            
        curr = [False]*numCourses
        visited = [False]*numCourses  
        
        def func(i):
            curr[i] = True
            val = visited[i] or all(not curr[j] and func(j) for j in dictionary[i])
            curr[i] = False
            visited[i] = True
            return val
        
        return all(func(n) for n in range(numCourses))
