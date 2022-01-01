class IOBus():
  def __init__(self): 
    self.bus = [0] * 0x7fff #init a empty 16 bit address space

if __name__ == "__main__":
  bus = AddressBus()
