### while
# x = 1
# y = 1
# while x < 10 and y < 20:
#   print('O valor de x * y é: ', x * y)
#   x += 1
#   y += 2
# else:
#   print('O valor de x * y é: ', x * y)


### break
# x = 1
# lista = []

# while True:
#   lista += [x]

#   x += 1

#   if x > 10:
#     break

# print(lista)


### continue
ate = 50
x = 1

while x < ate:
  x += 1

  if x % 2 == 1:
    continue

  if x % 2 == 0:
    print(x, 'é par')