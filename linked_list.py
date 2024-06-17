'''------------------------------------------------------------------------------------------------------------

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=tail=node(10)
tail.next=node(20)
tail=tail.next

tail.next=node(30)
tail=tail.next

tail.next=node(40)
tail=tail.next

def print_list(head):
    if head==None:
        print("List is empty")
        return
    curr=head
    while curr!=None:
        print(curr.data)
        curr=curr.next

# head=node(10)
# head.next=node(20)
# head.next=node(30)


print(head)
print(tail)
print(head.next.next.next)
print(print_list(head))
--------------------------------------------------------------------------------------------------'''
import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=self.tail=None

    def insert_front(self,v):
        nn=node(v)
        if self.head==None:
            self.head=self.tail=nn
        else:
            nn.next=self.head
            self.head=nn
    def insert_end(self,v):
        nn=node(v)
        if self.tail==None:
            self.tail=self.head=nn
        else:
            self.tail.next=nn
            self.tail=nn
    def insert_pos(self,v,pos):
        nn=node(v)
        if pos==0:
            nn.next=self.head
            self.head=nn
            return
        c=0
        curr=self.head
        while curr!=None and c<pos-1:
            c=c+1
            curr=curr.next
        if curr==None:
            print("Position not found.")
            return
        nn.next=curr.next
        curr.next=nn
    def delete_front(self):
        if self.head==None:
            print("No elements")
        else:
            self.head=self.head.next
    def delete_end(self):
        if self.head==None:
            print("No Elements")
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None
            self.tail=curr
    def delete_anywhere(self,pos):
        if self.head==None:
            print("Linked list is Empty")
            return
        if pos==0:
            self.head=self.head.next
            return
        curr=self.head
        c=0
        while curr!=None and c<pos-1:
            curr=curr.next
            c=c+1
        if curr==None or curr.next==None:
            print("Position not found")
            return
        if curr.next==self.tail:
            self.tail=curr
        curr.next=curr.next.next
        
    def print_list(self):
        if self.head==None:
            print("List is empty")
            return
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next  
    
s=linked_list()
while True:
    print("1.Front Insertation\n2.End Insertation\n3.Insertation Anywhere \n4.Display\n5.Delete Front\n6.Delete End\n7.Delete Anywhere\n8.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        v=int(input("Enter the value to be inserted:"))
        s.insert_front(v)
    elif ch==2:
        v=int(input("Enter the value to be inserted:"))
        s.insert_end(v)
    elif ch==3:
        v=int(input("Enter the value to be inserted:"))
        p=int(input("Enter the position:"))
        s.insert_pos(v,p)
    elif ch==4:
        s.print_list()
    elif ch==5:
        s.delete_front()
    elif ch==6:
        s.delete_end()
    elif ch==7:
        p=int(input("Enter the position:"))
        s.delete_anywhere(p)
    elif ch==8:
        sys.exit()
    else:
        print("invalid")




