from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph  = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,v):
        visited = []
        queue = []
        queue.append(v)
        visited.append(v)
        while queue:
            s = queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(2,5)
g.addEdge(3,4)
g.addEdge(5,0)
g.BFS(2)
