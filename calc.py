  # Program to make a simple calculator
def calculate():
  # This function adds two numbers 
  def add(x, y):
    return x + y

  # This function subtracts two numbers 
  def subtract(x, y):
    return x - y

  # This function multiplies two numbers
  def multiply(x, y):
    return x * y

  # This function divides two numbers
  def divide(x, y):
    return x / y

  print("Welcome to Simple Calculator.")
  print("")
  print("Enter the first number")
  print("Enter the second number")
  print("Chose an operation")
  print("")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("")

  num1 = float(input("Enter first number: "))
  print("")

  num2 = float(input("Enter second number: "))
  print("")

  # Take input from the user 
  choice = input("Enter choice(1/2/3/4): ")
  print("")

  if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

  elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

  elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

  elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
  else:
    print("Invalid input")
  
  again()

def again():
    print("")
    print("")
    calc_again = input('''
Do you want to calculate again?

Please type Y for YES or N for NO.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
      print("")
      print("")
      calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
      print("")
      print("")
      print('See you later.')

    else:
      print("")
      print("")
      print("Invalid input")
      again()

# Call calculate() outside of the function
calculate()
again()
