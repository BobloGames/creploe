import sys

import pygame

CreplVersion = "Ver 0.0.1"

ON = 0

class OE:
  def __init__(self):
    pygame.init()
    pygame.display.init()
    pygame.mixer.init()
    self.screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Crepl OE Pygame " + str(pygame.version.ver) + " Crepl OE " + CreplVersion)
    pygame.display.set_icon(pygame.image.load('Icon.ico'))
  def RunOE(self):
    global ON

    # INIT the sounds.

    pygame.mixer.music.load('Startup.mp3')

    pygame.mixer.music.play()
    while True:
      self.screen.fill((0, 128, 0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_COMMA:
            if ON == 0:
              print("Cannot go down, reached limit.")
            else:
              ON -= 1
          elif event.key == pygame.K_PERIOD:
            ON += 1
          else:
            print("Unknown key.")
      pygame.display.update()

if __name__ == "__main__":
  AI = OE()
  AI.RunOE()