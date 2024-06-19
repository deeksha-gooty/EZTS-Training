#Bubble sort logic

l=list(map(int,input().split()))
n=len(l)
for j in range(0,n):
    for i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

#Selection Sort

l=list(map(int,input().split()))
for i in range(0,len(l)):
    index=i
    min=l[i]
    for j in range(i+1,len(l)):
        if l[j]<min:
            min=l[j]
            index=j
    l[i],l[index]=l[index],l[i]
print(l)

#Insertion Sort Logic

l=list(map(int,input().split()))
n=len(l)
for i in range(1,len(l)):
    ele=l[i]
    index=i
    for j in range(i-1,-1,-1):
        if ele<l[j]:
            l[j+1]=l[j]
            index=j
        else:
            break
    l[index]=ele
print(l)

#Quick Sort

def partation(l,low,high):
    pivot=l[high]
    j=low-1
    pi=high
    for i in range(low,high):
        if l[i]<=pivot:
            j+=1
            l[j],l[i]=l[i],l[j]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi

def quick_sort(l,low,high):
    if low<high:
        pi=partation(l,low,high)
        print(pi,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return

if __name__=="__main__":
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    quick_sort(l,low,high)
    print(f"Sorted Array: {l}")

#Merge Sort Method 1

def merge(l,low,mid,high):
    left=l[low:mid+1]
    right=l[mid+1:high+1]
    i=j=0
    t=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l[t]=left[i]
            t+=1
            i+=1
        else:
            l[t]=right[j]
            t+=1
            j+=1
    while i<len(left):
        l[t]=left[i]
        t+=1
        i+=1
    while j<len(right):
        l[t]=right[j]
        t+=1
        j+=1
    print(l)

def merge_sort(l,low,high):
    if low<high:
        mid=low+(high-low)//2
        print(mid,l[low:mid+1],l[mid+1:high+1])
        merge_sort(l,low,mid)
        print(mid)
        print(mid,l[low:mid+1],l[mid+1:high+1])
        merge_sort(l,mid+1,high)
        merge(l,low,mid,high)
    return

if __name__=="__main__":
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    merge_sort(l,low,high)
    print(f"Sorted Array: {l}")

#Merge Sort Method 2

def merge(left,right):
    i=j=0
    temp=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1  
    while i<len(left):
        temp.append(left[i])
        i+=1        
    while j<len(right):
        temp.append(right[j])
        j+=1

    return temp

def mergesort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left=l[:mid] 
    right=l[mid:]
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    return merge(left_sorted,right_sorted)

if __name__=="__main__":
    l=list(map(int,input().split()))
    sorted=mergesort(l)
    print(f"Sorted Arrar is {sorted}")
