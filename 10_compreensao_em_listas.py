### manualmente
# x = [1,2,3,4]


### utilizando o for
# x = []
# for i in range(0, 30):
#   x += [i]

# print(x)

# x = []
# for i in range(0, 30):
#   x.append(i)

# print(x)


### simplificando o for
# x = [i for i in range(0, 30)]
# print(x)


### operações matemáticas
# x = [i * 2 + 10 for i in range(0, 15)]
# print(x)


### operações lógicas
# x = [i for i in range(0, 20) if i % 2 == 0]
# print(x)


### strings
# lista = [letter for letter in 'word']
# print(lista)


### converção de temperatures de Celsius para Fahrenheit
celsius = [0, 10, 15, 20, 50, 50, 100]
fahrenheit = [temp * (9/5) + 32 for temp in celsius] 
print(fahrenheit)
