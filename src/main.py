import player
import led
import button
import time

if __name__ == "__main__":
  # First thing is to turn on red LED to indicate that the system is booting up
    led_red = led.Led(23, "red")
    led_red.on()
    
    btn = button.Button(17)
    player = player.Player()
    
    time.sleep(3)
    
    main_loop = True
    while main_loop:
      print("Waiting for button press")
      print(f"Button state is {btn.state}")
      time.sleep(2)
      
      if not player.state and btn.state:
        player.play()
      else:
        player.stop()
        main_loop = False
      
    player.stop()
    led_red.off()
    print("Exiting main loop")
