# tuple: ordered, immutable, allows duplicate elements

mytuple = ("max", 28, "Boston")  # same as a list but cant be changed
mytuple2 = "max", 28, "Boston"  # paranthesis are optional
mytuple3 = ("max",)  # tuple with one value requires a comma
# create a tuple from an iterable(a list)
mytuple4 = tuple(["max", 28, "Boston"])

item = mytuple[0]  # grab by index, 0 based
item2 = mytuple[-1]  # Boston, -1 is last element, -2 is second last ...

# iterate over mytuple, print each element
for i in mytuple:
    print(i)

# check if the element exists
if "max" in mytuple:
    print("yes")
else:
    print("no")

mytuple5 = ('a', 'p', 'p', 'l', 'e')
length = len(mytuple5)  # returns the length
countp = mytuple5.count('p')  # returns the number of elements that match
firstp = mytuple5.index('p')  # returns index of first element that matches

mylist = list(mytuple)  # convert a tuple to a list
tupleFromList = tuple(mylist)  # convert a list to a tuple

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]  # 3,4,5 include start, exclude end
c = a[:5]  # start from beginning
d = a[3:]  # stop at the end

print(d)
