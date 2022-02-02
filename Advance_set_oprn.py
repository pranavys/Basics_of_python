friends= {"rolf", "bob", "anne"}
abroad = {"bob", "anne"}

local_frnds = abroad.difference(friends)
print(local_frnds)

#

local= {"rolf", "kodi", "kotte"}
abroad = {"bob", "anne"}

frnds = abroad.union(local)
print(frnds)

#

friends= {"rolf", "bob", "anne"}
abroad = {"bob", "anne", "bob", "anne"}

both = friends.intersection(abroad)
print(both)
