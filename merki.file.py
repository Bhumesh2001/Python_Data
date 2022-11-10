meraki site question
Q.1 

file1 = open("people1-exercise.txt","r")
file2 = file1.read()
print(file2)
file1.close()

Q.2


file1 = open("people1-exercise.txt","r")
file2 = file1.read()
sp = file2.split("\n")
count=0
for j in sp:
    if j:
        count+= 1
print("number of file line = ",count)
file1.close()

Q.3

file2 = open("file-question3.txt","a")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
for j in banks_list:
    file2.write(j)
    file2.write("\n")
file2.close()
print("file stored succesfully")

Q.4 

b = ["rishabh - meerut","imtiyaz - delhi","nilima - cochin","rati - shimla","ayishah - delhi","raghu - shimla",
     "naseer - kanpur","karthikeyan - delhi","salma - jaipur","pankaj - delhi","brijesh - delhi",
     "govind - delhi","puneet - shimla","siddhi - delhi",
     "suman - jaipur","rajeev - shimla","mohinder - delhi","rajendra - jaipur","priyanka - shimla",
     "neela - delhi","sashi - jaipur","sarika - delhi","deepti - shimla","harshad - delhi","trishna - raipur",
     "pradeep - jaipur",
     "sekhar - delhi","nand - delhi","anoop - delhi","balwinder - tokyo",]
for j in b:
    if j[-5:] == "delhi":
        file1 = open("delhi.txt","a")
        file1.write(j)
        file1.write("\n")
        file1.close()
    elif j[-6:] == "shimla":
        file1 = open("shimla.txt","a")
        file1.write(j)
        file1.write("\n")
        file1.close()
    else:
        file1 = open("other.txt","a")
        file1.write(j)
        file1.write("\n")
        file1.close()
print("data stored succesfully....")
