from time import sleep

class Clock: 
  @classmethod 
  def monostable(self, interrupt): 
    print("[Return] To Trigger Clock Pulse")
    while True:
      input()
      interrupt()

  @classmethod
  def bistable(interrupt, frequency=1): 
    while True: 
      interrupt() 
      sleep(frequency)
      
      
