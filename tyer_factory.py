#Identifying the Factory Supervisor for the give list of workers
#3 5 2 14 5 3 7 9 4 6 9 4 2 5 3

#Method 1 Using Stack
class stack:
    def __init__(self):
        self.items=[]
    def push(self,b):
        self.items.append(b)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def top(self):
        return self.items[-1]
    
s=stack()
ip=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
o=[0]*len(ip)
for i in range(len(ip)-1,-1,-1):
    if s.size()!=0:
        while s.size()!=0 and s.top()<=ip[i]:
            if s.top()<=ip[i]:
                s.pop()
    if s.size()==0:
        o[i]=-1
    else:
        o[i]=s.top()
    s.push(ip[i])
print(o)

#Mehtod 2 Without using Stack, by using Looping
ip=list(map(int,input().split()))
op=[-1]*len(ip)
for i in range(len(ip)):
    for j in range(i,len(ip)):
        r=-1
        if ip[j]>ip[i]:
            r=ip[j]
            op[i]=r
            break
print(op)
    