#Ford Algorithm
#Working on dynamic Programming 
graph=[
    [0, 6, 4, 5, False, False],
    [False, 0, False, False, -1, False],
    [False, -2, 0, False, 3, False],
    [False, False, -2, 0, False, -1],
    [False, False, False, False, 0, 3],
    [False, False, False, False,False, 0]
]
n=len(graph)
#Creation of edge list
e_l=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0 and  graph[i][j]!=False:
            e_l.append(tuple((i,j)))
print(e_l)
#Creating resultant dictionary
dist={}
for i in range(n):
    dist[i]=float('inf')
dist[0]=0
#Updating the result Dictonary
for i in range(n-1):
    for j in e_l:
        new_dist=dist[j[0]]+graph[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
print(dist)



# d={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"}
# res=[float('inf')]*n
# res[0]=0
# #Use the code for creation of the edge list
# #Creation of the result res 
# for i in range(len(e_l)):
#     for i in range(n-1):
#         for j in range(n):
#             if graph[i][j]==0 and  graph[i][j]==False:
#                 continue
#             elif graph[i][j]+res[i]<res[j]:
#                 res[j]=graph[i][j]+res[i]
# print(res)