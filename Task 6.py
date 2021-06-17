# Write a Python script to merge two Python dictionaries

a={"Ford":"Mustang","Lamborghini":"Aventador"}
b={"Toyota":"Supra","Nissan":"GT-R"}
a.update(b)
print(a)

print()
print()

# Write a Python program to remove a key from a dictionary

print(a)
print()
if "Toyota" in a:
    del a["Toyota"]
print(a)

print()
print()

# Write a Python program to map two lists into a dictionary

keys=['Messi','Cristiano Ronaldo','Neymar jr']
values=[10,7,11]
dictionary=dict(zip(keys,values))
print(dictionary)

print()
print()

# Write a Python program to find the length of a set

set={1,2,3,4,5,6,7,8,9}
print(set)
print(len(set))

print()
print()

# Write a Python program to find the length of a set

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1)
print(set2)
print("using difference_update()")
set1.difference_update(set2)
print(set1)
print(set2)
print("using compound assignment operator")
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set1-=set2
print(set1)
print(set2)
