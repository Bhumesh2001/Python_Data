# # binary file create.

# import pickle
# def write():
#     f = open("myfile.det","wb")
#     lis = ["bhumeh","rahul","akash","raja","aniket"]
#     pickle.dump(lis,f)
#     f.close()
# def readfile():
#     f = open("myfile.det","rb")
#     list2 = pickle.load(f)
#     print(list2)
#     f.close()
# write()
# readfile()  

# import pickle
# def write():
#     f = open("myfile.dat","wb")
#     record = []
#     while True:
#         roll = int(input("enter your roll no: "))
#         name = input("enter your name: ")
#         marks = int(input("enter your marks: "))
#         list1 = [roll,name,marks]
#         record.append(list1)
#         choice = input("enter your choice:(y/n)")
#         if choice == "n":
#             break
#     pickle.dump(record,f)
# def read():
#     f = open("myfile.dat","rb")
#     r = pickle.load(f)
#     for j in r:
#         print(j)
# def search():
#     f = open("myfile.dat","rb")
#     roll = int(input("enter your roll number: "))
#     flag = 0
#     r = pickle.load(f)
#     for i in r:
#         if i[0] == roll:
#             print(i)
#             flag = 1
#             break
#     if flag == 0:
#         print("roll no. not found")
# write()
# print("data stored succesfully")
# read()
# search()

