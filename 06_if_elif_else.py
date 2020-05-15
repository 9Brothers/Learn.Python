a = 1
b = 1
bol = a == b

if bol:
  a += 10

print(a)

# a = [10, 9, 9, 8, 5, 10, 7]
# index = 3

# if a[index] >= 9:
#   print("Aprovado!")
# elif a[index] >= 7:
#   print("Recuperação")
# else:
#   print("Reprovado!")


b = { 'Adriano': 10, 'Paulo': 7, 'Bruno': 3 }
index = 3

if b[index] >= 9:
  print("Aprovado!")
elif b[index] >= 7:
  print("Recuperação")
else:
  print("Reprovado!")