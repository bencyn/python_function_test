# slicing

mystring= 'abcdefg'

print("original string :" + mystring)
print(mystring[2:])
# index upto
print(mystring[:3])

# grab
print(mystring[2:5])

# grab by step sizes

print(mystring[::2])
print(mystring[::3])
print (mystring.upper())
# split strings
mystring2= "Hello World"
x = mystring2.split('e')
print(x)

# print formatting
n = "Item one : {} Item Two: {}".format("dog","cat")
print (n)
y= "Item one : {x} Item Two: {y}".format(x="dog",y="cat")
print(y)

var="bencyn"
print(var)
var="wangechi"
print(var)
