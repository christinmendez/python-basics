def hieght():
    print(6.1)
hieght()
def how(*t):
    print(t[3])
how(1,2,3,4)
def tact(a,b,c):
    print(b)
tact(a=10,b=20,c=30)
def tuf(**r):
    print(r["boy"])
tuf(b="monkey",boy="male")
def mycountry(country="india"):
    print(country)
mycountry("saudi arabia")
mycountry("serbia")
mycountry()
def hell(x):
    return 10+x
print(hell(10))
def add(x,y):
    return x+y
print(add(10,20))
def man(ab):
    pass
y=lambda x:x+10
print(y(240))
a=lambda b,c,d:b+c+d
print(a(20,30,50))
def sum(n):
    t=0
    for i in range(1,n+1):
        t+=i
    return t
n=int(input("enter a valve"))
print(sum(n))






