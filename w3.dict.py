# Q.1
# import operator

# w = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print("orignal list is = ",w)

# a = dict(sorted(w.items(), key = operator.itemgetter(1)))
# print("ascending order is = ",a)

# d = dict(sorted(w.items(),key = operator.itemgetter(1),reverse = True))
# print("descending order is = ",d)

# Q.2

# c = {0: 10, 1: 20}
# c.update({2:30})
# print(c)

# Q .3

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# r = {}
# for i in dic1,dic2,dic3:
#     r.update(i)
# print(r)

# Q.4
# b = input("enter the key: ")
# a = {"bhumesh":67,"rahul":87,"raja":89,"praveen":90}
# if b in a:
#     print("allready exist")
# else:
#     print("not exist")

# Q.5

# c = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# for key, value in c.items():
#     print(key,"-:-",value)

# Q.6

# b = int(input("enter the renge: "))
# dict={x:x*x for x in range (1,b)}
# print(dict)

# type 2

# dict1 = {}
# a = int(input('enter the range:-'))
# for i in range(1,a):
#     m = i*i
#     dict1[i]=m
# print(dict1)  
 
# Q.7


# c = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# b = {"rahul":45,"us":78,"rajat":"nagpur"}
# c.update(b)
# print(c)

# Q.8

# c = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# for j,i in c.items():
#     print(j,i)

# Q.9

# z = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# add = 0
# g = 0
# for j in z.values():
#     add += j
#     for i in z.keys():
#         g += i
# print("sum of values = ",add)
# print("sum of keys = ",g)
   

# Q 10

# z = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# mul = 1
# for j in z:
#     mul= mul*z[j]
# print(mul)

# Q.11

# s = ["bhumesh",56,"raja",67,"rahul",89,"praveen",23]
# g = [45,67,"aniket",56,"tiwari"]
# f = dict(zip(s,g))
# print(f)
 
 
# s = ["bhumesh",56,"raja",67,"rahul",89,"praveen",23]
# g = [45,67,"aniket",56,"tiwari"]
# d = []
# for j in s,g:
#     d.extend(j)
# print(d)

# Q.12

 
# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23}
# f = sorted(s.values())
# print("maximum number is",f[-1])
# print("minimum number is = ",f[1])
        
# Q.13  
  
# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23}
# a = sorted(s.keys())
# print("sorted dict is = ",a)

# Q.14

# a = {}
# n = int(input("enter the range: "))
# for i in range(1,n):
#     g = input("enter the key: ")
#     h = input("enter the value: ")
#     a.update({g:h})
# print(a)


# Q.15

# remove dublicates frome dictionary.

# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23,"bhumesh":34,"rahul":78}
# p = {}
# for j,i in s.items():
#     if j not in p:
#         p[j]=i
# print(p)
        
# Q.16  

# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23,"bhumesh":34,"rahul":78}
# if not bool(s):
#     print("dictionary is empty")
# else:
#     print("dictionary is not empty")


# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23,"bhumesh":34,"rahul":78}
# if not s:
#     print("empty")
# else:
#     print("not empty")


# s = {"bhumesh":56,"raja":67,"rahul":89,"praveen":23,"bhumesh":34,"rahul":78}
# if len(s) == 0:
#     print("empty")
# else:
#     print("not empty")

# Q.17

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# t = []
# y = []
# for i in d2.keys():
#     t.append(i)
# for j in d1.values():
#     if j == 100:
#         r = j + 300
#         y.append(r)
#     elif j == 200:
#         d = j + 200
#         y.append(d)
#     elif j == 300:
#         g = j + 100
#         y.append(g)
# u = dict(zip(t,y))
# u.update({"c":300})
# print(u)

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3= {}
# d3.update(d1)
# d3.update(d2)
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i == x:
#             d3[i] = j+y

# Q.18

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values is: ",u_value)


# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b = []
# a = []
# for d in L:
#     for j in d.values():
#         a.append(j)
# for e in a:
#     if e not in b:
#         b.append(e)
# print(set(b))



# d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# a=[]
# for i in d:
#     for j in i.values():
#         a.append(j)
# print(set(a))

# Q.19
    
# d = {'1':['a','b'], '2':['c','d']}
# a,b = d.values()
# for i in a:
#     for j in b:
#         print(i+j)

# Q 20

# d = {'a':500, 'b':
# 874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# a=list(d.keys())
# a.sort()
# print('three largest ',a[:-4:-1])
        
# Q.21   
        
