'''
It is a technique that is used as a solution for the colision in the Hashing.
In this Technique, Hashing is done for two times.
        h1Key= k mod (a prime number >=11)
        h2key= 8 - (k mod 8)   //any number whose sum with the above taken prime number is prime
        hkey= (h1key+ i * h2key) mod 11

[20,34,45,70,56]
[81,104,37,46,39]


in_p=[20,34,45,70,56,81,104,37,46,39]
n=len(in_p)
res=[False]*11
for i in in_p:
    j=0
    h1=i%11
    h2=8-(i%8)
    hk=h1
    while res[hk]!=False and j<11:
        j+=1
        hk=(h1+j*h2)%11
    res[hk]=i
print(res)

        
'''

#General Double Hashing

def next_prime(k):
    flag=0
    while flag<1:
        flag=check_prime(k)
        if flag==1:
            return k
        else:
            k+=1

def check_prime(m):
    flag=True
    if m<1:
        flag=False
    elif m==1:
        flag=True
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=False
                break
    if flag:
        return 1
    else:
        return next_prime(m+1)


in_p=[20,34,45,70,56,81,104,37,46,39]
n=len(in_p)
n=check_prime(len(in_p))
if n==1:
    n=len(in_p)
res=[False]*n
k=check_prime(n+1)
m=k-n
print(n)
print(m)
for i in in_p:
    j=0
    h1=i%n
    h2=m-(i%m)
    hk=h1
    print(hk)
    while res[hk]!=False and j<11:
        j+=1
        hk=(h1+j*h2)%11
    print(hk)
    res[hk]=i
    print(res)
print(res)










