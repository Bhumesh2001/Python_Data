dict() function
create a dictionary,with dictionary function.
student=dict(name="Ravina",age= 20)
print(student)

# aceess element frome dictionary.

person={'name':'jack','age':20,'gender':'male',4:'organisation'}
result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result)
 
 
# get() function.   
# We can also make use of the get() function to access dictionary values.
person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
print(person['gender'])

print(person[4])

result = person[4]['place']

print(result)

Adding Elements to a Dictionary.

dic= {'Name': 'RAM', 'Age': 17}

dic['ORGANIZATION'] = "NAV GURUKUL"

dic['place'] = 'dharamsala'

print(dic)


dic= {'Name': 'RAM','Age': 17,}
dic['student']={'id':22,'place':'dharamsala'}
print(dic)

Key Exists or not

car ={"brand":  "ford","model":  "mustang","year":  1964}
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary.")
else:
    print("No, 'model' key dictionary mai nahi hai.")

Updating Dictionary .

person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)

details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
details['student']['id']=35
print(details)

# Copy of Dictionary :-

classes ={"room1":  "6th","room2":  "7th","room3":  "8th"}
mydict=classes.copy()
print(mydict)


Removing Elements from a Dictionary:-

pop()

CAR_DETAILS={"brand": "Ford","model": "jason","year": 1964}
CAR_DETAILS.pop("model")
print(CAR_DETAILS)

# popitem()

person={'name':'jack','id':22,'place':'dharamsala'}
person.popitem()
print(person)

del()

person={'name':'jack','id':22,'place':'dharamsala'}
del person
print(person)


person={'name':'jack','id':22,'place':'dharamsala'}
del person('place')
print(person)

iterations

Iterate through all keys.

states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
for state in states_capitals:
  print(state)
  


Iterate through all values.

states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
for state in states_capitals:
    print(states_capitals[state])


details ={"name":  "Bijender","age":  17,"class":  "10th"}
for x in details.values():
    print(x)
    
    
How to print keys and values together from a dictionary?


movie ={"name":  "Puli","hero":  "Vijay","rating":  7.5}
for x,y in movie.items():
    print(x,y)

len()

meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
print(len(meal))


dict. meraki Questions.

Q.1

# type 1

d1={1:10, 2:20}
d2={3:30,2:40}
d3={5:50,6:60}
g = {}
for i in d1,d2,d3:
    g.update(i)
print(g)

type 2

d1={1:10, 2:20}
d2={3:30,2:40}
d3={5:50,6:60}
g = {}
g = {*d1,d2,*d3}
print(g)

Q.2
input in dictionary
d = {}
n = int(input("enter number of eliment: "))
for j in range(n):
    b = input("enter key: ")
    c = input("enter value: ")
    d.update({b:c})
print(d)

dict1={'name':'raju','marks':56}
print(dict1)
h = input("enter keys:")
if h in dict1:
    print("exist")
else:
    print("not exist")

Q.3

my_dict = {'data1':100,'data2': -54,'data3': 247}
add = 0
for i in my_dict.values():
    add += i
print(add)


Q.4

d = {1: 'NAVGURUKUL',2: 'IN',3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
del d[3]['A']
print(d)

Q.5

r=['one','two','three','four','five']
l=[1,2,3,4,5,]
a = {}
for i in range(len(r)):
    a[r[i]] = l[i]
print(a)
    
dictionary comprihension .

r=['one','two','three','four','five']
l=[1,2,3,4,5,]
d = {r[i]:l[i] for i in range(len(r))}
print(d)

Q.6

type 1

dic={"ball":"red","bat":"4","vickets":"8","ball":"green","bat":"3"}
f = {}
for k,v in dic.items():
    if v not in f.keys():
        f[k] = v
print(f)

type 2

dic={"ball":"red","bat":"4","vickets":"8","ball":"green","bat":"3"}
g = []
r = dict()
for k,v in dic.items():
    if v not in g:
        g.append(v)
        r[k] = v
print(r)

Q.7

dic = [{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
e = []
for j in dic:
    for i in j:
        if (j[i]) not in e:
            e.append(j[i])
print(e)
        
Q.8 

d = {}
for j in range(10):
    b = input("enter name of students: ")
    c = input("enter arks of students: ")
    d.update({b:c})
print(d)

Q.9

b = "MISSISSIPPI"
a = {}
for i in b:
    count = 0
    for k in b:
        if i == k:
            count+=1
    a[i]=count
print(a)

Q.10

type 1

dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}  
c = []
for i in dict1.values():
    if type(i) == list:
        c.extend(i)
print("total count = ",len(c))

type 2

dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
count = 0
for j in dict1:
    if j:
        count+=len(dict1[j])      
print(count)
    
Q.11

type 1

my = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
l = []
for i in my.values():
    l.append(i)
l.sort()
print("3 highest value is = ",l[-3:])

type 2

dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
a=sorted(dict.values())
print("3 highest value is = ",a[-3:])

Q.12
type 1

dict={x:x*x for x in range (1,16)}
print(dict)

type 2

dict1 = {}
a = int(input('enter the range:-'))
for i in range(1,a):
    m = i*i
    dict1[i]=m
print(dict1)

Q.13

dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
a=sorted(dict.keys())
print("3 highest keys is = ",a[-3:])


my = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
l = []
for i in my.keys():
    l.append(i)
l.sort()
print("3 highest value is = ",l[-3:])

Q.14
type 1

w = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
b = sorted(w.items())
print(dict(b))

type 2

import operator

w = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
print("orignal list is = ",w)

a = dict(sorted(w.items(), key = operator.itemgetter(1)))
print("ascending order is = ",a)

d = dict(sorted(w.items(),key = operator.itemgetter(1),reverse = True))
print("descending order is = ",d)

type 3

w = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a = sorted(w.items(),key=lambda t:t [1])
print(dict(a))

type 4

w = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
d = sorted(w.values())
print(d)


code output
Q.1

a = {(1,2):1,(2,3):2}
print(a[1,2])

Q.2

a = {'a':1,'b':2,'c':3}
print(a['a','b'])

Q.3

fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print(len(fruit))
print(fruit)


Q.4

Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student
Details['Age'] = Age

print(Details)
print(Age)

Q.5

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum)
print(my_dict)


Q.6

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates))
print(len(box))


Q.7

rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
id1 = id(rec)
del rec

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)

debug code.

Q.1

details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}
print(details["name"])
print(details["age"])

Q.2

dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():
    sum=sum+i
print(sum)

Q.4

c=dict()
for i in range(1,16):
    e=i*i
    c[i]=e
print(c)

Q.5

s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)  


d1={1:10, 2:20}
d2={3:30,2:40}
d3={5:50,6:60}
g = {}
for j in d1,d2,d3:
    for i in j.keys():
        g[i] = g.get(i,0)+j[i]
print(g)


a = ["emp1","emp2","emp3"]
b = ["bhumesh","raja","akash"]
c = ["m","m","m"]
e = [34,23,56]
o = [["HR",5000,5],["CEO",6000,6],["project manager",7000,8]]
d = {}
for j in range(len(a)):
    d.update({a[j]:{"name":b[j],"sex":c[j],"age":e[j],
    "other detail":{"post":o[j][0],'salary':o[j][1],"year":o[j][2]}}})
print(d)

print({a[j]:{"name":b[j],"sex":c[j],"age":e[j],
"other detail":{"post":o[j][0],'salary':o[j][1],"year":o[j][2]}} for j in range(len(a))})
