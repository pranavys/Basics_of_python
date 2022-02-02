l = ["bob", "polf", "anne"] 
#can add and remove elements from lists
#keep the order

t = ("bob", "polf", "anne")
#can not add and remove elements from tuples
#keep the order

s = {"bob", "polf", "bob"}
#can add and remove elements from sets
#can not have duplicate elements
#do not keep the order

print(l[0])
print(t[1])
#subscript notation
#sets won't allow it

#modify
l[0] = "sam"
print(l)
#tuples and sets won't allow this

l.append("will")
l.remove("sam")

s.add("sam")