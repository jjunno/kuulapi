import player
import led
import time

if __name__ == "__main__":
  # First thing is to turn on red LED to indicate that the system is booting up
    led_red = led.Led(23, "red")
    led_red.on()
    player = player.Player()
    time.sleep(10)
    led_red.off()
    # player.play()
    # time.sleep(10)
    # player.stop()
