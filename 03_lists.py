######## Listas ########
my_list = [1,2,3]
print(my_list)

my_list2 = [1, 2, 2.3, 'string']
print(my_list2[1:3] + my_list)

print(len(my_list))

lst_1 = [ 1, 2, 3 ]
lst_2 = [ 4, 5, 6 ]
lst_3 = [ 7, 8, 9 ]

matrix = [ lst_1, lst_2, lst_3 ]

# print(matrix[1][1])

first_col = [ row[0] for row in matrix ]
print(first_col[1])