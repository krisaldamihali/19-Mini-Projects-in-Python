
class Pencil():
  def __init__(self, brand, color, thickness):
    self.brand = brand
    self.color = color
    self.thickness = thickness
    
  def GetBrand(self):
    return self.brand

  def SetBrand(self, brand):
    self.brand = brand

  def GetColor(self):
    return self.color

  def SetColor(self, color):  
    self.color = color

  def GetThickness(self):
    return self.thickness
    
  def SetThickness(self, thickness):
    self.thickness = thickness
    
a = Pencil('MONTEGRAPPA','Red',12)
print(a.GetBrand())
print(a.GetColor())
print(a.GetThickness())