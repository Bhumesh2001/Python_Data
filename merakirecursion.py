
# Q.1

# def pattern(b,h):
#     if b == 0:
#         return 
#     print(h,end=" ")
#     pattern(b-1,h+3)
# n = int(input("enter the number: "))
# pattern(n,1)

# Q.2

# def pattern(b,h):
#     if b == 0:
#         return 10
#     elif b % 2 == 0:
#         print(h,end=" ")
#         pattern(b-1,h+1)
#     else:
#         print(h,end=" ")
#         pattern(b-1,h*10)
# n = int(input("enter the number: "))
# (pattern(n,10))


# Q.3

# factorial of given number

# def factorial(number):
#     if number==1:
#         return 1
#     else:
#         return number * factorial(number - 1)
# n = int(input("enter the number: "))
# print(factorial(n))

# Q.4

# sum of list using recursion

# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])

# print (sum_list([1, 4, 7, 10]))

# Q.5

# def ifPalindrome(string):
#     if string == "": 
#         return True
#     elif len(string) == 1: 
#         return True
#     elif string[0] == string[len(string)-1]: 
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False
# g = input("enter the number:")
# print(ifPalindrome(g))


# Q.6

# def fibo(f):
#     if f == 1:
#         return 0
#     elif f == 2:
#         return 1
#     return fibo(f-1)+fibo(f-2)

# n=int(input("enter your range: "))
# for j in range(1,n+1):
#     print(fibo(j))


# Q.7


# def fib(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)

# def getFibList(number):
#     fib_list = []
#     key = 1
#     while (key <= number + 1):
#         fib_list.append(fib(key))
#         key += 1
#     return fib_list

# print(getFibList(10))

# Q.8


# def binarysearch(a,size,key):
#     flag = 0
#     i = 0
#     j = size-1
#     while i <= j and flag == 0:
#         mid = i + j // 2
#         if a[mid] == key:
#             flag = 1
#             pos = mid+1
#         elif a[mid] < key:
#             i = mid + 1
#         elif a[mid] > key:
#             j = mid - 1
#     if flag == 1:
#         print("number found at",pos,"position")
#     else:
#         print("number not found")
# a = []
# size = int(input("enter the size of the list: "))
# for i in range(size):
#     val = int(input("enter the value for the list in ascending order: "))
#     a.append(val)
# print(sorted(a))
# key = int(input("enter number to search: "))
# binarysearch(a,size,key)


# Q.8

# binary search using recursion 

# def binaryrecursion(a,key,low,high):
#     if low > high:
#         return -999
#     mid = low + high // 2
#     if  a[mid] == key:
#         return mid
#     elif key > a[mid]:
#         binaryrecursion(a,key,low,mid-1)
#     elif key < a[mid]:
#         binaryrecursion(a,key,mid+1,high)
# a = [2,3,4,5,6,7,8,9,10]
# print(sorted(a))
# key = int(input("enter number to search: "))
# x = binaryrecursion(a,key,0,len(a)-1)
# if x == -999:
#     print("number not found")
# else:
#     print("number found at",x,"position")


# Q.9

# def operate(num1, operator, num2):
#     if operator=='+':
#         return num1 + num2
#     elif operator=='-':
#         return num1 - num2
#     elif operator=='*':
#         return num1 * num2
#     else:
#         return num1 / num2
# print(operate(8,"+",8))


# def operate(num1, operator, num2):
#     if operator=='+':
#         return num1 + num2
#     elif operator=='-':
#         return num1 - num2
#     elif operator=='*':
#         return num1 * num2
#     else:
#         return num1 / num2
# def solve(q):
#     if len(q)==1:
#         return int(q[0])
#     elif len(q)==3:
#         return operate(int(q[0]), q[1], int(q[2]))
#     else:
#         return operate(solve(q[:-2]), q[-2], int(q[-1])) 

# print(solve(['3',  '+', '5', '-', '2', '', '4', '/', '2', '+', '8', '-', '10', '', '9', '/', '3']))