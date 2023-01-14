import re

def password(passo):
   uppercase = re.compile(r'[A-Z]')
   if not uppercase.search(passo):
      return False
   lowercase = re.compile(r'[a-z].')
   if not lowercase.search(passo):
      return False
   digit = re.compile(r'[0-9].')
   if not digit.search(passo):
      return False
   if len(passo) < 8:
      return False
   else:
      return True
   
passo = input("enter password: ")

if password(passo):
   print("nice password")
else:
   print("weak password")


   
   
    
