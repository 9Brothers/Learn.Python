# def primeira_funcao():
#   """
#   Printa "Olá mundo"
#   """
#   print('primeira função')  

# primeira_funcao()


# l = [i for i in range(1, 6)]

# print(len(l))


# def somar(num1, num2):
#   return num1 + num2

# soma = somar(3,4)

# print(soma)


def primo(num):
  """
  Método para checar se o número é primo
  """

  for n in range(2, num):
    if num % n == 0:
      print('Não é primo')
      break
  else:
    print('Primo')


primo(7)