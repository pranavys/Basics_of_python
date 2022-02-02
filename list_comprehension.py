num = [1, 2, 3]
doubled = [x * 2 for x in num]

print(doubled)

# Normal approach
friends = ["rolf", "pope", "olive", "sam"]
starts_s = []

for friend in friends:
    if friend.startswith("s"):
        starts_s.append(friend)

print(starts_s)

# Using list comprehension
friends = ["rolf", "pope", "olive", "sam"]
starts_s = [friend for friend in friends if friend.startswith("s")]

# for friend in friends:
#     if friend.startswith("s"):
#         starts_s.append(friend)

print(starts_s)

#

friends = ["sam", "fam"]
starts_s = ["sam", "fam"]
print(friends)
print(starts_s)

print(friends is starts_s)
print("friends:", id(friends), "starts_s:", id(starts_s))
