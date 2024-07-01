class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("dequeue from empty queue")
    
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

queue = QueueUsingStacks()
while True:
    print("\n1.Insert\t2.Delete\t3.Size\t4.Display\t5.Exit")
    ch=int(input())
    if ch==1:
        n=int(input("Enter the element:"))
        queue.enqueue(n)
    elif ch==2:
        print(queue.dequeue())
    elif ch==3:
        print(queue.size())
    elif ch==4:
        print(queue.stack1,queue.stack2)
    elif ch==5:
        break
 
