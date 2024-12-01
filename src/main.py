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
    
    time.sleep(3)
    
    main_loop = True
    while main_loop:
      # print("Waiting for button press")
      print(f"Button state is {btn.state}")
      time.sleep(2)
      
      # Player ei vielä ole päälle ja painetaan ekaa kertaa = player päälle
      if not player.state and btn.state:
        led_green.on()
        player.play()
        
      # Player is on and button is pressed again
      if player.state and not btn.state:
        led_green.off()
        main_loop = False
        
    player.stop()
    led_red.off()
    print("Exiting main loop")
