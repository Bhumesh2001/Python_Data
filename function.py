# meraki question.....
# Q.1

# def ask_question (e):
#     print("Who is the founder of Facebook?")
#     print("""
#     1. Mark Zuckerberg
#     2. Bill Gates
#     3. Steve Jobs
#     4. Larry Page

#            """)
# ask_question(1)
# ask_question(2)
# ask_question(3)
# ask_question(4)
# ask_question(5)

# Q.2

# def ask(a):
#     print("Who is the founder of Facebook?")
#     print("""
#     1. Mark Zuckerberg
#     2. Bill Gates
#     3. Steve Jobs
#     4. Larry Page

#         """)
#     return a
# b  = 1
# while b <= 100:
#     print(ask(b))
#     b+=1

# pre difine function question
# Q.3

# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# print(max(numbers))

# Q.4

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# Q.4

# li = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# print(sorted(li))

# Q.5

# rt = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# print(rt[-1::-1])


# Q.6

# list = [8, 6, 4, 8, 4, 50, 2, 7]
# print(min(list))

# debug code
# Q.7

# def sum():
#     print(12+13)
# sum()


# Q.8

# def welcome():
#     print("Welcome to function")
# welcome()

# Q.9

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()

# Q.10

# def greet(names):
#     for name in names:
#         print("Welcome", name)
# name = "Rinki", "Vishal", "Kartik", "Bijender"
# greet(name)

# Q.11

# def info(name, age = 5 ):
#     print(str(name) + "  is  " + str(age) + "  years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# Q.12

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","bhumesh")


# Q.13

# def fun (a,b):
#     print(a)
#     print(b)
# b = "My name is Rishabh."
# h = 'I am the co-founder of NavGurukul'
# fun(b,h)

# Q.14

# a = []
# def st(name):
#     print()
# for j in range(1,11):
#     a.append(j)
# print(a)

# Q.15

# def is_greater (a,b = 20):
#     print(a)
#     print(b)
# a = 45
# is_greater(a)


# Q.16

# def add_numbers(num1,num2):
#     print(num1 + num2)
# num1 = 56
# num2 = 12
# add_numbers(num1,num2)


# Q.17

# def add ():
#     for j in range(len(a)):
#         bh = a[j] + b[j]
#         print(bh)
# a = [50,60,10]
# b = [10,20,13]
# add()

# Q.18

# def check_even(x,y):
#     if x % 2 == 0 and y % 2 == 0:
#         return 1
#     else:
#         return 0

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# t = check_even(a,b)
# if t == 1:
#     print("both are even")
# else:
#     print("both are not even")


# Q.19

# def check_numbers_list():
#     c = [2, 6, 18, 10, 3, 75]
#     d = [6, 19, 24, 12, 3, 87]
#     for j in range(len(c)):
#         if c[j] % 2 == 0 and d[j] % 2 == 0:
#             print("both are even")
#         else:
#             print("both are not even")

# check_numbers_list()


# Q.20

# def calculator(a,b):
#     num1 = a + b
#     num = a - b
#     num3 = a*b
#     num5 = a / b 
#     print(num5)
#     print(num3)
#     print(num)
#     print(num1)
# a = 45
# b = 78
# calculator(a,b)

# Q.21

# def calculator():
#     a = int(input("enter the number: "))
#     b = int(input("enter the second number: "))
#     print("add = ", a+b)
#     print("sub = ",a-b)
#     print("multiply = ",a*b)
#     print("divide = ",a/b)
# calculator()

# Q.22

# def calculator():
#     t =  []
#     h = [5, 10, 50, 20], [2, 20, 3, 5]
#     a,b = h
#     for j in range(len(a)):
#         m = a[j] * b[j]
#         t.append(m)
#     print(t)
# calculator()


# Q.23

# def eligible (t):
#     if g >= 18:
#         print("your are eligible for vote")
#     else:
#         print("your not eligible for vote")

# g = int(input("enter your age for vote: "))
# eligible(g)

# Q.25

# def perfect(n):
#     for i in range(1,n):
#         a = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 a += j
#         if i == a:
#             print(i)
# n = int(input("enter the number: "))
# perfect(n)

# Q.26

# def sum_average(w,x,y):
#     t = w + x + y
#     print("sum",t,"\naverage",t//3)
# a = int(input("enter first number: "))
# b = int(input("enter first number: "))
# c = int(input("enter first number: "))
# sum_average(a,b,c)

#Q.27

# def lable(u):
#     for j in range(u+1):
#         if j % 2 == 0:
#             print(j,"even")
#         else:
#             print(j,"odd")
# n = int(input("enter the number: "))
# lable(n)

