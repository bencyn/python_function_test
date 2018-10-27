# making a list of lists to form a matrix

lst_1= [1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix =[lst_1,lst_2,lst_3]
print (matrix[0])
# sort for lists
new_list = ['a','e','x','b','c']
# reverse list
new_list.reverse()
print (new_list)
# sort list
new_list.sort()
print (new_list)

# list comprehesions
# matrix2 = [[1,2,3]]
first_col =[row[2] for row in matrix]

print(first_col)
