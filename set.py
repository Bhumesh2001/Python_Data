plythin sets.

myset = {"apple", "banana", "cherry"}
print(myset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

python access set items.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)    
  
Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

add set items.
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

add sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
# print(thisset)

# remove set item.

# remove method.
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# # discard method.
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# pop method
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# clear method se .

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# del method 

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# loop set.

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# python join set

# union methods

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# # update method
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

#Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# Example
# Keep the items that exist in both set x, and set y:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)

# intersection method.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# Example
# Keep the items that are not present in both sets:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# Example
# Return a set that contains all items from both sets, except items that are present in both:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)


# Python Set issuperset() Method

# Return True if all items set y are present in set x:

# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

# Python Set issubset() Method

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)

# Python Set isdisjoint() Method

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}

# z = x.isdisjoint(y)

# print(z)

# Python Set copy() Method

# fruits = {"apple", "banana", "cherry"}

# x = fruits.copy()

# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","apple"}
# x.difference_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference(y)
# print(x)
