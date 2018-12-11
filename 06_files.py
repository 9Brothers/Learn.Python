# my_file = open("files/texto.txt")

# text = my_file.read()
# print(text)

# text = my_file.readline()
# print(text)

# my_file.seek(0)
# text = my_file.readline()
# print(text)

my_file = open("files/text.txt")

for line in my_file:
  print(line)