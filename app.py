import tkinter as tk

import pygame
from pygame.locals import *

from congklakGame import CongklakGUI


def main():
  # # Membuat instance Tkinter untuk aplikasi GUI
  #   root = tk.Tk()

  #   # Membuat objek CongklakGUI yang akan menangani antarmuka pengguna
  #   app = CongklakGUI(root)

  #   # Memulai loop utama Tkinter untuk menampilkan GUI dan menunggu interaksi pengguna
  #   root.mainloop()
  pygame.init()
  screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
  pic = pygame.image.load("asset/tempat2.png")
  screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
  pygame.display.flip()
  while True:
      pygame.event.pump()
      event = pygame.event.wait()
      if event.type == QUIT:
          pygame.display.quit()
      elif event.type == VIDEORESIZE:
          screen = pygame.display.set_mode(
              event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
          screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
          pygame.display.flip()
    
if __name__ == "__main__":
    main()
