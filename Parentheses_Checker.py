class stack:
    def __init__(self):
        self.items=[]
    def push(self,b):
        self.items.append(b)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

#Method 1
s=stack()
exp=input()
flag=True
for i in exp:
    if i =="(" or i=="{" or i=="[":
        s.push(i)
    elif i ==")" or i=="}" or i=="]":
        r=s.pop()
        if (i==")" and r!="(") or (i=="}" and r!="{") or (i=="]" and r!="["):
            flag=False
            break

if flag and s.size()==0:
    print("valid")
else:
    print("Invalid")


#Method 2
# s=stack()
# exp=input()
# flag=True
# op="({["
# cl=")}]"
# for i in exp:
#     if i in op:
#         s.push(i)
#     elif i in cl:
#         r=s.pop()
#         if (i==")" and r=="("):
#             pass
#         elif (i=="}" and r!="{"):
#             pass
#         elif (i=="]" and r!="["):
#             pass
#         else:
#             flag=False
#             break
# if flag and s.size()==0:
#     print("valid")
# else:
#     print("Invalid")


#Method 3
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     def display(self):
#         print(self.items)
#     def top(self):
#         if len(self.items)==0:
#             return 0
#         return self.items[-1]
    
# st = Stack()
# exp = "{[3+4{43/11(3+5})]}"
# for i in exp:
#     if i in "{[(":
#         st.push(i)
#     elif i == "]" and st.top()=="[":
#         st.pop()
#     elif i==")" and st.top()=="(":
#         st.pop()
#     elif i=="}" and st.top()=="{":
#         st.pop()
#     elif i in "]})":
#         st.push(i)  

# if st.size()==0:
#     print("valid")
# else:
#     print("invalid")