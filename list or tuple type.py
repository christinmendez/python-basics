fruits=["apple","orange","mango","peach","grape","pineapple"]
print(fruits)
print(len(fruits))
print(type(fruits))
num=list((7,10,11,33,1,777,2255,666,777))
print(num)
print(fruits[1])
print(fruits[-1])
print(fruits[2:5])
print(fruits[:5])
print(fruits[1:])
print(fruits[-5:-1])
print("apple" in fruits)
print("musambi" in fruits)
print("musambi" not in fruits)
print("apple" not in fruits)
fruits[1]="blueberry"
print(fruits)
fruits[2:4]=["banana","guva"]
print(fruits)
fruits.append("mangochili")
print(fruits)
fruits.insert(2,"passionfruit")
print(fruits)
fruits.extend(num)
print(fruits)
fruits.remove("passionfruit")
print(fruits)
fruits.pop(1)
print(fruits)
fruits.pop()
print(fruits)
del fruits[-1]
print(fruits)
# fruits.clear()
# print(fruits)
# del fruits
# print(fruits)
for i in fruits:
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
xy=fruits+mix
print(xy)
list1=["a","b","c"]
list2=[1,2,3,3,3]
for i in list2:
    list1.append(i)
print(list1)
d=list2.count(3)
print(d)