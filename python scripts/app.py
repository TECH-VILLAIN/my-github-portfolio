while True:
 try:
  num1 = float(input( "enter first number"))
  operator = input('enter an operator')
  num2 = float(input('enter second number'))
  if operator == "+" :
   print( num1 + num2)
  elif operator == '-':
    print( num1 - num2)
  elif operator == '*':
    print(num1 * num2 )
  elif operator == "/":
    print(num1 / num2)
  else:
    print('invalid operator')
 except ZeroDivisionError:
      print( 'you cant divide by zero')
 except ValueError:
      print("invalid value")


