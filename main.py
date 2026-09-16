import pygame
from pygame.locals import *
import sys

from packages.get_files import get_files
from packages.display import display_all_samples
from packages.__init__ import width, height, screen
from packages.scroll import scroll_through_catalogue
from packages.find_samples import find_samples
from packages.ready import ready
import variables


pygame.init()


def main():
    def find_button(type = "hover"):
        if type == "click":
            x,y = event.pos
        else:
            x,y = pygame.mouse.get_pos()

        if width*0.15 <= x <= width*0.85 and height*0.05 <= y <= height*0.2:
            if type == "hover":
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else: get_files()
        elif width*0.05 <= x <= width*0.475 and height*0.7 <= y <= height*0.9:
            if type == "hover":
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else: ready()
        else:
            find_samples(x,y, type) # allows to bind keys to a specific sample




    while True:
        screen.fill("darkRed")

        # displaying all side sample names + their keybinds + background sample
        display_all_samples()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    find_button("click")

            elif event.type == MOUSEMOTION:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) # changing cursor to a grab cusor
                find_button()

            elif event.type == MOUSEWHEEL:
                scroll_through_catalogue(event.y)

            elif event.type == KEYDOWN:
                # make the sound stop if a user clicks on a spacebar
                if event.key == pygame.K_SPACE:
                    if variables.sound is not None:
                        variables.sound.stop()


        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()
