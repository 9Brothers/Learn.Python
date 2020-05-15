### valores positivos (0,1,2,3,4,5...)
# _range = range(0, 10, 1)

# lista = list(_range)

# print(lista)


### valores positivos de dois em dois
# _range = range(0, 30, 2)

# lista = list(_range)

# print(lista)


### valores positivos em ordem decrescente
# _range = range(30, 0, -2)

# lista = list(_range)

# print(lista)


### valores negativos em ordem decrescente
# _range = range(0, -30, -2)

# lista = list(_range)

# print(lista)


### exemplo de uso de range() + for
for i in range(0, 100):
  print(i)

  if i > 10:
    break