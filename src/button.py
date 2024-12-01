import RPi.GPIO as GPIO

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

class Button:
  def __init__(self, gpio):
    self.gpio = int(gpio)
    self.state = False
    
    # Setup GPIO for to button
    GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    # Listen to events on GPIO PIN
    GPIO.add_event_detect(self.gpio, GPIO.RISING, callback=self.onPressm, bouncetime=200)

    
  def onPress(self):
    print(f"Button {self.gpio} pressed")
    # Toggle state
    self.state = not self.state
    return True
