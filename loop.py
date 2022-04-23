# loop question.
# Q.0.
# a = 1
# while a <= 100 :
#     print(a)
#     a += 1


# Q.1. 1 to 100 sum ,inpput leke.
# n = int(input("enter the number upto which you want to sum:  "))
# a = 1
# b = 0
# while a <= n :
#     b += a
#     a += 1
# print("your sum is=",b)


# Q.2.
# a = 1
# while a <= 100 :
#     if a % 7 == 0 :
#         print (a)
#     a += 1


# Q.3.10 numbers input leke sum.
# a = 1
# sum = 0
# while a <= 10 :
#     n = int(input("enter any number: "))
#     sum += n
#     a += 1
# print("your sum is =",sum)


# Q.4.odd even.
# a = 1
# while a <= 100 :
#     if a % 2 == 0 :
#         print(-a)
#     else :
#         print(a)
#     a += 1


#counter question .
# Q.1
# a = 556
# while a <= 656 :
#     x = a - 555
#     if x % 7 == 0 :
#         print(x)
#     a += 1

# print 3 and 7 se divisible so print navgurukul and nav and gurukul.
# Q.2.
# a = 1
# while a <= 100 :
#     if a % 3 == 0 and a % 7 == 0:
#         print("navgurukul")
#     elif a % 3 == 0 :
#         print("nav")
#     elif a % 7 == 0 :
#         print("gurukul")
#     else :
#         print(a)
#     a += 1


# 11 to 101 numbers print.
# Q.3.
# a = 156
# while a <= 246 :
#     print(a-145)
#     a += 1


# prime number input leke .
# Q.4.
# c = int(input("enter the number: "))
# n = 1
# while n <= c :
#     a = 0 
#     b = 1
#     while b <= n :
#         if n % b == 0 :
#             a += 1
#         b += 1
#     if a == 2 :
#         print(n) 
#     n += 1


# pattern print.
# Q.5.
# a = 5
# while a >= 1 :
#     print(str(a)*5)
#     a -= 1

# 
    
    
#  questions of break and continue statement.
# Q.1. 2 se divisible numbers print.
# a = 20
# while a <= 100 :
#     if a % 2 == 0 :
#         print(a)
#     a += 1


# Q.2. 7 se divisible number print frome 20 to 100 .
# a = 20
# while a <= 100 :
#     if a % 7 == 0 :
#         print(a)
#     a += 1


# Q.3. sum calculation only input leke.
# n = int(input("enter the number : "))
# a = 12
# b = 0
# while a <= n :
#     b += a
#     a += 1
# print("your total sum is = ",b)


# Q.4. sum calculate  input leke  with numbering show.
# n = int(input("enter the number upto which you want to sum: "))
# a = 30
# b = 0
# while a <= n :
#     if a % 8 == 0 :
#         print(a+b)
#         b += a 
#     a += 1
# print("your sum is =",b)


# Q.5 find the weight a average.
# a = 1
# b = 0
# while a <= 11 :
#     print("enter",a,"persion weight")
#     n = int(input())
#     b += n
#     a += 1
#     c = b / 11
# print("your weight average is",c)
# if c % 5 == 0 :
#     print("average divided by 5")
# else :
#     print("average not divided by 5")


# q.6 odd even number print.
# a = 1
# while a <= 100 :
#     if a % 2 == 0 :
#       print(-a,end=" ")
#     else :
#       print(a,end=" ") 
#     a += 1

# q.7 guessing game
# print("welcome to guessing game")
# a = 1
# while a <= 10 :
#     b = int(input('enter any number : '))
#     if b == 3 :
#         print("congratulation, you win ! your guess is correct")
#         break
#     elif b == 6 :
#         print("congratulation, you win ! your guess is correct")
#         break
#     elif b == 9 :
#         print("congratulation, you win ! your guess is correct")
#         break
#     print(f"sorry, your guess is wrong, you have 10 chances,your reamaing chance is {10-a}")
#     a += 1    


# q.8 second guessing game
# print("welcome to guessing game ")
# a = 1
# while a <= 10 :
#     b = int(input("enter any number : "))
#     if b == 5 :
#         print("wow , its guessed !you win ")
#         break
#     elif b > 5 :
#         print(f"your enter number is greater, so please try one more time,")
#         continue
#     elif b < 5:
#         print(f"your enter number is small, so please try one more time") 
#         continue
#     a += 1


# q.9 bina multiply ka multiply .
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# c = 1
# e = 0
# while c <= b :
#     e += a
#     c += 1
# print(e)


