from collections import defaultdict
class Graphs:
    def __init__(self) -> None:
        pass
    adj = defaultdict(dict)
    def addEdge(self, U , V , Cost , isBiDir = True):
        self.adj[U][V] = Cost
        if isBiDir:
            self.adj[V][U]  = Cost
    print(adj)
    def Prints(self):
        for i in self.adj:
            print(i,"->" , self.adj[i])
G = Graphs()
G.addEdge("ankola" , "karwar" , 45)
G.addEdge("mysruru" , "hubli" , 45)
G.addEdge("hubli" , "mysuru" , 45)
G.addEdge("karwar" , "mysuru" , 45)
G.addEdge("ankola" , "mangaluru" , 45)
G.addEdge("ankola" , "karwar" , 45)
G.addEdge("chitturu" , "karwar" , 45)
G.addEdge("ankola" , "karkal" , 45)
G.addEdge("ankola" , "gadag" , 45)
G.Prints()

            