# Q.28

# def multiple(g):
#     add = 0
#     for j in range(1,g+1):
#         if j % 3 == 0 :
#             print(j,end=' ')
#             add += j
#         else:
#             if j % 5 == 0:
#                 print(j,end=' ')
#                 add += j
#     print("sum",add)
# h = int(input("enter the number: "))
# multiple(h)

# Q.29

# def speed (h):
#     if h <= 70:
#         print("70")
#     elif h > 70:
#         count = 0
#         for j in  range(1,h):
#             if j % 5 == 0:
#                 count += j
#         print("your point is ",count)
#         if count > 12:
#             print("License suspended")
# m = int(input("enter your speed: "))
# speed(m)

# Q.30

# def large(a,b):
#     if len(a) == len(b):
#         print(a)
#         print(b)
#     elif len(a) > 4 :
#         print(a)
#     elif len(b) > 4:
#         print(b)
# n = input("enter the  your charecter: ")
# v = input("enter the  your charecter: ")
# large(n,v)

# Q.31

# def dict1(r):
#     d = {}
#     for j in range(1,r+1):
#         d[j] = j*j
#     print(d)
# n = int(input("enter your range:  "))
# dict1(n)


# def dict1(r):
#     print({i:i*i for i in range(1,r+1)})
# n = int(input("enter your range:  "))
# dict1(n)


# Q.32

# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")


# Q.33

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#             print(i,"times",num//i,"is",num)
#             break
#         else:
#             print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot()


# Q 34

# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# Q.35

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# print(sumofdigits(123))


# Q.36

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

# Q.37.

# def checkKey():
#     car ={"brand": "ford","model": "mustang","year": 1964}
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")
# checkKey()

# Q.38

# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)

# Q.39

# def functionmulti(a,b):
#     multiply=a*b
#     return multiply
# print(functionmulti(3,4))

# Q.40

# def Avg(number1,number2,number3):
#     sum=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)

# Q.41

# def voter(age):
#     if age > 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)

# Q.42

# def distance(kms,bh):
#     if kms < 20:
#         print("close")
#     elif bh < 50:
#         print("midian")
#     else:
#         print("far")
# distance(20,30)


# fibonacies siries.


# def fibo(m):
#     x = 0
#     y = 1
#     z = 0
#     while z <= m:
#         print(z)
#         x = y
#         y = z
#         z = x + y
# n = int(input("enter the number: "))
# fibo(n)


# interviw question

# Q.1  What is the difference between a parameter and an argument?

# ans :- A parameter is the variable listed inside the parentheses in the function definition.
#  An argument is the value that are sent to the function when it is called.

# Q.2

# 2- All functions in Python by default return …?

# ans:- no.

#.Q 3

# What are keyword arguments and when should we use them?

# ans :- Keyword arguments can often be used to make function calls more explicit. 
# This takes a file object output_file and contents string and 
# writes a gzipped version of the string to the output file. Notice that using this
# keyword argument call style made it more obvious what each of these three arguments represent.

# Q.4

# How can we make a parameter of a function optional?

# ans :-    Use the *args parameter to make optional arguments
# Include the *args parameter at the end of a function declaration 
#  allow the user to pass in an arbitrary number of arguments as a tuple.

# Q.5

# What happens when we prefix a parameter with an asterisk (*)?

# ans:- The asterisk (star) operator is used in Python with more than one meaning attached to it. 
# Single asterisk as used in function declaration allows variable number of arguments passed from calling environment. 
# Inside the function it behaves as a tuple.

# Q 6.

# What about two asterisks (**)?

# ans:- Python3. In a function definition, the double asterisk is also known **kwargs. 
# They used to pass a keyword, variable-length argument dictionary to a function. 
# The two asterisks (**) are the important element here, 
# as the word kwargs is conventionally used, though not enforced by the language.

# Q.7

# What is the scope?

# ans:- The scope of a variable refers to the context 
# in which that variable is visible/accessible to the Python interpreter.

# Q.8

# What is the difference between local and global variables?

# ans:- The main difference between Global and local variables 
# is that global variables can be accessed globally in the entire program, 
# whereas local variables can be accessed only within the function or block in which they are defined.

# Q.9

# Why is using the global statement a bad practice?

# ans:- Using globals in any language is bad practice. 
# In a nutshell - a global can be legally changed from anywhere (that after all is the point). 
# That means it makes it difficult in any reasonably complex program 
# to keep track of what values are in that global at any time.