# Q.10. fibonacci series .
# n = int(input("enter the number: "))
# x = 0
# y = 1
# z = 0
# while z <= n :
#     print(z)
#     x = y
#     y = z
#     z = x + y


# prime numbers input leke.
# c = int(input("enter the number: "))
# n = 1
# while n <= c :
#     a = 0 
#     b = 1
#     while b <= n :
#         if n % b == 0 :
#             a += 1
#         b += 1
#     if a == 2 :
#         print(n) 
#     n += 1


# code output quetions.
# Q. 1
# c = 0
# d = 1
# while c < 3:
#     c = c + 1
#     d = d * c
#     print("Loop Ke Andar", c, d)
# else:
#     print("Loop Ke Bahar", c, d)

# Q . 2 add .
# n = 6
# s = 0
# i = 1
# while i <= n:
#     s = s + i
#     i = i + 1
#     print(s)

# Q 3 prime number input leke .
# c = int(input("enter the number: "))
# n = 1
# while n <= c :
#     a = 0 
#     b = 1
#     while b <= n :
#         if n % b == 0 :
#             a += 1
#         b += 1
#     if a == 2 :
#         print(n) 
#     n += 1


# Q .4 star print
# i = 0 
# while i < 5 :
#     j = 0
#     while j < 5 :
#         if j > 3 :
#             break
#         else :
#             print("*")
#         j += 1
#     print()
#     i += 1  

# Q . 5 numbers print.
# x = 0
# while (x < 7) :
#     if (x == 3 or x == 5 ) :
#         x += 1
#         continue
#     print(x)
#     x += 1


# debug code example solved.
# Q . 1 .
# in this code was inditation error and bugs, i solved.
# index = 1
# while(index <= 10):
#     print(index)
#     index += 1


# Q 2. debug code line number 2,3 .
# n = int(input("enter the number: "))
# i = 1
# while(i <= n):
#     if(i % 3 == 0):
#         print(i)
#     i += 1


# Q.3  heare indantations errors solved .
# i=0
# while(i<10):
#     j = 0
#     while(j<=5):
#         print(j)
#         j = j + 1
#     print()
#     i = i + 1


# Q.4  heare increasing statement bugs solved.
# i = 0
# num = int(input("Enter your number:- "))
# while(i <= num):
#     if(num > 0):
#         print("its positve number")
#     i = i + 1


# greatest common divisor(gcd) or highest common factor(hcf.)
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# j = 1
# while j <= a and j <= b :
#     if a % j == 0 and b % j == 0 :
#         gcd = j
#     j += 1
# print("your gcd is",gcd)


# sum of digit of each number.
# n = int(input("enter the number: "))
# sum = 0
# while n > 0 :
#     sum = sum + n % 10 
#     n = n // 10
# print("your sum of digit of each number=",sum)


# sum of square of  each digit
# n = int(input("enter the number: "))
# sum = 0
# while n > 0 :
#     sum = sum + (n % 10) * (n % 10)
#     n = n // 10
# print("sum of square of each digit is=",sum)


# product of each digit.
# n = int(input("enter the number: "))
# sum = 1
# while n > 0 :
#     sum = sum * (n % 10)
#     n = n // 10
# print("sum of product of each digit is =",sum)


# product of odd numbers and sum of even numbers.
# n = int(input("enter the numbers: "))
# sum = 0
# prod = 1
# while n > 0 : 
#     d = n % 10
#     if d % 2 == 0 :
#         sum = sum + d
#     else :
#         prod = prod * d
#     n = n // 10
# print("the sum of even digit is =",sum,"the product of odd digit is =",prod)


# reverse number.
# n = int(input("enter the number: "))
# sum = 0
# while n > 0 :
#     sum = (sum * 10) + (n % 10)
#     n = n // 10 
# print("reverse numbers is",sum)


#  check the happy numbers .
# sum = 0
# n = int(input("enter the number: "))
# while (sum != 1 and sum != 4):
#     sum = 0
#     while n > 0 :
#         sum = sum + (n % 10)*(n % 10)
#         n = n // 10
#     n = sum
# if sum == 1 :
#     print("its happy number")
# else :
#     print("its unhappy number")


# c = int(input("enter the number: "))
# n = 1
# while n <= c :
#     a = 0 
#     b = 1
#     while b <= n :
#         if n % b == 0 :
#             a += 1
#         b += 1
#     if a == 2 :
#         print(n) 
#     n += 1


# a = "satish"
# print(a)
# n = (input("enter the charecter: "))
# if n == "a":
#     d = a[1:]
#     print(d)