import art
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations_dictionary = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply,
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?"))
  for symbol in operations_dictionary:
    print(symbol)
  operation_symbol = input("Pick an operation from the list above?")
  
  
  should_continue = True
  while should_continue:
    num2 = float(input("What's the next number?"))
    calculation = operations_dictionary[operation_symbol]
    answer = calculation(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continuing = input ("Type 'y' to continue calculating, or type 'n' to start a new calculation")
  
    if continuing == "n":
      should_continue = False
      calculator()
      #recursion--> function runs until here and calls itself
    elif continuing == "y":
      should_continue = True
      num1 = answer

calculator()







