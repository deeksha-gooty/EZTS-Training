#Balence Factor = |lh-rh| ==(-1,0,1)
#Rotations : LL RR LR RL
#Balance Factor < -1 then LL and LR rotation takes place
#Balance Factor > 1 then RR and RL rotation takes place
#       RR                       RL                         LL                  LR
#           2                      2                -2                       -2
#       1                      1                         -1                      -1
#   0                              0                            0             0
#key<root.left.value:   key>root.left.value:      key>root.right.value:     key<root.right.value:
#   right_rotate            root.left=L_Rotate      Left_Rotate                 root.right=R_rotate         
#                           Right_rotate                                        Left_Rotate

class Node:     #Class for tree nodes
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

def insert(root,ele):
    if not root:
        return Node(ele)
    if ele<root.data:
        root.left=insert(root.left,ele)
    else:
        root.right=insert(root.right,ele)

    root.height=1+max(ght(root.left),ght(root.right))    
    BF=getBF(root)

    if BF>1 and ele<root.left.data:
        return rightRotate(root)        #RR Rotation
    
    if BF>1 and ele>root.left.data:
        root.left=leftRotate(root.left)
        return rightRotate(root)        #RL Rotation
    
    if BF<-1 and ele>root.right.data:
        return leftRotate(root)         #LL Rotation
    
    if BF<-1 and ele<root.right.data:
        root.right=rightRotate(root.right)
        return leftRotate(root)         #LR Rotation
    
    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftRotate(A):
    B=A.right
    temp=B.left     #Creating the copy of values

    B.left=A
    A.right=temp    #Rotating the nodes

    A.height=1+max(ght(A.left),ght(A.right)) 
    B.height=1+max(ght(B.left),ght(B.right))   #Updating the Height of the nodes after Rotation 

    return B

def rightRotate(A):
    B=A.left
    temp=B.right    #Creating the copy of values

    B.right=A
    A.left=temp    #Rotating the nodes 

    A.height=1+max(ght(A.left),ght(A.right)) 
    B.height=1+max(ght(B.left),ght(B.right))   #Updating the Height of the nodes after Rotation 

    return B

def inorder(root):      #Print the data in inorder format
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    VL=[40,45,32,50,19,54,27,70,25,80,60,10,63,90]
    root=None
    for i in VL:
        root=insert(root,i)
    inorder(root)