#Printing of solid shapes 
print("enter square size:")
n=int(input())
print("solid square")
for i in range(n):
    for i in range(n):
        print("*",end=" ")
    print()


print("Enter length and bredth of rectangle:")
l=int(input())
b=int(input())
for i in range(b):
    for j in range(l):
        print("*", end=" ")
    print()


print("value of n:")
m=int(input())
print("\nNormal Triangle:\n")
for i in range(1,m+1):
    print(" "*(m-i),end="")
    print("* "*(i))

print("\n\nInverted Triangle:\n")
for i in range(m,0,-1):
    print(" "*(m-i)+"* "*(i))

print("\n\nTriangle Pattern:\n")
for i in range(1,m+1):
    print(" "*(m-i)+"* "*(i),end=" ")
    print(" "*(m)+"* "*(m-i+1))

'''
row=5
max_width=len((' *')*row)
for i in range(1,row+1):
    stars=' '.join('*'*i)
    leading_spaces=(max_width-len(stars))//2
    print(' '*leading_spaces+stars)

'''
print("\n\nRight Angle Triangle:")
def right_triangle(row):
    for i in range(1,row+1):
        print("* "*(i))

print("\nEnter the value of n:\n")
n=int(input())
print()
right_triangle(n)
'''
row=5
for i in range(1,row+1):
    stars=' '.join('*'*i)
    print(stars)

'''
