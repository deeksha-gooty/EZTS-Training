#Sipmle Calculator

s=input("Enter a string:")
operator=["+","-","*","/"]
for i in operator:
    if i in s:
        op=i
        s=s.replace(i," ")
        break
result=list(map(float,s.split()))
match op:
    case "+": 
        r=result[0]+result[1]
        print(r)
    case "-": 
        r1=result[0]-result[1] 
        print(r1)
    case "*": 
        r2=result[0]*result[1]
        print(r2)
    case "/": 
        r3=result[0]/result[1]
        print(r3)
    case _:
        print("Invalid")
    