from alu import ALU
from bus.register import X, Y, SP
from bus.io import IOBus

class _6502: 
  def __init__(self, clock):
    self.clock = clock
    self.ce = True #chip enable 
    self.alu = ALU()

    # registers
    self.X = X() 
    self.Y = Y() 
    self.SP = SP()

    #io 
    self.io = IOBus()
 
