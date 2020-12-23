# Dictionaries: key-value pairs, unordered, mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict2 = dict(name="Mary", age=27, city="Boston")

value = mydict["name"]  # grab a key, value
# value2 = mydict["lastName"]  will raise an exception, value missing
mydict["email"] = "max@xyz.com"  # set a new key, value
mydict["email"] = "coolmax@xyz.com"  # change the value for a key
del mydict["name"]  # removes key, value
mydict.pop("age")  # removes key,value
mydict.popitem()  # removes last key, value

# print value if key is there
if "name" in mydict2:
    print(mydict2["name"])

# print value if key is there
# otherwise print "error"
try:
    print(mydict2["name2"])
except:
    print("error")

# loop through keys, print all keys
for key in mydict2:
    print(key)

# same, keys method returns list of keys
for key in mydict2.keys():
    print(key)

# loop and print values
for value in mydict2.values():
    print(value)

# loop and print key and value
for key, value in mydict2.items():
    print(key, value)

mydict_cpy = mydict2  # pass memory reference
mydict_cpy["name"] = "sarah"  # this will modify org and copy
mydict_cpy2 = mydict2.copy()  # pass value
mydict_cpy2["age"] = 30  # this will not modify original
mydict_cpy3 = dict(mydict2)  # pass value
mydict_cpy3["age"] = 55  # this will not modify original

mydict3 = dict(name="jacob", age=25, email="jcbcouch2@gmail.com")
mydict4 = dict(name="eric", age=50, city="Ponder")

mydict3.update(mydict4)  # update existing keys, add new key value pairs

# dictionary key must be of a type that is immutable. For example, you can use an integer, float, string, or
# Boolean as a dictionary key. However, neither a list nor another dictionary can serve as a dictionary key,
# because lists and dictionaries are mutable. Values, on the other hand, can be any type and can be used more than once.
# they can contain tuples if they only contain immutable elements
