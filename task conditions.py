x=int(input("enter a value"))
if x<0:
    print(" x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is equal")
ab=int(input("enter a number"))
if ab%2==0:
    print("it is even number")
else:
    print("it is odd number")
x=int(input("enter a value"))
y=int(input("enter a second value"))
z=input("enter a oprator")
if z=="+":
    sum=x+y
    print(sum)
elif z=="-":
    dif=x-y
    print(dif)
elif z=="/":
    div=x/y
    print(div)
elif z=="*":
    mult=x*y
    print(mult)
else :
    print("invalid operator")
no=int(input("enter a number"))
fact=1
while(no>1):
    fact=fact*no
    no=no-1
print(fact)
x=int(input("enter a num"))
n1=0
n2=1
print("fibonicci series")
for y in range (0,x):
    if y<=1:
        n3=y
    else:
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3,end='')
    