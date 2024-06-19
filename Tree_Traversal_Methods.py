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
        print(root.data)
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

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
    print("\nPreorder")
    preorder(root)
    print("\nInorder")
    inorder(root)
    print("\nPostorder")
    postorder(root)
    print("\nLevel Order")
    levelorder(root)
    print("\nHeight")
    print(height(root))
    print("\nLeaf Nodes")
    print_leaf_nodes(root)
    