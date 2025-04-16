

# set is mutable but set elements are immutable
collection={1,2,"hari"}
# print(type(collection))
null_dictionary={}
null_set=set()

collection.add("rajesh")
print(collection)
# collection.remove("rajesh")
# collection.clear()
# collection.pop() #delete first element from set

# print(collection)

collection2={3,2,1}
# print(collection.union(collection2))
print(collection.intersection(collection2))
