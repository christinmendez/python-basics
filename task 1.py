x="hello python"
print(x)
print(type(x))
print(len(x))
print(x[0])
for i in x:
    print(i)
y="    python, is, a ,coding, language ,   "
print(y)
print("coding"in y)
print("coding" not in y)
print(y[2:5])
print(y[0:])
print(y[:8])
print(y[-5:-1])
print(y.upper())
print(y.lower())
print(y.strip())
print(y.replace("p","y"))
print(y.split(","))
print(x+"."+y)
pig=78
text="i have {} pig in my farm"
print(text.format(pig))
print(text.count("pig"))