class Register:
  def __init__(self):
    self.value
  
  def set_value(self, value):
    assert(value <= 0xff)
    self.value = value

class X(Register): 
  def __init__(self):
    super().__init__()

class Y(Register): 
  def __init__(self):
    super().__init__()

class SP(Register):
  def __init__(self): 
    super().__init__()

