#Making use of queue data structur to print bfs and we use stack to print dfs.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class node_data:
    def __init__(self,Node,Hkey):
        self.node=Node
        self.hkey=Hkey

def top_views(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    key_dict={}

    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
            if curr.hkey not in key_dict.keys():
                key_dict[curr.hkey]=curr.node.data
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right!=None:
                temp=node_data(curr.node.right,curr.hkey+1)
                q.append(temp)
    for i in sorted(key_dict):
        print(key_dict[i],end=" ")

def bottom_views(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    key_dict={}

    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
            key_dict[curr.hkey]=curr.node.data
            if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right!=None:
                temp=node_data(curr.node.right,curr.hkey+1)
                q.append(temp)
    for i in sorted(key_dict):
        print(key_dict[i],end=" ")


def left_Side_views(root):
    q=[root]
    q.append(None)
    print(root.data,end=" ")
    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                print(q[0].data,end=" ")
                q.append(None)
        else:
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
    

def Right_Side_views(root):
    q=[root]
    q.append(None)
    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
            if q[0]==None:
                print(curr.data,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
  
if __name__=="__main__":
    root=Node(1)

    root.left=Node(2)
    root.right=Node(3)

    root.left.left=Node(4)
    root.left.right=Node(5)

    root.right.left=Node(6)
    root.right.right=Node(8)

    root.left.right.left=Node(9)
    root.left.right.right=Node(10)

    root.left.right.left.left=Node(12)
    root.left.right.left.right=Node(13)

    root.right.right.right=Node(11)

    print("TOP VIEW")
    top_views(root)
    print("\nBOTTOM VIEW")
    bottom_views(root)
    print("\nLEFT SIDE VIEW")
    left_Side_views(root)
    print("\nRIGHT SIDE VIEW")
    Right_Side_views(root)