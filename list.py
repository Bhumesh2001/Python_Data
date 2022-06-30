three type to write the append functions.
pattern  print palidrome.
for x in range(1,5):
    for y in range(4,x,-1):
        print(" ",end="")
    for z in range(x-1,-x,-1):
        print(x-abs(z),end="")
    print()

a = []
for i in range(5):
    x = int(input("enter the number: "))
    a.append(x)
for i in a :
    print(a[i])


a = []
for i in range(5):
    x = int(input("enter the number: "))
    a.append(x)
for i in a :
    print(i)
    
    
a = []
for i in range(5):
    x = int(input("enter the number: "))
    a.append(x)
print(a)


a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
a.sort(reverse=False)
print("asending order after sort ",a)


a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
a.sort()
print("after sort is list is ",a)



a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
a.sort(reverse=True)
print("descending order after sort = ",a)


a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
print(min(a))


a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
print(max(a))


a = []
for i in range(5):
    b = int(input("enter the number: "))
    a.append(b)
print("original list is =",a)
print(len(a)

a = ["bhumesh","rahul","akash","aniket"]
print(a)
a.pop()
print(a)


names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
names_list[0] = "abhishek"
print(names_list)

names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
print(names_list)
names_list.pop()
print("length of the list is ", len(names_list))
print(names_list)


names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
print("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print("lenth of the list is = ",len(names_list),names_list)

names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
print("bhumesh" in names_list)


students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
list_length = len(students_list)
index = 0
while index < list_length:
    print(students_list[index])
    index = index + 1
    
    
student_marks = [23, 45, 89, 90, 56, 80] 
length = len(student_marks)
index = 0
total_marks = 0
while index < len(student_marks):
    total_marks = student_marks[index] + total_marks
    index = index + 1
print("Total Marks: " + str(total_marks))


student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
list_length = len(student_marks)
index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
    marks = student_marks[index]
    if marks < 50:
        less_than50 = less_than50 + 1
    else:
        more_than50 = more_than50 + 1
    index = index + 1
print("Marks more than 50: " + str(more_than50))
print("Marks less than 50: " + str(less_than50))
print(less_than50 + more_than50)

mearaki question.
question set 1.
Q.1 element count.
a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
print(len(a))


count = 0
a =[50, 40, 23, 70, 56, 12, 5, 10, 7]
for i in a :
    count += 1
print(count)

string se lenth.
count = 0
a =[50, 40, 23, 70, 56, 12, 5, 10, 7]
while a[count:]:
    count += 1
print(count)

Q.2
count = 0
a =[50,40,45,23,34,34,56,23, 12, 5, 10, 7]
for i in a :
    if i > 20 and i < 40 :
        count += 1
print(count)

Q.3
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
print(max(a))

a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
print(a[3])


sabde bada number in list.
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
greate = a[0]
for i in a :
    if i >  greate :
        greate = i
print(greate)


sabse chota number in list.
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
small = a[0]
for i in a :
    if i < small :
        small = i
print(small)

sort method se chota bada number nikalna in list.
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort()
print("your greater number is = ",a[-1])


a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort(reverse=True)
print("your greater number is = ",a[0])


Q.4. second max in list.
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort()
print("second max is = ",a[-2])


a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort(reverse=True)
print("second max is = ",a[1])


second min in  list.
a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort(reverse=True)
print("second min is = ",a[-2])



a  = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a.sort()
print("second min is = ",a[1])


Q.5 reverse list.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
places.reverse()
print(places)

bina reverse function use kare reverse.
a = ["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
for i in range(-1,-(len(a)+1),-1):
    print(a[i])


Q.6
check its palidrome list or not.
a = []
b = a
g = int(input("enter the number: "))
for i in range(g):
    x = input("enter the list which you want = ")
    a.append(x)
print(a)
c = (a[-1::-1])
print(c)
if c == b :
    print("its palidrome list")
else :
    print("its not palidrome list")


Q.7
binary to decimal in list.
a = []
b = int(input("how many long want to enter your list = "))
for i in range(b):
    x = input("enter the binary number: ")
    a.append(x)
a.reverse()
add = 0
for j in range(len(a)):
    add = 2 ** j * int(a[j]) + add
print("your decimal number is = ",add)



decimal to binaryin list.
n = int(input("enter the decimal number: "))
a =[]
while n != 0 :
    b = n % 2
    a.append(b)
    n = n // 2
a.reverse()
print("your binary number is = ",a)



binary to cecimal without list.
n = input("enter binary number: ")
b = n[-1::-1]
sum = 0
for i in range(len(b)):
    sum = 2 ** i * int(b[i]) + sum 
print(sum)

questoin set 2.
Q.1
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
for i in list1 :
    if i not in list2:
        print(i)

Q.2.
sum of list.
a = [2,3,4,5,6,7]
sum = 0
for i in a :
    sum += i
print(sum)


without index.
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
sum = 0
for i in marks :
    for j in i :
        sum += j
print("marks of three year = ",sum)


with index.
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
sum = 0
for i in range(len(marks)) :
    for j in (marks[i]):
        sum += j
print("marks of three year = ",sum)


marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
add = 0
for i in marks:
    for j in range(len(i)):
        add += i[j]
print("your three year marks is = ",add)


marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
add = 0
for i in marks:
    for j in range(len(i)):
        add += i[j]
print("your three year marks is = ",add)


sum of nested list.
a=[1,2,3,[4,5,6,7],8,9,[10,11,12,13]]
add = 0
sum = 0
for i in a:
    if type(i) is list:
        for j in i :
            add += j
    else:
        sum += i
print("your nested list of sum is = ",sum+add) 



        
Q.3
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
add = 0
count = 0
for i in marks:
    count += 1
    for j in i:
        add += j
    print("average",count,"year",add//5)
    add = 0
    


with index.
marks = [[78, 76, 94, 86, 88, 56],[91, 71, 98, 65],[95, 45, 78, 52, 49, 34, 78 ]]    
add = 0
for i in marks:
    for j in range(len(i)):
        add += i[j]
    print("average",add//len(i))
    add = 0


marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
add = 0
count = 0
for i in marks:
    count += 1
    for j in range(len(i)):
        add += i[j]
    print("average",count,"year",add//len(i))
    add = 0


marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
add = 0
count = 0
for i in marks:
    count += 1
    for j in range(len(i)):
        add += i[j]
    print("average",count,"year",add//len(i))
    add = 0


Q.4 
total sum.
n = 30
b=[]
a = [10,11,14,16,19,24,12,18]
for i in a:
    for y in a:
        if i+y==n:
            b.append([i,y])
            a.remove(i)
print(b)


Q.5 magik square.
a = []
for i in range(3):
    b = []
    for j in range(3):
        j = int(input("enter the number:  "))
        b.append(j)
    a.append(b)
print("matrix is......")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sumd1 = 0
sumd2 = 0
for i in range(3):
    for j in range(3):
        if i == j:
            sumd1 = sumd1 + a[i][j]
        if i + j == 3 - 1:
            sumd2 = sumd2  + a[i][j]
if sumd1 != sumd2:
    f = 1
else:
    for i in range(3):
        sumr = 0
        sumc = 0
        for j in range(3):
            sumr = sumr + a[i][j]
            sumc = sumc + a[i][j]
        if sumr != sumd1:
            f = 1
        elif sumc != sumd1:
            f = 1
        else:
            f = 0
if f == 0:
    print("its magic square")
else:
    print("its not magic square")



m = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
add = 0
count = 0
for i in m:
    count += 1
    for j in i:
        add += j
    print("row of sum",count,"=",add)
    add = 0
    
Q.6.  iterate otwo lists together.
with range.
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
for i in range(len(students)):
        print(students[i],marks[i])  
        

with zip function.
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
for b,c in zip(students,marks):
    print(b,c)
        
        
use of sum function.
marks = [10, 20, 56, 45, 36, 20]
print(sum(marks))

Q.7
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even = 0
odd = 0
for i in elements:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("even number is = ",even,"odd number is = ",odd)


Q.8
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even = 0
odd = 0
for i in elements:
    if i % 2 == 0:
        even += i
    else:
        odd += i     
print(" sum of even number is = ",even," sum of odd number is = ",odd)


Q.9
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even = 0
odd = 0
count = 0
count1 = 0
for i in elements:
    if i % 2 == 0:
        count += 1
        even += i
    else:
        count1 += 1
        odd += i     
print(" average of even number is = ",even/count," average of odd number is = ",odd/count1)



Q.10
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even = 0
odd = 0
even1 = 0
odd1 = 0
count1 = 0
count2 = 0
count3 = 0
sum = 0
for i in elements:
    sum += i
    count3 += 1
    if i % 2 == 0:
        count1 += 1
        even += i
        even1 += 1
    else:
        count2 += 1
        odd += i
        odd1 += 1
print("all number =",count3)
print("even numbers =",count1,"odd number =",count2)       
print("sum of even number = ",even,"sum of odd number",odd)
print("sum of all the number = ",sum)
print(" average of even number is = ",even/even1," average of odd number is = ",odd/odd1)
print("average of all number = ",sum/count3)



questions set 2.
Q.1
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
crore = 0
lakh  = 0
dil = 0
for i in kitna_paisa_hai:
    if i >= 10000000:
        crore += 1
    elif i >= 100000:
        lakh += 1
    else:
        dil += 1
print("people of crorepati=",crore,"people of lakhpati=",lakh,"people of dilwale=",dil)

    
        
Q.2 occurence.
a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
b = []
for a1 in (a):
    if a1 not in b:
        b.append(a1)
for a2 in (b):
    print([a2,a.count(a2)],end=" ")


Q.3 dubliucates
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a = []
for i in n:
    if i not in a:
        a.append(i)
print(a)


Q.substring remove'.
m = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b = m.replace("over", "")
print(b)


m = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b = m.replace("over","on")
print(b)


Q.kbc, kon banega crorepati/ kya banega re crorepati.

import random
a = ["How many continents in the world?",
    "What is the capital of India?",
    "NG mei kaun se course padhaya jaata hai?",
    "who is author of the meghdoot?",
    "pongal is a popular festival of which state?",
    "which one of the following is essentially a solo dance?",
    "which of the following is a folk dance of india?",
    "who is the president of russia?",
    "which of the folllowing year was celebrated as the world communication year?",
    "which of following newspaper is 150 years old?",
    "The conark temple is dedicated to?","Van mahotsav was stated by?"]

b = [["1.Four", "2.Nine", "3.Seven", "4.Eight","5.life line"],
     ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.New Delhi","5.life line"],
     ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture","5.life line"],
     ["1.Vishakhadatta","2.Vlmiki","3.Banabatta","4.kalidas","5.life line"],
     ["1.karnataka","2.kerla","3.tamil nadu","4.Andhra pradesh","5.life line"],
     ["1.kuchipudi","2.kathak","3.mohiniattam","4.manipuri","5.life line"],
     ["1.kathkali","2.mohiniattam","3.garba","4.manipuri","5.life line"],
     ["1.joe biden","2.narendre modi","3.boris jhonson","4.vladimir putin","5.life line"],
     ["1.1981","2.1983","3.1985","4.1987","5.life line"],
     ["1.the statesjman","2.the times of india","3.the hindu","4.malayala manorma","5.life line"],
     ["1.vishnu","2.shiva","3.krishna","4.sun-god"],
     ["1.maharshi karve","2.bal gangadhar tilak","3.k m munshi","4.sanjay gandhi"]]

c = [3,4,1,4,3,3,3,1,2,2,4,3]
life line.
t = ['1).50:50','2).Phone-a-Friend','3).Audience Poll','4).Switch the Question','5)gochi']
50:50 ke liye option
w = [["3.seven","4.eight"],["2.bhopal","4.new delhi"],["1.software engineering","2.counceling"],
     ["1.Vishakhadatta","4.kalidas"],["2.kerla","3.taml nadu"],["1.kuchiipudi","3.mohiniattam"],
     ["3.garba","2.manipuri"],["1.joe biden","2.narendra modi"],["1.1981","2.1983"],
     ["2.the times of india","3.the hindu"],["2.shiva","4.sun god"]]
d = 100
ab = 0
ac = 0
ad = 0
ae = 0
af = 0
s = 0
h = 1
while h > 0:
    a1 = random.randint(1,101)
    a2 = random.randint(1,101)
    a3 = random.randint(1,101)
    a4 = random.randint(1,101)
    if a1 + a2 + a3 + a4 == 100:
        break
    else:
        h += 1
k = [0,1,2,3,4,5,6,7,8,9,10]      
for i in range(len(a)):
    print()
    print('\033[1m','This Question for',d,'rupees amount.','\033[0m')
    print()
    h = random.choice(k)
    k.remove(h)
    if i == 10:
        break
    print('\033[1m','\033[91m','Q.',str(i+1) ,a[h],'\033[0m')
    print()
    for j in b[h]:
        print('\033[35m',j,'\033[0m')
    print()
    n = int(input("enter your answer: "))
    print()
    if n == 5:
        if ab == 1:
            print('\033[33m','allready use 50:50','\33[0m')
        if ac == 1:
            print('\033[33m','allready used phone a friends','\033[0m')
        if ad == 1:
            print('\033[33m','allready used audience poll','\033[0m')
        if ae == 1:
            print('\033[33m','allready used switch the question','\033[0m')
        if af == 1:
            print('\033[33m','allready used gochi','\033[0m')
        for j in t:
            print('\033[32m',j,'\033[0m')
        print()
        l = int(input("choose your option: "))
        50:50 
        if l == 1 and ab < 1:
            print('\033[32m','choose correct answer','\033[0m')
            print()
            for e in w[h]:
                print('\033[96m',e,'\033[0m')
            print()
            ab += 1
            t.remove("1).50:50")
            q = int(input(" enter your answer: "))
            n = q
        elif l == 2 and ac < 1:
            print('\033[33m','correct answear is....','\033[0m')
            print('\033[34m',c[h],'\033[0m')
            ac += 1
            t.remove('2).Phone-a-Friend')
            v = int(input("enter your answer:  "))
            n = v
        elif l == 3 and ad < 1:
            print()
            if a1 + a2 + a3 + a4 == 100:
                print('\033[34m','1.Audience',a1,'% ','\033[0m')
                print('\033[34m','2.Audience',a2,'% ','\033[0m')
                print('\033[34m','3.Audience',a3,'% ','\033[0m')
                print('\033[34m','4.Audience',a4,'% ','\033[0m')
            print()
            ad += 1
            t.remove('3).Audience Poll')
            z = int(input('enter your answer: '))
            n = z     
        elif l == 4 and ae < 1:
            h = 11
            print('\033[31m',"Q.",str(i+1),a[h],'\033[0m')
            print()   
            for j in b[h]:
                print('\033[34m',j,'\033[0m')
            print()
            n = int(input("enter your answer: "))
            print()
            ae += 1
            t.remove('4).Switch the Question')
        s += 1
        if c[h] == n:
            d += d * 2
            print('\033[31m','you win amount',d,'rs.','\033[0m')
        print()
    if c[h]== n:
       print('\033[33m','congratulation,you win.','\033[0m')
       d += d * 2
       print()
       print('\033[32m','you win',d,'rs.','\033[0m')
       continue
    else:
        print('\033[32m','your answer is wrong \n you loss','\033[0m')
    print('\033[31m','do you want play continue y or n','\033[0m')
    print()
    m = input("enter your choice: ")
    if m == "y":
        i = 0
        continue
    else:
        break
print("your total amount is ",d,"rupees")


guessing game.

import random
print("\033[33m","\033[1m","Welcome to guessing game","\033[0m")
for i in range(1,8):
    v = random.randrange(1,12)
    n = int(input("enter your guess number: "))
    print()
    if n == v:
        print("\033[35m","\033[1m","congratulation,you win.\n your guess is right","\033[0m")
        break
    elif v >= n:
        print("\033[32m","your guess number is greater ","\033[0m")
        if i + 1 == 7:
            print("\033[35m","this is your last chance","\033[0m")
            print()
            h = int(input("enter the guess number: "))
            if h == v:
                print("\033[32m","you win","\033[0m")
                break
            else:
                print("\033[33m","\033[3m","you loss","\033[0m")
                break
        else:
            print("\033[31m",i + 1,"chance,try again","\033[0m")
            print()
    elif v <= n:
        if i + 1 == 7:
            print("\033[35m","this is your last chance","\033[0m")
            print()
            g = int(input("enter the guess number: "))
            if g == v:
                print("\033[34m","\033[1m","congratulation,you win","\033[0m")
                break
            else:
                print("\033[31m","\033[3m"," you loss","\033[0m")
                break
        elif i + 1 == 8:
            print("\033[32m","game over \n you loss the game","\033[0m")
            print()
        else:
            print("\033[36m",i + 1,"chance,try again","\033[0m")
         
         
rock, paper, scissor.

import random
print("Welcome to \n rock, paper,scissors game")
print()
h = ["rock","paper","scissors"]
for j in range(1,21):
    c = random.randrange(0,3)
    print("press 0 for rock")
    print("press 1 for paper")
    print("press 2 for scissors")
    print()
    b = int(input("enter your choice: "))
    if b == c:
        print("match draw")
        print()
    elif (b==0 and c==1)or(b==1 and c==2)or(b==2 and c==0):
        print(h[c],"means,computer win")
        print()
        print("you loss\n try again...")
        print()
    elif (b==0 and c==2)or(b==1 and c==0)or(b==2 and c==1):
        print(h[c])
        print()
        print("congratulation,you win")
        print()
        break
    else:
        print()
        print("please, enter correct number")
        print()
        j = 0
        continue
    


packing tupule.
a = ("apple",45.3,45,3+5j)

unpacking tupule.
a = ("apple",45.3,45,3+5j)
(c,v,l,j) = a
print(a)
 

sorting, buble sort.
n = int(input("enter the size of the list: "))
b = []
for i in range(n):
    c = int(input("ente the number: "))
    b.append(c)
print(b)
for i in range(n):
    for j in range(0,n-1-1):
        if b[j] > b[j+1]:
            t = b[j]
            b[j] = b[j+1]
            b[j+1] = t
print("sorted list is = ",b)



insertion sort .
a = int(input("enter size of the list: "))
b = []
for i in range(a):
    c = int(input("enter the number: "))
    b.append(c)
print(b)
for i in range(1,a):
    t = b[i]
    j = i - 1
    while j >= 0 and t < b[j]:
        b [j + 1] = b [j]
        j = j - 1
    b [j + 1] = t
print("sorted list is = ",b)
 
 
Debugging question.
Q.1
marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + (marks[counter])
    counter = counter + 1
print("your total marks = ",total_marks)


marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
a = 0
for i in marks:
    a += int(i)
print("your total marks = ",a)


Q.2
name = ["Savitri", "Phule", "26"]
 Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
print(name[0]+name[1]+name[2])
Code mei dekhiye naam theek se print kyu nahi ho raha


a = [1,2,3,[4,5,8],8,6,7,[3,6,8],[4,5,7]]
b = []
for j in a:
    if type(j) == list:
        b.extend(j)
    else:
        b.append(j)
print(b)

find the pair.
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
a=[]
for x in n:
    for y in n:
        if x+y==30:
            if [x,y] not in a and [y,x] not in a:
                a.append([x,y])
            n.remove(y)
print(a)
    
flatten list question.

l = [1, 2, [3, 4, [5, [[[6]], 7], 8, [9, [10,[12,45,34]]]]]]
output = []
def call(l):
    for i in l:
        if type(i) == list:
            call(i)
        else:
            output.append(i)

print ('The original list: ', l)
call(l)
print ('The list after removing nesting: ', output)


def pair ():
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    h = []
    for j in range(len(a)):
        g = [j,j+1]
        h.append(g)
    print(h)
pair()


pair find

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

n=int(input("enter the number: "))

print([a[n*y:n*(y+1)] for y in range((len(a)+n-1)//n)])


question .

Q 1.

a = [1,2,3,9]
b = [2,3,4]
g = []
h = []
for j in a:
    if j not in b:
        g.append(j)
for i in b:
    if i not in a:
        h.append(i)
print(g)
print(h)

Q.2

a = [1,2,3,3,5,1,4,8,9]
b = []
for j in a:
    if j not in b:
        if j == 1 or j == 3:
            b.append(j)
print(b)

Q.3

The main difference between the sort() function and the sorted() 
function is that the sort function will modify the list it is called on. The sorted() function will create a
new sequence type containing a sorted version of the sequence it is given.


Q.4

n = int(input("enter the size of the list: "))
b = []
for i in range(n):
    c = int(input("ente the number: "))
    b.append(c)
print(b)
for i in range(n):
    for j in range(0,n-1-1):
        if b[j] > b[j+1]:
            t = b[j]
            b[j] = b[j+1]
            b[j+1] = t.
print("sorted list is = ",b)


one time add or remove in list

a = [ 1,2,3,4,5,6,7,8,9 ] 
b = []
for i in a[::-1]:
    b.append(i)
    a.remove(i)
print("a = ",a)
print("b = ",b)

