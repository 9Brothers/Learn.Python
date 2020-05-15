# l = [1, 2, 3, 4, 5, 6, 7]

### iteração
# for num in l:
#   print(num)


### resto de divisão
# for num in l:
#   if num % 2 == 0:
#     print(num, 'é par')
#   else:
#     print(num, 'é impar')


### somatório
# _sum = 0

# for num in l:
#   _sum += num

# print(_sum)


### strings
# string = 'Essa é uma string!'

# for char in string:
#   print(char)


### tuplas
# tup = (1, 2, 3, 4, 5)
# for t in tup:
#   print(t)

# l = [(1,2), (2,3), (3,4)]
# (t1, t2) = l[0]

# for (t1, t2) in l:
#   print(t1 * t2)


### dicionários
## retorna as chaves
# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for item in d:
#   print(item)

## retorna os valores
d = {'k1': 1, 'k2': 2, 'k3': 3}
for (key, value) in d.items():
  print(key, ': ', value)