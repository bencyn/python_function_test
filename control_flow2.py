# range functions
for item in range(10):
    print (item)
# list comprehesions
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
# print(out)

compr = [num**3 for num in x]
print(compr)
