a={"name":"aravindh","age":48,"job":"hub opreator"}
print(a)
print(type(a))
print(len(a))
y={"name":"jayanthy","age":43,"job":"house wife"}
print(y)
print(a["age"])
print(a.get("name"))
xy=a.keys()
print(xy)
xy=a.values()
print(xy)
xy=a.items()
print(xy)
print("christin" in a)
print("christin" not in a)
a["age"]=22
print(a)
a.update({"name":"appu"})
print(a)
a.update({"DOB":"3-10-2001"})
print(a)
a["place"]="padiyoor"
print(a)
a.pop("place")
print(a)
a.popitem()
print(a)
del a["age"]
# print(a)
# x.clear()
# print(a)
# del a
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
xy=a.copy()
print(xy)
yx=dict(a)
print(yx)
fmly={"child1":{"name":"biethel","age":5},"child2":{"name":"ihana","age":7},"child3":{"name":"ihan","age":1}}
print(fmly)
print(fmly["child3"]["name"])
print(fmly["child2"]["name"])


