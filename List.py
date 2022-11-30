a = [10,20,20.56,"Hello"]
print(type(a))
print(a)

b = list()
print(type(b))
b = [10,20]
print("b",b)

data = input("data: ")
print("type of data:",type(data))
list1 = data.split(",") # split() ats pace is used to convert a string into list
print("list:",list1)
print("type of list:",type(list1))
list1[0] = "Johnny"  # Mutable list replacing first element in list to given value to johny
print("list:",list1)

l1 = [10,20,30,40,50]
print(l1)
index = int(input("Enter index to print :"))
if index>len(l1)-1 or index<-len(l1):
    print("{invalid")
else:
    print(l1[index])

chars = ['a','b','c','d']
print(chars)

chars[3] = "xyz"
print(chars)

chars.append("abc")
print(chars)
print(len(chars))

chars.append(['f','g'])
print(chars)

list2 = [1,2,3]
chars.extend(list2)
print(chars)

list1 = ["hi","hello","lists"]
print(list1[0])
print(list1[1])
print(list1[2])

x = [1,2,3]
y = [3,4,5]
print(x==y)

a = ['', 2, 3, "all"]
print(all(a))

a=['a','b','c','d']
print(list(enumerate(a)))
print(list(enumerate(a,3)))

print(max([1,2,3,4,10,20]))
print(min([1,2,3,4,10,20]))

a = [10,1,2,20,5,4]
sortedlist=sorted(a)
print(sortedlist)
print(a)

a = [23,6,5,31,89,66,8,10]
print(sorted(a))
print(a)

data =input("data:")
list1 = data.split(",")
size = len(list1)
for i in range(size):
    list1[i]=int(list1[i])
max_val = max(list1)
min_val = min(list1)
print("min:",min_val)
print("max:",max_val)
difference = max_val - min_val
print("difference:", difference)

data1 = input("data1:")
data2 = input("data2:")
l1 = data1.split(",")
l2 = data2.split(",")
str1 = '{'
if len(l1)!=len(l2):
    print("lists are different lengths")
    exit()
else:
    for i in range(len(l1)):
        str1=str1+"'"+l1[i]+"'"+":"+"'"+l2[i]+"'"+","
print(str1[0:len(str1)-1]+"}")

a = [1, 2, 3, 4, ' ']
print(all(a))

a = (1, 2, 3, 4)
print(type(a))
print(a)
print(list(a))
print(type(a))
a = list(a)
print(a)
print(type(a))

a = (1, 2, 3, 4, [10, 20], 4)
print(type(a))
a[4][0] = 100
print(a)

l1 = [1, 2, 3, 4]
print(tuple(l1))
print(type(l1))

data = input("data:")
list1 = data.split(",")
tuple1 = (tuple(list1))
print(tuple1)

a = (1)
print(type(a))

a = 1, 2, 3
b = 10, 20, 30
c = a+b
print(c)
print(type(c))

a = (1, 2, 3, 4, [10, 20])
a[4][1] = 200
print(a)

data = input("data:")
list1 = data.split(",")
tuple1 = tuple(list1)
index = int(input("index:"))
list2 = []
if index < len(list1) and len(list1) >= (index):
    value = input("value:")
    list2 = list(tuple1)
    list2[index] = value
    tuple2 = tuple(list2)
    print("tuple:", tuple2)
else:
    print("enter valid index")

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)


