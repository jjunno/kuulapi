from gpiozero import LED

class Led:
  def __init__(self):
    self.gpio = 23
    self.led = LED(self.gpio)
    self.state = False
    
  def on(self):
    print("Turning on LED")
    self.led.on()
    self.state = True
    return True
    
  def off(self):
    print("Turning off LED")
    self.led.off()
    self.state = False
    return True
