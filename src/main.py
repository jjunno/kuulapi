import player
import led
import button
import time

if __name__ == "__main__":
  # First thing is to turn on red LED to indicate that the system is booting up
    led_red = led.Led(23, "red")
    led_red.on()
    
    led_green = led.Led(26, "green")
    
    btn = button.Button(17)
    player = player.Player()
    
    main_loop = True
    while main_loop:
      print(f"Button state is {btn.state}")
      time.sleep(1)
      
      # Button has not been pressed, player is not busy
      
      # Player is off and button is pressed
      if not player.is_playing() and btn.state:
        led_green.on()
        player.play()
        
      # Player is on and button is pressed again
      if player.is_playing() and not btn.state:
        led_green.off()
        player.stop()
      
      # Player is busy, continue
      if player.is_playing():
        continue
      
      # Button has been pressed but player is not busy, the song has ended
      if btn.state:
        led_green.off()
        
    player.stop()
    led_red.off()
    print("Exiting main loop")
