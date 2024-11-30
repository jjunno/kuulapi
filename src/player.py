import pygame

class Player:
  def __init__(self):
    self.audiofile = 'src/audiofile.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(self.audiofile)
    
  def play(self):
    print("Playing audio file")
    pygame.mixer.music.play()
    print("Audio file played")
    return True
  
  def stop(self):
    print("Stopping audio file")
    pygame.mixer.music.stop()
    print("Audio file stopped")
    return True
