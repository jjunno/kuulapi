import pygame

class Player:
  def __init__(self):
    self.audiofile = 'src/audiofile.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(self.audiofile)
    self.state = False
    
  def play(self):
    print("Playing audio file")
    self.state = True
    pygame.mixer.music.play()
    return True
  
  def stop(self):
    print("Stopping audio file")
    self.state = False
    pygame.mixer.music.stop()
    return True
