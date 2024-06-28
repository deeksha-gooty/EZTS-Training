'''
Graphs are made up of set of edges and vertices. 
There is no relation between the edges and the vertices.
Graph G={Edges(E),Vertices(V)}
Edges and Vertices: Weighted
                    Directed
Total there are 4 Types of graphs that are made from the combinations of the above mentioned 
two types of the edges and vertices.
Three important metrices of a graph are: 1. S-Source
                                         2. D-Destination
                                         3. W-Weight
Graphs can be stored by using: 1.List of ArList (Java)
                               2.List of List (Python)
                                        -> [[(src,des,weight),..],...,[(src,des,weight),...]]
                               3.Dictionary of list of tuples (Python)
                                        -> {key:[(src,des,weight),....(src,des,weight)]}
                                            Here src is the key and des is the vertices that 
                                            can be reached from src.
Spanning Tree: It is a subgraph of a graph where in all the vertices of the graph 
are visited with minimum cost.

Graph Algorithms:
1.Prims Algorithm : Finding the minimum connected edge from the given graph,and then find the 
  connected edge that is minimum of the selected subgraph edges,and visit all the other edges 
  is known as prims algorithm.

'''
# def min_weight(graph,visit):
#     min=float('inf')
#     sc=ds=0
#     for i,j in graph.items():
#         l=sorted(j,key=lambda x:x[2],reverse=False)
#         sl=l[0][2]
#         if sl<min:
#              min=sl
#              sc=l[0][0]
#              ds=l[0][1]
#     visit[sc]=True
#     visit[ds]=True
#     print(visit)
#     print(min)
#     return min
# if __name__=="__main__":
#     graph={1:[(1,2,7),(1,3,4),(1,5,8)],
#            2:[(2,1,7),(2,5,2)],
#            3:[(3,1,4),(3,4,5)],
#            4:[(4,3,5),(4,5,1)],
#            5:[(5,1,8),(5,2,2),(5,4,1)],
#            6:[(6,5,9)]}
#     visit={1:False,2:False,3:False,4:False,5:False,6:False}
#     mi=min_weight(graph,visit)


# #Prims Algorithm:

graph=[[0,7,4,-1,8,-1],
        [7,0,-1,-1,2,-1],
        [4,-1,0,5,-1,-1],
        [-1,-1,5,0,1,-1],
        [8,2,-1,1,0,9],
        [-1,-1,-1,-1,9,0]]    
visited=[False]*len(graph)
m=float('inf')
sc=ds=-1
n=len(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j]>0 and graph[i][j]<m:
            m=graph[i][j]
            sc=i
            ds=j
visited[sc]=visited[ds]=True
spanning_tree=[(sc+1,ds+1,m)]
while False in visited:
    m=float('inf')
    for i in range(len(visited)):
        if visited[i]==True:
            for j in range(n):
                if graph[i][j]>0 and graph[i][j]<m and visited[j]==False:
                    m=graph[i][j]
                    sc=i
                    ds=j
    visited[ds]=True
    spanning_tree.append((sc+1,ds+1,m))
print(spanning_tree)
print(visited)


#Kurscals' Algorithm

# graph=[[0,7,4,-1,8,-1],
#         [7,0,-1,-1,2,-1],
#         [4,-1,0,5,-1,-1],
#         [-1,-1,5,0,1,-1],
#         [8,2,-1,1,0,9],
#         [-1,-1,-1,-1,9,0]] 
graph = [
    [0, 1, 7, 10, 5],   # P
    [1, 0, 3, -1, -1],  # Q
    [7, 3, 0, 4, -1],   # R
    [10, -1, 4, 0, 2],  # S
    [5, -1, -1, 2, 0]   # T
]   
visited=[False]*len(graph)
m=float('inf')
sc=ds=-1
n=len(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j]>0 and graph[i][j]<m:
            m=graph[i][j]
            sc=i
            ds=j
visited[sc]=visited[ds]=True
spanning_tree=[(sc+1,ds+1,m)]
while False in visited:
    m=float('inf')
    for i in range(len(visited)):
        for j in range(n):
            if graph[i][j]>0 and graph[i][j]<m and visited[j]==False:
                m=graph[i][j]
                sc=i
                ds=j
    visited[ds]=True
    spanning_tree.append((sc+1,ds+1,m))
print(spanning_tree)
print(visited)



#Dijacktras Algorithm