# d=[{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d1={}
# for i in d:
#     if i['item'] in d1.keys():
#         d1[i['item']]+=i['amount']
#     else:
#         d1[i['item']]=i['amount']
# print(d1)

# Q.22
    
# m = 'w3resource'
# d = {}
# for x in m :
#     if x in d :
#        d[x] = d[x] + 1
#     else :
#         d[x] = 1
# print(d)

# Q.23


# t = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(*list(t.keys()))
# a=(list(t.values()))
# for i in range(len(a)):
#     print(*(a[i]))


# Q.24

# st = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# count = 0
# for i in st:
#     count+=i["id"]
# print(count)

# Q.25

# t = [1, 2, 3, 4]
# r = {}
# for i in t:
#     r[i]={}
# print(r)
    
# 26

# n = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in n:
#     n[i]=sorted(n[i])
# print(n)

# Q.27.

# d = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
# d1= {}
# for i,j in d.items():
#     for x in " ":
#         i = i.replace(x,"")
#         d1[i]= j
# print(d1)

# Q.28.

# data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# data = sorted(data.items() , key = lambda item:item[1], reverse = True)
# print(data[:3])

# Q.29.

# m = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key value count")
# count = 1
# for i in m:
#     print(i," ",m[i],"  ",count)
#     count += 1


# m = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count = 1
# print("key value count")
# for i,j in m.items():
#     print(i," ",j," ",count)
#     count += 1
    

# Q.30

# s = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in s:
#     print(i)
#     for j in s[i]:
#         print(j,":",s[i][j])


# a= {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i,j in a.items():
#     print(i)
# for x,y in j.items():
#     print(x,y)

# Q.31

# t = {'name': 'Alex','class': 'V','roll_id': '2'}
# if "name" and "class" in t:
#     print("true")
# else:
#     print("false")
     
     
# t = {'name': 'Alex','class': 'V','roll_id': '2'}
# count = len(t.keys())
# if count > 1:
#     print("true")
# else:
#     print("false")

# Q.32

# d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count = 0
# for i in d.values():
#     for j in range(len(i)):
#         count += 1
# print(count)


# d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# b = 0
# for i,j in d.items():
#     b += len(j)
# print(b)

# Q.33

# data = {'Math':81, 'Physics':83, 'Chemistry':87}
# list1 = sorted(data.values())
# r = []
# for n in list1[: : -1]:
#     for key, values in data.items():
#         if n == values:
#             r.append((key, values))
# print(r)
    

# Q.34

# s = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# d = [1, 2, 2, 3]
# print(dict(zip(s,d)))


# list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# list2 = [1, 2, 2, 3]
# d = {}
# for i in range(len(list1)):
#     if list1[i] not in d:
#         d[list1[i]] = {list2[i]}
#     elif list1[i] in d:
#         d.update({list1[i]: {list2[i]}})
# print(d)

# Q.35

# l = [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
# for i in l:
#     a = i.pop("id")
#     i["id"]= a
#     n1 = i.pop('V')
#     n2 = i.pop('VI')
#     i['V+VI'] = (n1 + n2)/2
# print(l)


# Q.36

# d1 = {'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# d3={}
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i ==x and j==y:
#             d3[i]=j
# print(d3)


# a,b={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# for k,v in zip(a,b):
#     if a[k]==b[v]:
#         print(k,": is present in both a,and b")

# Q.37

# d = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
#                {"firstName": "Mervin", "lastName": "Friedland"},
#                {"firstName": "Aron ", "lastName": "Wilkins"}],
# "teachers":[{"firstName": "Amberly", "lastName": "Calico"},
#          {"firstName": "Regine", "lastName": "Agtarap"}]}
# print("Original dictionary:")
# print(d)
# print(type(d))
# import json
 
# with open("dictionary", "w") as f:
#    json.dump(d, f, indent = 4, sort_keys = True)
 
# print("\nJson file to dictionary:")
# with open('dictionary') as f:
#  data = json.load(f)
# print(data)

# Q.38


# dic = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for key,value in dic.items():
#     print(value[4])
# for k,v in dic.items():
#     print(k,"has value",v)

# Q.39


# a = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# del a["c3"]
# print(a)

# a = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# h = {}
# for j,i in a.items():
#     if i is not None:
#         h.update({j:i})
# print(h)

# a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# x={}
# for k, v in a.items():
#     if v!=None:
#         x[k]=v
# print(x)


# a = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# di = {j:i for j,i in a.items()if i is not None}
# print(di)

# Q.40

# w = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d = {}
# for k,v in w.items():
#     if v > 170:
#         d[k] = v
# print(d)

# Q.41

