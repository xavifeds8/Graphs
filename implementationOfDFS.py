"""
1--2-------3
|   |     /  \"
4--5     6    7

"""
class Graph:
    def __init__(self , size) -> None:
        self.size = size
        self.adjList = [[] for i in range(size)]
    def addEdges(self , U , V , Cost=0):
        self.adjList[U].append(V)
        self.adjList[V].append(U)

    def DFS(self , src , visited):
        visited.add(src)
        print(src , end="->")
        for i in self.adjList[src]:
            if i not in visited:
                self.DFS(i , visited)

    def dfsHelper(self):
        visited = set()
        for i in range(1,self.size):  #DISCONNECTED GRAPHS
            self.DFS(i , visited)

    def Print(self):
        # for i in range(1,self.size):
        #     print(i ,"-->", self.adjList[i])
        print(self.adjList)


g = Graph(9)
g.addEdges(1 , 2)
g.addEdges(1 , 4)
g.addEdges(4 , 5)
g.addEdges(5 , 2)
g.addEdges(2 , 3)
g.addEdges(3 , 6)
g.addEdges(3 , 7)
g.addEdges(6,7)
g.dfsHelper()
g.Print()

