"""
1--2-------3
|   |     /  \"
4--5     6 -- 7

LEVEL ORDER TRAVERSAL

"""
class Graph:
    def __init__(self , size) -> None:
        self.size = size
        self.adjList = [[] for i in range(size)]
        pass
    def addEdges(self , U , V):
        self.adjList[U].append(V)
        self.adjList[V].append(U)
    def Print(self):
        print()
        for i in range(1,self.size):
            print(i , "->" , self.adjList[i])
    def BfS(self):
        visited = set()
        queue = list()
        queue.append(1)
        visited.add(1)
        while len(queue):
            src = queue.pop(0)
            print(src,end="->")
            for i in self.adjList[src]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

    def __del__(self):
        print("destructor is called")


g = Graph(8)
g.addEdges(1 , 2)
g.addEdges(1 , 4)
g.addEdges(4 , 5)
g.addEdges(5 , 2)
g.addEdges(2 , 3)
g.addEdges(3 , 6)
g.addEdges(3 , 7)
g.addEdges(6,7)
g.BfS()
g.Print()