# a = 1
# b = 1
# bol = b is a 

# if a is 2 :
#   a += 10

# print(a)

notas = [ 10, 9, 8 ,9 ,5, 10, 7 ]

for nota in notas :
  if nota >= 9 :
    print("Aluno nota {n} foi aprovado".format(n = nota))
  elif nota >= 7 :
    print("Aluno nota {n} está de recuperacão".format(n = nota))
  else :
    print("Aluno nota {n} foi reprovado".format(n = nota))