import player
import led
import time

if __name__ == "__main__":
    player = player.Player()
    led = led.Led()
    led.on()
    time.sleep(3)
    led.off()
    time.sleep(3)
    led.on()
    time.sleep(3)
    led.off()
    # player.play()
    # time.sleep(10)
    # player.stop()
