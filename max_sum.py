# Question1
#given an integer array your task is to find the 3 continuous digits which give you the maximum sum.
#Sample input:  [2,4,3,5,6,3,4,6,7,1,2,5]
#sample output: [4,6,7]

#Method 1
# def max_sum(lst):
#     s=[]
#     for i in range(len(lst)-2):
#         s.append(sum(lst[i:(i+3)])) 
#     m=s.index(max(s))
#     result=lst[m:m+3]
#     return result

#Method 2
def max_sum(lst):
    m=s=0
    for i in range(0,len(lst)-2):
        s=lst[i]+lst[i+1]+lst[i+2]
        if s>m:
            m=s
            pos=i
    result=lst[pos:pos+3]
    return result
   
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(lst))  


# Question2
#given an integer array your task is to find the k continuous digits which give you the maximum sum.
#Sample input:  3
#               [2,4,3,5,6,3,4,6,7,1,2,5]
#sample output: [4,6,7]

def max_sum(k,lst):
    m=s=0
    for i in range(len(lst)-(k-1)):
        s=(sum(lst[i:(i+k)]))
        if s>m:
            m=s
            pos=i
    result=lst[pos:pos+k]
    return result

k=int(input())
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(k,lst))  


