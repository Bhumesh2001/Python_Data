flattern list 

 l = [1, 2, [3, 4, [5, [[[6]], 7], 8, [9, [10,[12,45,34]]]]]]
output = []
def call(l):
    for i in l:
        if type(i) == list:
            call(i)
        else:
            output.append(i)

print ('The original list: ',l)
call(l)
print ('The list after removing nesting: ', output)



list1 = [1, 2, [3, 4, [5, [[[6]], 7], 8, [9, [10,[12,45,34]]]]]]
l2 = []
print("orignal list = ",list1)
while list1:
    r = list1.pop()
    if type(r) == list:
        list1.extend(r)
    else:
        l2.append(r)
l2.sort()
print(l2)
