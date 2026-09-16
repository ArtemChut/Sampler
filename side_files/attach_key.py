import pygame
from pygame.locals import *
from packages import width, height, screen, medium_font
import packages.variables as variables
from .Sample import Sample

pygame.mixer.init()


def waiting_input_display():
    global width, height, screen

    pygame.draw.rect(screen, "lightBlue", (width*0.25, height*0.425, width*0.5,height*0.15))
    waiting_input_display = medium_font.render(f"Waiting for a key input..", False, "black")
    screen.blit(waiting_input_display, (width*0.29, height*0.48))

    pygame.display.update()

def remove_sample(sample_chosen):
    found = False
    move_by = 1

    margin = height//20


    for sample in Sample.samples[:]:
        if sample == sample_chosen:
            Sample.samples.remove(sample_chosen)
            found = True

        if found:
            sample.index -= move_by
            sample.y -= margin

            move_by += 1



def attach_key(sample):
    while True:
        waiting_input_display()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # allow to see what a sample sounds like by clicking on a spacebar
                if event.key == pygame.K_SPACE:
                    variables.sound = pygame.mixer.Sound(sample.path)
                    variables.sound.play()
                    return

                # allow to delete a sample if a user wants to
                elif event.key == pygame.K_DELETE:
                    remove_sample(sample)
                    return

                # if attaching a sample to a specific key - check that its a letter, not e.g. Enter key
                try: 
                    if chr(event.key).isalpha():
                        sample.key = chr(event.key)
                    return
                except: return
                
