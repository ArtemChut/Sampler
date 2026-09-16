import pygame
from pygame.locals import * 
import sys
from .Sample import Sample
from . import screen, big_font, width, height
import variables

pygame.init()
pygame.mixer.init()


pygame.mixer.set_num_channels(120) # allow to play up to 120 samples at a time

def ready():
    global screen

    start_time = pygame.time.get_ticks()
    countdown_length = 3  # seconds
    background_started = False


    while True:
        screen.fill("black")


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                try:
                    if chr(event.key).isalpha():
                        for sample in Sample.samples:
                            if sample.key == chr(event.key):
                                sound = pygame.mixer.Sound(sample.path)
                                sound.play()

                                sample_name_text = big_font.render(sample.name, True, "white")
                                sample_text_rect = sample_name_text.get_rect(center=(width*0.5, height*0.5))
                                
                                screen.blit(sample_name_text, (sample_text_rect))
                except: pass

                if event.key == pygame.K_SPACE:
                    background_started = False
                    background_sound.stop()
                    start_time = pygame.time.get_ticks()



        elapsed = (pygame.time.get_ticks() - start_time) / 1000
        remaining = countdown_length - elapsed

        if remaining > 0:
            time = int(remaining) + 1

            remaining_text = big_font.render(str(time), False, "white")
            screen.blit(remaining_text, (width*0.48, height*0.48))

        elif not background_started: # only play this once
            background_sound = pygame.mixer.Sound(variables.background_sample_path)

            background_sound.play(-1)  # loop indefinitely

            background_started = True
            

        pygame.display.update()
        pygame.time.Clock().tick(60)
