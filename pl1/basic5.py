import re


print("Split de uma linha por virgulas")

inputFromUser = input(">> ")

while inputFromUser != "":
  lista = re.split(r',', inputFromUser, maxsplit=1, flags=3)
  for i in lista:
    print(i) 
  inputFromUser = input(">> ")

  
  
