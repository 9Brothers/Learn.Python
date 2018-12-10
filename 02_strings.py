s = 'Heber\'s café '

######## Indexação ########
# Pega um trecho da string
print(s[6:10])

# Pega os dois últimos caracteres
print(s[-2])

# Pega todos os caracteres menos os dois últimos
print(s[:-2])
###########################



######## Indexação com espaçamentos ########
# Pega os elementos de dois em dois
print(s[::2])

# Inverte a string
print(s[::-1])
###########################



# Strings são imutáveis, ou seja, não dá para alterar os caracteres dela
# porém, é possível concatenar
s = s + ' é muito bom'
print(s)

# Também é possível fazer multiplicação das strings
print(s * 3)
###########################


######## Formatação de strings ########
s = 'string'
print('Temos uma %s auxiliar.' %(s))
print('Imprimindo pontos flutuantes: %1.2f' %(13.144))

a1 = 'string'
a2 = 1234
print('Temos uma %s aqui. Tempos um inteiro aqui: %r' %(a1, a2))

a1 = 'One: {a}, Two: {b}, Three: {c}'.format(a = 1, b = 'two', c = 12.3)
print(a1)
###########################