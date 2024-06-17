# Given an interger array your task is to find the K continious digits which gives you the maximum sum.
# Where K is entered by user
# sample input [2,4,3,5,6,3,4,6,7,1,2,5]
# output: [4,6,7]

def max_sum(k,lst):
    window=max=0
    window=sum(lst[:k])   #window
    lst.append(0)
    for i in range(0,len(lst)-k):
        if max<window:
            max=window
            pos=i
        window=window-lst[i]+lst[i+k]      #slider
    result=lst[pos:pos+k]
    return result

k=int(input("Enter the number of continuous inputs: "))
#lst=list(map(int,input().split()))
lst=[2,4,3,5]#,6,3,4,6,7,1,2,5]
print(max_sum(k,lst)) 