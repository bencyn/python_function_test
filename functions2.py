# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0
evens = filter(even_bool,mylist)
print(list(evens))
# lamba expressions
evens2 = filter(lambda num:num%2 ==0,mylist)
print(list(evens2))

# stirng split
tweet = "Go Sports! #Sports"
result = tweet.split('#')
result1 = tweet.split("!#")
result2 = tweet.split("#")[0]

print(result)
print(result1)
print(result2)
# better searching through text
'x' in [1,2,3]
print('x' in [1,2,3])
print('x' in [1,2,3,'x'])
