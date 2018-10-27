# logical operators
(1 > 2) and (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

if 1 <2:
    print("First Block")
    if 20 <3:
        print("Second Block")
    elif 3 == 3 :
        print('elif ran')
    else:
        print('last')
# loops
# for loops

seq =[1,3,4,5,6]

for item in seq:
    print("Hello {x}" .format(x=item))

d = {"sam":1,"Frank":2,"Dan":3}
for k in d:
    print(k)
    print(d[k])

# loop in tuples
mypairs = [(1,2),(3,4),(5,6)]
for p in mypairs:
    print(p)
# tuple unpacking
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)
# while loops
i = 1
while i<5:
    print("i is : {}".format(i))
    i = i +1
