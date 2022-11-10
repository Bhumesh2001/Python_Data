# 1. python tuple
mytuple = ("apple", "banana", "cherry","banana")
print(mytuple[3]) 

mytuple = ("apple", "banana", "cherry","banana")
print(len(mytuple)) 

thistuple = ("apple",)
print(type(thistuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# access tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# update tuple.
# change tuple values.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# add tuple  to a tupule values.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# add tupule values.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# remove tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del(thistuple)
print(thistuple) #this will raise an error because the tuple no longer exists

unpak tupule.

packing tupule.
fruits = ("apple", "banana", "cherry")

# unpak tupule.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

Using Asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow,blue,*red) = fruits
print(green)
print(yellow)
print(blue)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

python loop tuple.
loop through a tupule

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
use for loop.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
use while loop.

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

python join tupule.
join two tupule
add.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

multiply tupule.

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

tuple methods
tupule count()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

tupule index()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

list  bhi store kar sakte hai. 

a = (2,23,4,["bhumesh","kewat"])
print(a)
