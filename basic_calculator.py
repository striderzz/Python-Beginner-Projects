def add(a,b):
  answer = a + b
  print(f'{a} + {b} = {answer}')

def sub(a,b):
  answer = a - b
  print(f'{a} - {b} = {answer}')

def mul(a,b):
  answer = a * b
  print(f'{a} * {b} = {answer}') 

def div(a,b):
  answer = a / b
  print(f'{a} / {b} = {answer}')  



while True:
  print("1. Add")
  print("2. Sub")
  print("3. Mul")
  print("4. Div")
  print("5. Exit")



  choice = input("Enter your choice:\n")

  if choice == str(1):
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: "))
    add(a,b)


  elif choice == str(2):
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: "))
    sub(a,b)

  elif choice == str(3):
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: "))
    mul(a,b)  

  elif choice == str(4):
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: "))
    div(a,b) 

  else:
    break 

  

