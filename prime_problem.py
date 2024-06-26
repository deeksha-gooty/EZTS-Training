# In the enchanted land of Numeria, Alice is on a quest to find the legendary
# Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an
# ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the
# Prime Key.
# The puzzle consists of multiple levels, each requiring Alice to solve a different
# challenge involving prime numbers. To progress through each level, Alice must
# perform the following tasks:
# Level 1: Find the smallest prime number larger than a given integer N.
# Level 2: Calculate the sum of all prime numbers between N and the smallest
# prime number larger than N.
# Level 3: Determine if the product of the smallest prime number larger than N
# and the next immediate prime number is also a prime.
# To complete the puzzle and retrieve the Prime Key, Alice must solve these
# challenges in sequence for a given integer N.
# Your task is to write a function that takes an integer N and returns a tuple
# containing the following:
# - The smallest prime number larger than N (Level 1 result).
# - The sum of all prime numbers between N and the smallest prime number
# larger than N (Level 2 result).
# - A boolean indicating whether the product of the smallest prime number
# larger than N and the next immediate prime number is prime (Level 3 result).
# Help Alice navigate through the levels, solve the puzzle, and obtain the Prime
# Key to unlock the Vault of Secrets.

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
        return 0

def next_prime(k):
    flag=0
    while flag<1:
        flag=check_prime(k)
        if flag==1:
            return k
        else:
            k+=1

result=[]
n=int(input())
k=n+1
result.append(next_prime(k))
sum=0
for i in range(n+1,result[0]):
    sum+=i
result.append(sum)

p1=result[0]
k=p1+1
p2=next_prime(k)

p3=p2*p1
bo=check_prime(p3)
if bo==0:
    result.append("False")
else:
    result.append("True")

Prime_Key=tuple(result)
print(Prime_Key)