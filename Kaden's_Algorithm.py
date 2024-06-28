num=[-3,5,3,-2,6,1,9,-3]
curr=0
maxsum=float('-inf')
for i in num:
    curr=curr+i
    maxsum=max(curr,maxsum)
    if curr<0:
        curr=0
print(maxsum)