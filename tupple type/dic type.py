x={"name":"christin","age":23,"job":"buisness"}
print(x)
print(type(x))
print(len(x))
y=dict(name="anagha",age=21,job="data analyst")
print(y)
print(x["age"])
print(x.get("name"))
xy=x.keys()
print(xy)
xy=x.values()
print(xy)
xy=x.items()
print(xy)
print("christin" in x)
print("christin" not in x)
x["age"]=22
print(x)
x.update({"name":"appu"})
print(x)
x.update({"DOB":"3-10-2001"})
print(x)
x["place"]="padiyoor"
print(x)
x.pop("place")
print(x)
x.popitem()
print(x)
del x["age"]
# print(x)
# x.clear()
# print(x)
# del x
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
xy=x.copy()
print(xy)
yx=dict(x)
print(yx)
fmly={"child1":{"name":"biethel","age":5},"child2":{"name":"ihana","age":7},"child3":{"name":"ihan","age":1}}
print(fmly)
print(fmly["child3"]["name"])
print(fmly["child2"]["name"])

