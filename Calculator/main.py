
#                The first way.

class Calculator: 
  def performOperation(self,a,b,op):
    if op == "+":
      return a + b 
    elif op == "-":
      return a - b 
    elif op == "*":
      return a * b 
    elif op == "/":
      if b == 0:
        return "Error: Can not divide by zero."
      else:
        return a / b
    
    else:
      return "Error: Operation not supported "
     
calc = Calculator()
print(calc.performOperation(8,2,'/'))
print(calc.performOperation(3,2,'*'))
print(calc.performOperation(1,5,'+'))
print(calc.performOperation(1,4,'-'))
print(calc.performOperation(6,0,'/'))

###########################################################
#                   The second way.

class Calculator():
  def performOperation(self,A,B,operation):
    try:
      if operation == '+':
        return A + B
      elif operation == '-':
        return A - B
      elif operation == '*':
        return A * B
      elif operation == '/':
        return A / B
    except ZeroDivisionError:
      return "Error: Can not divide by zero"
    except TypeError:
      return "Error: Operation not supported"



a = Calculator()
print(a.performOperation(1,2,'/'))
print(a.performOperation(1,2,'*'))
print(a.performOperation(1,2,'+'))
print(a.performOperation(1,2,'-'))
print(a.performOperation(1,0,'/'))
print(a.performOperation(1,'a','/'))
     


