
# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }

# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()


# import json

# a={"lalalala": 3}
# mystring = json.dumps(a)
# print(mystring)


# Q.meraki question.

#Q.1

# import json
# json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
# print("json obj",json_obj)
# python_objects = json.loads(json_obj)
# print("python obj",python_objects)

# Q.2

# import json
# python_obj =  { 
#     "Name":"David", 
#     "Class":"I", 
#     "Age":6 
# }
# print(type(python_obj))
# json_data = json.dumps(python_obj)
# print(json_data)

# Q.3

# import json
# python_obj =  { 
#     "Name":"David", 
#     "Class":"I", 
#     "Age":6 
# }
# json_data = json.dumps(python_obj)
# print(type(json_data))
# print(json_data)

# Q.4

# import json
# python_obj = {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# json_data = json.dumps(python_obj,indent=6)
# print(json_data)

# Q.5

# import json
# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print("Complex_object: ",complex_object)
# print("Without complex object: ",simple_object)

# Q.6

# import json
# json_data = '{"a": 1,"a": 2,"a": 3, "a": 4,"b": 1, "b": 2}'
# print("orignal python object:-")
# print(json_data)
# obj = json.loads(json_data)
# print("uniq key in a json object")
# print(obj)

# Q.7

# import json
# filename = "file.txt"
# dict1 = {}
# with open(filename) as obj:
#     for line in obj:
#         b,h = line.strip().split(None,1)
#         dict1[b] = h.strip()
# file2 = open("test1.json","w")
# json.dump(dict1,file2,indent=6)
# file2.close()


# Q.8

# import json
# file1 = ["neelam","programer","24","2400"]
# file2 = ["komal","trainer","24","20000"]
# file3 = ["anuradha","HR","25","40000"]
# file4 = ["Abhishek","manage","29","63000"]
# d1 = {}
# for j in range(len(file1)):
#     d1.update({"emp1":{"name":file1[0],"designation":file1[1],"age":file1[2],"salary":file1[3]}})
#     d1.update({"emp2":{"name":file2[0],"designation":file2[1],"age":file2[2],"salary":file2[3]}})
#     d1.update({"emp3":{"name":file3[0],"designation":file3[1],"age":file3[2],"salary":file3[3]}})
#     d1.update({"emp4":{"name":file4[0],"designation":file4[1],"age":file4[2],"salary":file4[3]}})
# print(d1)

# json_file = open("employs.json","w")
# json.dump(d1,json_file,indent=6)
# json_file.close()

# Q.9

# import json

# json_file = {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

# file1 = open("shoping.json","w")
# json.dump(json_file,file1,indent=4)
# file1.close()
# print("file created succesfully.....")
# print(json_file)
# cost = input("which items do you want to buy?:  ")
# for j in json_file:
#     for i in json_file[j]:
#         if cost == i:
#             item = int(input("how many item do you want? "))
#             json_file[j][i] = str(item)
#             m1 = json_file
#             print(m1)
#             file1 = open("shoping.json","w")
#             json.dump(json_file,file1,indent=4)
#             file1.close()
#             print("take it your",i,":-",json_file[j][i],"item\neat and do enjoy")

