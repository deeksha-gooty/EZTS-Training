#In Recursion function if there is no base case then it leads to 
#RecursionError: "Maximin Recursion Depth Exceeded" 
#Recursion for printing nth fibonacci number
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

if __name__=="__main__":
    n=int(input())
    print(fibo(n))

#Recursion for finding Factorial
def fact(n):
    if n==0:
        return 1
    return (n*fact(n-1))

if __name__=="__main__":
    n=int(input())
    print(fact(n))