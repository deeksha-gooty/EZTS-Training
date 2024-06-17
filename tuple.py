#The program to create a tuple without repeating elements from the give tuple
#Method 1
tuple1=(1,2,3,2,4,1)
tuple2=[]
for i in tuple1:
    if i not in tuple2:
        tuple2.append(i)
tuple2=tuple(sorted(tuple2))
print(tuple2)
#Method 2
tuple1=(1,2,3,2,4,1)
for i in sorted(list(tuple1)):
    if i not in tuple2:
        tuple2=(i,)
print(tuple2)
#Method 3
tuple1=(1,2,3,2,4,1)
tuple2=tuple(set(tuple1))
print(tuple2)