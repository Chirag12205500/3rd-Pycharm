
# implemention  of operators
number1 = 10 # first variable
number2 = 20 # second variable
sum = number1+number2 #It will add two variables and display the result
print("Sum of two number is:",sum)

subtraction = number1-number2
print("subtraction of two numbers:",subtraction)
multiplication = number1*number2
print("multiplication of two numbers is:",multiplication)

division = number1/number2
print("division of two number is:",division)

remainder = number1%number2
print("remainder of two number is:",remainder)

number1 = 40
number2 = 50
integerdivision = number1//number2
print("integerdivision of two numbers is:", integerdivision)

number1 = 2
number2 = 3
power = number1**number2 # exponential value
print("power of number1 ^ number2 is:",power)


#Wap to convert celsius to fahrenheit
celsius = 40;
f = 32 +( 9/5 * celsius)
print("After conversion the result is:",f)
Side = 4
Area = Side * Side
print("Area of square is:", Area)

Side = 4
Perimeter = 4 * Side
print("Perimeter of the square is:", Perimeter)
b = 10
a = 3
a = a+2
print(a)
a+=2
print("value of a is:",a)
a+=b
print(a)
print("hello")

i = 10
if(i == 10):
   print("value of i is 10") #here the space before print is needed because of this " : "

number1 = 2
number2 = 3
Area = number1 * number2
print("Area of the rectangle is:", Area)


list1 = [1,2,3,"Hello"]
list2 = [10,20,30,23,"H1"]
print(type(list1))
print(type(list2))
print(list1)
print(list2)
print(list1[-1]) #for specific element                            #numbering[0,1,2,3,4,5,6,7]
list3 = [0,1,2,3,4,5,6]                                           #elements[0,1,2,3,4,5,6,7]
print(list3[1:4]) #we didn't get last element in the output       #numbering[-8,-7,-6,-5,-4,-3,-2,-1]
print(list3[0:-1])
print(list3[2:])
print(list3[:-1])

list4 = [1,2,2.5,4,"hello",5.5,"Chirag",7.5,9,"LPU"]
print(list4[1:6])
print(list4[0:])

list5 = [0,1,2,3,4,5,6]
list6 = [10,20,"hello"]
print(list5+list6)
print(list5*2)
#nested_list = list inside the list
list7 = [0,1,2,[3,4],5,6]
print(list7)
print(list7[3])
print(list7[4])

#set example
a = {1,2,3,4,4,}
print(type(a))
print(a)

a = 10
b = 10
print(id(a))
print(id(b))
a = 20
print(id(a))

myset = set()
print(myset)
print(type(myset))
myset1 = {}
print(type(myset1))
print(myset1)

myset2 = 1,2,3,4
print(type(myset2))
#tuples
tuple1 = tuple()
print(tuple1)
tuple2 = (1,2,3,4)
print(tuple2)
print(type(tuple2))

list = [1]
print(type(list))
tuple3 = (1,)
print(type(tuple3))

dict1 = dict()
print(dict1)
print(type(dict1))

dict2 = {"Hyderabad":20,"Delhi":30}
print(dict2)
print(type(dict2))

s = "1010"
int(s,10)
print(s)
print(int(s,2))
s1 = "10001"
print(int(s1,2))
print(int(s1,10))

print(float(23))
print(float('23.4'))
print(float("nan"))

print(ord('A'))
print(ord('Z'))

print(hex(45))
print(hex(50))

print(oct(45))

print(complex(10,3))
print(complex(10))

print(str("Hello"))
print(str(99.9))
a = str(99.99)
print(type(a))

a = 20
b = 10
print(eval("a*b"))
c = 100
d = 150
print(eval("c+d"))
print(chr(97))
print(chr(255))

str1 = ("python")
print(tuple(str1))
str2 = ("1,2,3,4,5,6,")
print(tuple(str2))

str3 = ("python")
print(set(str3))

str4 = ("pyyyythonnnn")
print(set(str4))

regdNo = input("12205500")
name = input("Chirag")
section = input("K22JL")
phoneNo = input("8219323980")
print(regdNo, name, section, phoneNo)
i = 10
f = 10.8
d = 19.7907
str5 = 'Hello'
#passing a single object to be printed to the print () function
print('Hello world!')
print(i,f,d,str1,sep= '**',end= 'XYZ')
print('Hello World!')
