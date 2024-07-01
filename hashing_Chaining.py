'''
Step1 : class for node -> inssert,search,delete
Step2: Input of elements as k
Step3: Hashing list of :[None]*len(k)
Step4: {find h_key=h(k)=k mod 10}--> loop from 0 to len(k)
'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Hash_Table:
    def __init__(self):
        self.head=self.tail=None

    #Inserting the elements in end of list
    def insert_end(self,v):
        nn=node(v)
        if self.tail==None:
            self.tail=self.head=nn
        else:
            self.tail.next=nn
            self.tail=nn

    #Displaying the elements of the chain
    def print_list(self):
        if self.head==None:
            print("None")
            return
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next
        print()

    #Finding the element in an chain list
    def find_key(self,key,i):
        if self.head==None:
            print("Element not stored")
            return
        curr=self.head
        while curr!=None:
            if curr.data==key:
                print(f"Key is found in {i}")
                return 
            curr=curr.next
        print("Element not found")

def display(res):
    for i in res:
        print(f"{res.index(i)} : ",end=" ")
        i.print_list()

def create_hash_table(k,res):
    for i in k:
        key=i%10
        res[key].insert_end(i)

#k=list(map(int,input().split()))
k=[10,16,62,100,20,86,72,7,76,99]
n=len(k)
res=[None]*n

#Creating the list of address of the head of the chains(linked-list) 
for i in range(n):
    res[i]=Hash_Table()

#Adding the elements of the input into the table based on k mod 10 algorithm
create_hash_table(k,res)

#displaying the hash table
display(res)

#Finding an element in an hash table
ele=int(input("Enter the element to be searched: "))
h=ele%10
res[h].find_key(ele,h)
