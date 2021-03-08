# -- Problema: Alien username
import re 

f = open("usernames.txt", "r")

#print("««« Search »»»")

for linha in f:
  print(linha)
  y = re.search(r'(_|\.)([0-9]+[A-Za-z]{3,})(_|[A-Za-z])$', linha)
  if y:
    """    print("----------inic match------------------")
    print("Y :",y)
    print("Y em String :",y.string)
    print("Span : ",y.span())
    print("Groups : ",y.groups())
    print("Group :",y.group())
    print("-----------fim match-------------------")"""
    print("VALIDO")
  else:
    print("INVALIDO")  

#print("««« Search »»»")
