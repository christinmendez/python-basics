#factusing fun
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(6))
#fibo
def fib(num):
    x=0
    y=1
    i=0
    while i < num:
        print(x,end=' , ')
        z=x+y
        x=y
        y=z
        i+=1
n=int(input("enter the number:"))
fibionic=fib(n)
print(factorial)
#sum of a num
def sum(n):
    t=0
    for i in range(1,n+1):
        t+=i
    return t
n=int(input("enter a value"))
print(sum(n))
# sum_of_square
def sum_of_square(n1):
    return(n1*(n1+1)*(2*n1+1))//6
n=int(input("enter the number"))
print(sum_of_square(n))
l=int(input("enter a limit"))
for i in range(l):
    for j in range(l-i-1):
        print("",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
    
