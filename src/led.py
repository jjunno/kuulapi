from gpiozero import LED

class Led:
  def __init__(self, color):
    self.color = color
    self.gpio = 23
    self.led = LED(self.gpio)
    self.state = False
    
  def on(self):
    print(f"Turning on {self.color} LED")
    self.led.on()
    self.state = True
    return True
    
  def off(self):
    print(f"Turning off {self.color} LED")
    self.led.off()
    self.state = False
    return True
