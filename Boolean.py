print(5 == 5)
print(5 > 5)
print(10 != 10)

#comparisions: ==, !=, >, <, >=. <=

friends= {"bob", "anne"}
abroad = {"bob", "anne"}

print(friends == abroad)
#checks if same elements are present inside two sets

print(friends is abroad)
#checks if elements present in sets are exact same elements

print(friends is friends)

# 

friends= {"bob", "anne"}
abroad = friends

print(friends is abroad)
