flower=["jasmin","rose","lotus","lilly","hibiscus"]
print(flower)
print(type(flower))
print(len(flower))
x=list((10,20,30,40,50,60,70))
print(x)
print(flower[0])
print(flower[-1])
print(flower[0:5])
print(flower[-5:-1])
print(flower[0:])
print(flower[:2])
print("rose"in flower)
print("dalliya" in flower)
print("daliya"not in flower)
flower[1]="sunflower"
print(flower)
flower[-3:-1]=["rose","daliya"]
print(flower)
flower[1]="blueberry"
print(flower)
flower[2:4]=["banana","guva"]
print(flower)
flower.append("mangochili")
print(flower)
flower.insert(2,"passionfruit")
print(flower)
flower.extend(x)
print(flower)
flower.remove("passionfruit")
print(flower)
flower.pop(1)
print(flower)
flower.pop()
print(flower)
for i in flower:
    print(i)
colors=["red","blue","green","yellow","skyblue"]
print(colors)
colors.sort()
print(colors)
for i in colors:
    print(i)
colors.sort(reverse=True)
print(colors)
mix=colors.copy()
print(mix)
z=list(mix)
print(z)
xy=flower+mix
print(xy)
list1=["a","b","c"]
list2=[1,2,3,3,3]
for i in list2:
    list1.append(i)
print(list1)
d=list2.count(3)
print(d)