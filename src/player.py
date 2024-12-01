import pygame

class Player:
  def __init__(self):
    self.audiofile = 'src/audiofile.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(self.audiofile)
    
  def play(self):
    print("Playing audio file")
    pygame.mixer.music.play()
    return True
  
  def stop(self):
    print("Stopping audio file")
    pygame.mixer.music.stop()
    return True

  def is_playing(self):
    busy = pygame.mixer.music.get_busy()
    return busy
