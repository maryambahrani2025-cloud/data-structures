#Graphs
class Graph: 
    def __init__(self, n, directed=False, weighted=False): 
        self.n =n 
        self.directed = directed 
        self.weighted = weighted 
        self.M = [[0] * n for _ in range(n)] 

    def insert_edge(self, s, t, weight=1): 
        self.M[s][t] = weight 
        if not self.directed: 
            self.M[t][s] = weight 

    def delete_edge(self, s, t): 
        self.M[s][t] = 0 
        if not self.directed: 
            self.M[t][s] = 0 

    def count_edges(self): 
        total = sum(sum(1 for val in row if val != 0) for row in self.M) 
        return total if self.directed else total // 2 

    def show(self): 
        print("Adjacency Matrix:") 
        for row in self.M :
            print(" ".join(map(str, row))) 
#BFS
graph=Graph(6)
def BFS(start,graph):
    queue=[start]
    visited={start}
    while queue:
        vertex=queue.pop(0)
        for ne in range(graph.n):
            if graph.M[vertex][ne] != 0 and ne not in visited:
                visited.add(ne)
                queue.append(ne)
    return visited  
#DFS
def DFS(start, graph, visited=None):
    if visited is None:
        visited = [False] * graph.n
    visited[start] = True
    print(start, end=' ')  
    for ne in range(graph.n):
        if graph.M[start][ne] != 0 and not visited[ne]:
            DFS(ne, graph, visited)
    return visited