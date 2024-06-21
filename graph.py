#Graph DFS
def dfs(input_dict,visit,stack,ele):
    if visit[ele]=="False":
        stack.append(ele)
        visit[ele]="True"
    else:
        return
    for i in input_dict[ele]:
        dfs(input_dict,visit,stack,i[1])
    print(stack.pop(),end=" ")

#Graph BFS
def bfs(input_dict,ele):
    q=[ele]
    v={}
    for i in input_dict.keys():
        v[i]=False
    v[ele]=True
    while len(q)!=0:
        curr=q.pop(0)
        print(curr,end=" ")
        for i in input_dict[curr]:
            if v[i[1]]==False:
                q.append(i[1])
                v[i[1]]=True
                #print(v,q)
if __name__=="__main__":
    input_dict={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,6,0),(3,5,0)],4:[(4,7,0),(4,8,0)],
            5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:[(7,2,0),(7,5,0),(7,4,0)],8:[(8,4,0),(8,6,0)]}
    visit={1:"False",2:"False",3:"False",4:"False",5:"False",6:"False",7:"False",8:"False"}
    stack=[]
    print("DFS of Graph")
    for i in input_dict:
        dfs(input_dict,visit,stack,i)
    print("\nBFS of Graph")
    bfs(input_dict,1)


