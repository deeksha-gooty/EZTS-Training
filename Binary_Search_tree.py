class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)

# def binary_search_tree(root,ele):
#     curr=Node(ele)
#     if curr.data<root.data:
#         if root.left==None:
#             root.left=curr
#         else:
#             binary_search_tree(root.left,ele)
#     elif curr.data>root.data:
#         if root.right==None:
#             root.right=curr
#         else:
#             binary_search_tree(root.right,ele)
#     else:
#         return

def binary_search_tree(root,ele):
    if root==None:
        return Node(ele)
    if ele<root.data:
        root.left=binary_search_tree(root.left,ele)
    if ele>root.data:
        root.right=binary_search_tree(root.right,ele)
    return root
    
def preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def levelorder(root):
    q=queue()
    q.push(root)
    q.push(None)
    while q.size()>0:
        c=q.pop()
        if c==None:
            if q.size()==0:
                break
            else:
                print()
                q.push(None)
        else:
            print(c.data,end=" ")
            if c.left!=None:
                q.push(c.left)
            if c.right!=None:
                q.push(c.right)

def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return (max(lh,rh)+1)

def print_leaf_nodes(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.data,end=" ")
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

if __name__=="__main__":
    lst=[4,6,7,3,8,2,5,9,1]
    root=Node(lst[0])
    lst.pop(0)
    for i in lst:
        binary_search_tree(root,i)
    print("Preorder")
    preorder(root)
    print("\nInorder")
    inorder(root)
    print("\nPostorder")
    postorder(root)
    print("\nLevel Order")
    levelorder(root)
    print("\nHeight")
    print(height(root))
    print("Leaf Nodes")
    print_leaf_nodes(root)