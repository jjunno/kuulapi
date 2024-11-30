import player
import time

if __name__ == "__main__":
    player = player.Player()
    player.play()
    time.sleep(10)
    player.stop()
