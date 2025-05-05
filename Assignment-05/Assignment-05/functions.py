def E1(x,y):
  if len(x) != len(y):
    return
  z=[0] * len(x)
  for i in range(len(x)):
    z[i] = x[i] + y[i]
  return z

def E2(string):
  x=0
  y=0
  z=0
  for i in string:
    if i.isupper():
      x += 1
    elif i.islower():
      y += 1

  z=abs(y - x)
  return x, y, z

def E3(string):
  x = ""
  for i in string:
    if i.isalnum() or i.isspace():
      x = x + i
  return x


