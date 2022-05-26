import itertools
 
s = "abc"

perm_set = itertools.permutations(s)
for val in perm_set:
    print(val)