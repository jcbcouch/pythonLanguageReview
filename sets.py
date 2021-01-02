# sets: unordered, mutable, no duplicates
myset = {1,2,3}
noduplicates = {1,2,3,1,2} #this contains 1,2,3 wont get duplicates
fromIterable = set([1,2,3]) #get a set from an iterable(list)
setFromString = set("Hello") #contains (o,l,H,e) unordered, no duplicates
emptySet = set() #empty set, {} creates a dictionary

myset2 = {1,2,3}
myset2.add(4) #push an element
myset2.remove(1) #remove the passed in element(must exist in the set)
myset2.discard(6) #same as remove but will do nothing if not found
randomElement = myset2.pop() #return and remove a random element 
myset2.clear() #remove all elements

myset3 = {1,2,3,4}
#iterate over set and print each element
for i in myset3:
    print(i)

#check if element in set
if 5 in myset3:
    print('yes')
else:
    print('no')

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

union = odds.union(evens) #combine without duplicates
intersecion = odds.intersection(primes) #combine shared elements no duplicates {3,5,7}

a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3,10,11,12}
diff = a.difference(b) #return everything in a that is not in b {4,5,6,7,8,9}
diff2 = b.difference(a) #{10,11,12}
symDiff = a.symmetric_difference(b) #return all except elements in both sets {4,5,6,7,8,9,10,11,12}

print(symDiff)