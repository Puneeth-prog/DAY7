a=[12,21,31,40]
b=len(a)
c=5   #number of students in class

if c>b:
    print("not possible to distribute manga bag to all student \n")
elif c==b:
    print("one bag can be given to each students succesfully \n")
else:
    d=b-c
    print(d)
    print(" mango bag will be remained after distributing each bag")
z=min(a)
y=max(a)
x=y-z
print(x )
print("is the difference between maximum and minimum number of mango bags")