# a = ['S001', 'S002', 'S003', 'S004']
# b = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c = [85, 98, 89, 92]
# for j,k,l in zip(a,b,c):
#     print({j:{k:l}},end="")
    

# l1 = ['S001', 'S002', 'S003', 'S004']
# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3 = [85, 98, 89, 92]
# l5 =[]
# l6 = []
# for i in range(len(l2)):
#     d2 = {}
# for j in range(len(l3)):
#     if i == j:
#         d2.setdefault(l2[i],l3[j])
#     l5.append(d2)
# print(l5)
# for x in range(len(l1)):
#     d3 = {}
#     d3.setdefault(l1[x],l5[x])
#     l6.append(d3)
# print(l6)

# Q.42

# a = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 
#      'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# for k,v in a.items():
#     if v[0] >= 6.0 and v[1] >= 70:
#         print({k:v})

# Q.43

# val = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# for j in val.values():
#     if j == 12:
#         print("true")
#     else:
#         print("false")

# Q.44

# w = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {}
# for i in w:
#     if i[0] not in d.keys():
#         d.update({i[0]:i[1]})
# print(d)

# w = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# b = {}
# for k,v in w:
#     b.setdefault(k,[]).append(v)
# print(b)

# Q.45

# m = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# d = []
# a,b = m.values()
# for i in range(len(a)):
#     for j,k in m.items():
#         b = ({j:k[i]})
#         d.append(b)
#         print(b,end=" ")


# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# res=[dict(zip(d.keys(), itm)) for itm in list(zip(*d.values()))]
# print(res)


# Q.46

# dic1 = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
#         {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# for j in range(len(dic1)):
#     if (j) != 0:
#         print(dic1[j],end=" ")

    
# Q.47

# l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

# a,b=l
# a1={}
# a2={}
# fl=[]
# for i,j in a.items():
#     d={i:int(j)}
#     a1.update(d)
# for i,j in b.items():
#     d1={i:int(j)}
#     a2.update(d1)
#     fs=a1,a2
# for i in fs:
#     fl.append(i)
# print(fl)

# fl = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# a,b = fl
# b1 = {}
# b2 = {}
# c = []
# for k,v in a.items():
#     g = {k:float(v)}
#     b1.update(g)
# for j,i in b.items():
#     h = {j:float(i)}
#     b2.update(h)
#     fk = b1,b2
# for d in fk:
#     c.append(d)
# print(c)


# Q.48

# t = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for k in t.keys():
#     t[k] = []
# print(t)


# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# v = []
# for i,j in a.items():
#     if len(j)>0:
#         b = i,[]
#         v.append(b)
# print(dict(v))

# Q.49

# x = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# x['Math'][0]=91
# x['Math'][1]=90
# x['Math'][2]=91

# x['Physics'][0]=90
# x['Physics'][1]=92
# x['Physics'][2]=87
# print(x)


# Q.50

# dic1 = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# f = []
# for j in dic1:
#     f.append(j['Science'])
# print(f)


# dic2 = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# t = []
# for j in dic2:
#     t.append(j['Math'])
# print(t)
      
      
# Q.51

# l = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print({v:len(v) for k,v in l.items()})


# m = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# print({i:len(i) for j,i in m.items()})

# Q.52

# dict = {'a':1, 'b': {'c': {'d': {}}}}
# s = str(dict)
# c = 0
# for i in s:
#     if i =="{":
#         c +=1
# print(c)


# Q.53

# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])


# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# d1,d2,d3 = num
# print(d1)
# print(d2)
# print(d3)

# 54

# d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print([[k,v] for k,v in d.items()])

# a = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# print([[j,i] for j,i in a.items()])

# Q.55


# d ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in d.keys():
#     for j in d[i]:
#         if j % 2 == 0:
#             d[i] = [j]
# print(d)


# d ={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for k in d.keys():
#     d[k] = [i for i in d[k] if i%2 == 0]
# print(d)


# d = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for k in d.keys():
#     d[k] = [i for i in d[k] if i == 2]
# print(d)


# Q.56

# from itertools import combinations

# o={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# print([{k1: o[k1], k2: o[k2]} for k1, k2 in list(combinations(o.keys(), 2))])

# Q.57

# dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# f=[]
# for i,j in sorted(dic.items(),key=lambda x:x[1],reverse=True):
#     f.append(i)
#     break
# print(f)
# t=[]
# for i,j in sorted(dic.items(),key=lambda x:x[1],reverse=True):
#     t.append(i)
# print(t[:5])

# d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# t = []
# for j in (d.items()):
#     t.extend(j)
# print(t[-8])


