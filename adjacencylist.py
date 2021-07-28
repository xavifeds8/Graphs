from collections import defaultdict


class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.next = None
class Graphs:
    def __init__(self) -> None:
        pass
    adjList = defaultdict(list)
    def addEdge(self , U , V , Cost , isDir = False):
        self.adjList[U].append([V,Cost])
    def Print(self):
        for i in self.adjList:
            print(i,end=" ::= ")
            for j in self.adjList[i]:
                print(j , end=" -> ")
            print()
G = Graphs()
G.addEdge("ankola" , "karwar" , 45)
G.addEdge("mysruru" , "hubli" , 45)
G.addEdge("hubli" , "mysuru" , 45)
G.addEdge("karwar" , "mysuru" , 45)
G.addEdge("hulbi" , "mangaluru" , 45)
G.addEdge("hubli" , "karwar" , 45)
G.addEdge("chitturu" , "karwar" , 45)
G.addEdge("ankola" , "karkal" , 45)
G.addEdge("ankola" , "gadag" , 45)
G.Print()

