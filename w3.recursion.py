# w3.recursion question

# Q.1

# def list_sum(num_List):
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
# print(list_sum([2, 4, 5, 6, 7]))

# Q.2

# def to_string(n,base):
#    conver_tString = "0123456789ABCDEF"
#    if n < base:
#       return conver_tString[n]
#    else:
#       return to_string(n//base,base) + conver_tString[n % base]

# print(to_string(2835,16))

# Q.3

# sum of nested list list using recursion.

# def recursive_list_sum(data_list):
# 	total = 0
# 	for element in data_list:
# 		if type(element) == type([]):
# 			total = total + recursive_list_sum(element)
# 		else:
# 			total = total + element
# 	return total
# print( recursive_list_sum([1, 2, [3,4],[5,6]]))

# Q.4

# factoorial of a given number.

# def factorial(n):
#   if n <= 1:
#     return 1
#   else:
#     return n * (factorial(n - 1))
# n = int(input("enter the number: "))
# print(factorial(n))

# Q.5

# fibonacci series using recursion

# def fibo(f):
#     if f == 1:
#         return 0
#     elif f == 2:
#         return 1
#     return fibo(f-1)+fibo(f-2)
# n=int(input("enter your range: "))
# for j in range(1,n+1):
#     print(fibo(j))

# Q.6

# sum of non negative integer.
# sum of digits using recursion

# def sumDigits(n):
#   if n == 0:
#     return 0
#   else:
#     return n % 10 + sumDigits(int(n / 10))
# print(sumDigits(345))
# print(sumDigits(45))

# Q.7

# sum of positive integer

# def sum_series(n):
#   if n < 1:
#     return 0
#   else:
#     return n + sum_series(n - 2)

# print(sum_series(6))
# print(sum_series(10))

# Q.8

# def harmonic_sum(n):
#   if n < 2:
#     return 1
#   else:
#     return 1 / n + (harmonic_sum(n - 1))

# print(harmonic_sum(7))
# print(harmonic_sum(4))

# Q.9

# def geometric_sum(n):
#   if n < 0:
#     return 0
#   else:
#     return 1 / (pow(2, n)) + geometric_sum(n - 1)
 
# print(geometric_sum(7))
# print(geometric_sum(4))

# Q. 10

# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x*power(x,y-1)

# a = int(input("enter the base: "))
# b = int(input("enter exponant: "))
# h = power(a,b)
# print(a,"to the power",b,"is = ",h)

# Q.11

# def gcd(p,q):
#     if q == 0:
#         return p
#     else:
#         return (gcd(q,p%q))

# p = int(input("enter the first number: "))
# q = int(input("enter the first number: "))
# print("your gcd is = ",gcd(p,q))


# # happy numbers using recursion

# def happy(num):
#     if num < 10:
#         if num == 1:
#             print(n," is happy number")
#         else:
#             print(n," is not happy number")
#     else:
#         return sum_sq_digits(num,0)

# def sum_sq_digits(x,s):
#     if x > 0:
#         t = x % 10
#         s = s + t ** 2
#         x = x // 10
#         return sum_sq_digits(x,s)
#     else:
#         return happy(s)
# n = int(input("enter any number: "))
# sum_sq_digits(n,0)

