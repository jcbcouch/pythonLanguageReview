# Lists: ordered, mutable, allows duplicate elements, combine data types
mylist = ["banana", "cherry", "apple"]
item = mylist[0]  # banana
item2 = mylist[-1]  # apple, -1 is last element, -2 is second last ...

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")

length = len(mylist)  # return number of elements in list
mylist.append("lemon")  # add to the end
mylist.insert(1, "blueberry")  # insert at index of first parameter
# everything after moves a step closer to the end
removed = mylist.pop()  # remove last item and return it
mylist.remove("banana")  # remove item of parameter
mylist.sort()  # same as javascript but looks beyond first digit
mylist.reverse()
newlist = sorted(mylist)  # same as sort but returns list
mylist.clear()  # remove all elements

mylist2 = [0] * 5  # list of [0 0 0 0 0]
concat1 = [1, 2, 3]
contac2 = [3, 4, 5]
combine = concat1 + contac2  # concat to make [1,2,3,4,5]

mylist3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist3[0:5]  # [1,2,3,4,5] between indexes but include first index
b = mylist3[:5]  # [1,2,3,4,5] no start, start from beginnning
c = mylist3[5:]  # [6,7,8,9] no stop, goes to the end
d = mylist3[1:8:2]  # [2,4,6,8] start : stop : step
e = mylist3[-1:-10:-2]  # first number starts from the right
# because the step makes its reverse

list_org = [1, 2, 3, 4]
list_copy = list_org  # pass memory reference
list_copy.append(5)  # this will modify org and copy
list_copy2 = list_org.copy()  # pass value
list_copy2.append(6)  # this will not modify org
list_copy3 = list(list_org)  # pass value
list_copy3.append(100)  # this will not modify org
list_copy4 = list_org[:]  # pass value
list_copy4.append(500)  # this will not modify org

a_list = [1, 2, 3, 4, 5]
b_list = [i*i for i in a_list]  # [1,4,9,16,25]

print(b_list)
