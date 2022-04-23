# Q.1
# def max(a,b,c):
#     if a > b and a > c:
#         print(a,"is greater")
#     elif b > c and b > a:
#         print(b," is greater")
#     else:
#         print(c,"is greater")

# a = int(input("enter the number: "))
# b = int(input("enter the number: "))
# c = int(input("enter the number: "))

# max(a,b,c)

# Q.2

# def sum (a):
#     a = 0
#     for j in y:
#         a += j
#     return a
# y = [8, 2, 3, 0, 7]
# print(sum(y))


# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))

# Q.3

# def mul(into):
#     mul = 1
#     for j in into:
#         mul *= j
#     return mul
# print(mul(((8, 2, 3, -1, 7))))


# def into(mul):
#     mul = 1
#     for i in a:
#         mul *= i
#     return mul
# a = [8, 2, 3, -1, 7]
# print(into(a))


# Q.4

# def string(t):
#     t[::-1]
#     print(t)
# string(("1234abcd"))


# def string(t):
#     t[::-1]
#     return t
# print(string(("1234abcd")))


# def stringReverse(string):
#     b = ''
#     for i in range(len(string)):
#         b = string[::-1]
#     print(b)
# n = input("enter your charecter: ")
# stringReverse(n)


# def convertion(list):
#     i = len(list) - 1
#     while i >= 0:
#         print(list[i])
#         i -= 1
# print(convertion("1234abcd"))

# Q.5

# def factorial(h):
#     a = 1
#     while h > 0:
#         a *= h
#         h -= 1
#     print("factor = ",a)
# m = int(input("enter the number: "))
# factorial(m)


# Q.6

# def check(r):
#     if r in range(1,10):
#         print(r," is a given range")
#     else:
#         print(r," is not a given range")

# b = int(input("check your number given range is or not: ")) 
# check(b)


# Q.7

# def upper_lower(e):
#     d = {"upper case":0,"lower case":0}
#     for j in e:
#         if j.isupper():
#             d["upper case"] += 1
#         elif j.islower():
#             d["lower case"] += 1
#         else:
#             pass
#     print("no. of upper case charecter is ",d["upper case"])
#     print("no. lower case charecter is ",d["lower case"])

# upper_lower('The quick Brown Fox')


# def calc(s):
#     upper = [i for i in s if i.isupper()]
#     lower = [i for i in s if i.islower()]
#     print('No. of Upper case characters : ',len(upper),'\n','No. of Lower case Characters : ',len(lower))
# b = input("enter your charecter: ")
# calc(b)

# Q.8

# def lis(h):
#     n = []
#     for j in m1:
#         if j not in n:
#             n.append(j)
#     print(n)
# m1 = [1,2,3,3,3,3,4,5]
# lis(m1)

# Q.9

# def prime_number_check(n):
#     if n > 1:
#         for j in range(2,n):
#             if n % j == 0:
#                 print(n,"is not a prime number")
#             else:
#                 print(n,"is a prime number")
#             break
#     else:
#         print(n,'is a not a prime number')

# n = int(input("enter the number: "))
# prime_number_check(n)


# Q.10

# def even(w):
#     li = []
#     for j in e:
#         if j % 2 == 0:
#             li.append(j)
#     print(li)
# e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even(e)

# Q.11

# def perfect (v):
#     a = 0
#     for j in range(1,v):
#         if v % j == 0:
#             a += j
#     if a == v:
#         print(v,"is a perfect number")
#     else:
#         print(v,"is not a perfect number")

# p = int(input("enter your number: "))
# perfect(p)


# Q.12


# def palydrome(b):
#     rev = 0
#     g = b
#     while b > 0:
#         rev = (rev * 10)+(b % 10)
#         b = b // 10
#     if g == rev:
#         print("this is palydrome number")
#     else:
#         print("this not palydrome number")

# h = int(input("enter the number:  "))
# palydrome(h)


# def check (n):
#     i = n[::-1]
#     if n == i:
#         print("its palydrome number")
#     else:
#         print("its not a palydrome number")

# check(((input("enter the number: "))))


# Q.13

# def pascal(m):
#     for j in range(1,m+1):
#         for i in range(0,m-j+1):
#             print(" ",end=" ")
#         c = 1
#         for k in range(1,j+1):
#             print(" ",c,end=" ")
#             c = c * (j - k) // k
#         print()
# h = int(input("enter the number: "))
# pascal(h)


# Q.14

# def pangram(h):
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     for j in alpha:
#         if j in h.lower():
#             print("its pangram string")
#             break
#         else:
#             print("its not pangram")
#             break
# pangram("The quick brown fox jumps over  ")


# Q.14

# def hyphan(r):
#     b = r.split("-")
#     b.sort()
#     print("-".join(b))
# hyphan("green-red-yellow-black-white")


# Q.16

# def square():
#     b = []
#     for j in range(1,31):
#         b.append(j*j)
#     print(b)
# square()


# def square():
#     print([j*j for j in range(1,31)])
# square()

# Q.18

# my = 'print("hello world")'
# code = """
# def mutiply(x,y):
#     return x*y

# print('Multiply of 2 and 3 is: ',mutiply(2,3))
# """
# exec(my)
# exec(code)


# Q.19

# def test(a):
#         def add(b):
#             nonlocal a
#             a += 1
#             return a+b
#         return add
# func= test(4)
# print(func(4))


# Q.20



# def fun():
#     x = 2.3
#     y = 54
#     z = "susmit"
#     a = 25
# print(fun._code_.co_nlocals)


# Q.21

# from time import sleep
# import math
# def delay(fn, ms, *args):
#   sleep(ms / 1000)
#   return fn(*args)
# print("Square root after specific miliseconds:") 
# print(delay(lambda x: math.sqrt(x), 100, 16))
# print(delay(lambda x: math.sqrt(x), 1000, 100))
# print(delay(lambda x: math.sqrt(x), 2000, 25100))