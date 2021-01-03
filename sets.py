# sets: unordered, mutable, no duplicates
myset = {1, 2, 3}
noduplicates = {1, 2, 3, 1, 2}  # this contains 1,2,3 wont get duplicates
fromIterable = set([1, 2, 3])  # get a set from an iterable(list)
setFromString = set("Hello")  # contains (o,l,H,e) unordered, no duplicates
emptySet = set()  # empty set, {} creates a dictionary

myset2 = {1, 2, 3}
myset2.add(4)  # push an element
myset2.remove(1)  # remove the passed in element(must exist in the set)
myset2.discard(6)  # same as remove but will do nothing if not found
randomElement = myset2.pop()  # return and remove a random element
myset2.clear()  # remove all elements

myset3 = {1, 2, 3, 4}
# iterate over set and print each element
for i in myset3:
    print(i)

# check if element in set
if 5 in myset3:
    print('yes')
else:
    print('no')

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)  # combine without duplicates
# combine shared elements no duplicates {3,5,7}
intersecion = odds.intersection(primes)

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
diff = a.difference(b)  # return everything in a that is not in b {4,5,6,7,8,9}
diff2 = b.difference(a)  # {10,11,12}
# return all except elements in both sets {4,5,6,7,8,9,10,11,12}
symDiff = a.symmetric_difference(b)

c = {1, 2, 3, 4, 5, 6, 7, 8, 9}
d = {1, 2, 3, 10, 11, 12}
c.update(d)  # add all of d to c no duplicates

e = {1, 2, 3, 4, 5, 6, 7, 8, 9}
f = {1, 2, 3, 10, 11, 12}
e.intersection_update(f)  # update e with all elements found in both sets

g = {1, 2, 3, 4, 5, 6, 7, 8, 9}
h = {1, 2, 3, 10, 11, 12}
g.difference_update(h)  # remove all elements from g that exist in h

i = {1, 2, 3, 4, 5, 6, 7, 8, 9}
j = {1, 2, 3, 10, 11, 12}
i.symmetric_difference_update(j)  # i gets all except for those found in both

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
subsetTruth = setB.issubset(setA)  # returns true because all of b exists in a
# returns true because a includes everything in b
supersetTruth = setA.issuperset(setB)
# returns false because they share elements
disjointTruth = setA.isdisjoint(setB)

firstSet = {1, 2, 3, 4, 5, 6}
newSet = firstSet  # pass memory reference
newSet.add(7)  # this will modify firstSet and newSet
newSet2 = set(firstSet)  # pass value
newSet2.add(8)  # this will not modify firstSet
newSet3 = firstSet.copy()  # pass value
newSet3.add(9)  # this will not modify firstSet

frozenSet = frozenset([1, 2, 3, 4])  # same as set but immutable.