# Q.58

# o = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# b = []
# for i,k in o.items():
#     if len(k) <= 1:
#         b.append(i)
# print(b)


# o = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# print([j for j,k in o.items() if len(k) <= 1])

# Q.60

# v = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# d = {}
# for j in v.values():
#     if j in d:
#         d[j] += 1
#     else:
#         d[j] = 1
# print(d)
      
          
# Q.61

# h = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#      {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
#      {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
#      {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
#      {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# print([list(i.values())for i in h])



# h = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#      {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
#      {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
#      {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
#      {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# a = []
# for j in h:
#     a.append(list(j.values()))
# print(a)


# Q.62


# y = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# a = {}
# for j,i in y.items():
#     for e in i:
#         f = {j:[e]}
#         a.update(f)
# print(a)


# y = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# print({j:[i[0]]for j,i in y.items()})

# Q.63

# y = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# a = []
# for j,i in y.items():
#     for e in i:
#         f = {j:e}
#         a.append(f)
# print(a)


# h = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# print({i:j[0] for i,j in h.items()})

# Q.64

# j = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# count = 0
# for k,v in j.items():
#     count += len(v)
# print(count)

# Q.65

# d = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
# {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
# {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
# {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
# {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# for j in d:
#     if ("name") in j:
#         print("true")
#     else:
#         print("false")

# Q. 66

# d={'Ora Mckinney': 8,'Theodore Hollandl': 7,'Mae Fleming': 7,'Mathew Gilbert': 8,'Ivan Little': 7,}
# d2 = {}
# for k,v in d.items():
#     d2.setdefault(v,[]).append(k)
# print(d2)

# Q. 67

# d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# d2 = {'x': 300, 'y': 'Red', 'z': 600}
# d3 = {}
# for i,j in d1.items():
#         d3.setdefault(i,[]).append(j)
# print(d3)


# Q.68

# from collections import defaultdict
# from math import floor
# def test(lst, fn):
#   d = defaultdict(list)
#   for el in lst:
#     d[fn(el)].append(el)
#   return dict(d)
# nums = [7,23, 3.2, 3.3, 8.4]
# print("Original list & function:")
# print(nums," Function name: floor:")
# print("Group the elements of the said list based on the given function:")
# print(test(nums, floor))
# print("\n")
# print("Original list & function:")
# colors = ['Red', 'Green', 'Black', 'White', 'Pink']
# print(colors," Function name: len:")
# print("Group the elements of the said list based on the given function:")
# print(test(colors, len))

# Q.69

# d = {}
# for j in range(1,5):
#     d[j] = j*j
# print(d)

# print({j:j*j for j in range(1,5)})

# Q.70

# from functools import reduce 
# from operator import getitem
# def test(d, selectors):
#   return reduce(getitem, selectors, d) 
# users = {
#   'Carla ': {
#     'name': {
#       'first': 'Carla ',
#       'last': 'Russell' 
#     },
#     'postIds': [1, 2, 3, 4, 5]
#   }
# }
# print(test(users, ['Carla ', 'name', 'last']))
# print(test(users, ['Carla ', 'postIds', 1]))

# 71

# st = {'Theodore': 10,'Mathew': 11,'Roxanne': 9,}
# g = {}
# for j,k in st.items():
#     g.update({k:j})
# print(g)

# Q.72

# n = [{'name': 'Theodore', 'age': 18},{'name': 'Mathew', 'age': 22}, 
# {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# h = []
# for i in n:
#     p = (i['age'])
#     h.append(p)
# print(h)

# Q.73

# f = {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 
#     'Mathew': {'user': 'Mathew', 'age': 21}}
# r = {}
# for k,v in f.items():
#     b = (v['age'])
#     r.update({k:b})
# print(r)

# Q.74

# d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# a = []
# for j in d:
#     a.append(j)
# del a[0]
# del a[1]
# print(a)

# Q.75

# a = ['a', 'b', 'c', 'd', 'e', 'f']
# b = [1, 2, 3, 4, 5]
# s = {}
# for j,k in zip(a,b):
#         s.update({j:k})
# print(s)

# Q.76

# m = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# f = []
# for k in m.items():
#     f.append((k))
# print(f)

# Q.77


# m = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# gh = []
# for j in m.keys():
# #     gh.append(j)
# # print(gh)


# Q.78

# k = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# y = []
# for v in k.values():
#     y.append(v)
# print(y)


# Q.79

# u = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# h = []
# for j in u.keys():
#     h.append(j)
# print(sorted(h))
# print("max key and min key",(h[0],h[1]))