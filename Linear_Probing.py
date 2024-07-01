#Closed Hashing Based on Linear Probing 
k=[22,47,56,99,79]
n=len(k)
res=[False]*n
for i in k:
    j=0
    j_key=i%n
    while res[j_key]!=False and j<n:
        j_key=((i%10)+j)%n
        j+=1
    res[j_key]=i

print(res)



#Closed Hashing Based on Quadratic Probing form
k=[22,47,56,99,79]
n=len(k)
res=[False]*n
for i in k:
    j=0
    j_key=i%n
    while res[j_key]!=False and j**2<n:
        j_key=(((i+j**2)%10))%n
        j+=1
    res[j_key]=i

print(res)