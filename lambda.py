from functools import reduce

add10 = lambda x: x + 10 #lambda function
add10(5) #returns 15

#this non lambda function does the same thing
def add10_func(x):
    return x + 10
add10_func(5) #returns 15

mult = lambda x,y: x*y #lambda can take multiple arguemnts
mult(2,3) #returns 6

points2d = [(1,2),(15,1),(5,-1),(10,4)] #list of tuples
points2dSorted = sorted(points2d) #sorted by first index of each tuple
points2dSorted2 = sorted(points2d, key=lambda x: x[1]) #sorted by the second index of each tuple

#this will do the same, just with a regular function
def sortByY(x):
    return x[1]
points2dSorted3 = sorted(points2d, key=sortByY)

#sort by sum of both elements in each tuple
points2dSorted4 = sorted(points2d, key= lambda x: x[0] + x[1])

a = [1,2,3,4,5,6]
#map over a, return each element multiplied by 2
b = list(map(lambda x: x*2,a))
c = [x*2 for x in a] #this will do the same via list comprehension
d = list(filter(lambda x: x%2==0, a)) #this will only return even numbers
e = [x for x in a if x%2==0] #this will do the same via list comprehension
f = reduce(lambda x,y: x*y, a) #reduce to 720, multiply each element
