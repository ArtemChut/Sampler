import pygame
from pygame.locals import * 
import sys
from .sample import Sample
from packages import screen, big_font, width, height
from packages.variables import background_sample


pygame.init()
pygame.mixer.init()


pygame.mixer.set_num_channels(120) # allow to play up to 120 samples at a time

def ready():
    global screen

    start_time = pygame.time.get_ticks()
    countdown_length = 3  # seconds
    background_started = False

    all_sounds = []


    while True:
        screen.fill("black")


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # stopping all the sounds currently playing
                    background_sound.stop()

                    for playing_sample in all_sounds:
                        if playing_sample is not None:
                            playing_sample.stop()

                    import main
                    main.main()
                    return # exit

                try:
                    if chr(event.key).isalpha():
                        for sample in Sample.samples:
                            if sample.key == chr(event.key):
                                sound = pygame.mixer.Sound(sample.path)
                                sound.set_volume(sample.volume)

                                sample_name_text = big_font.render(sample.name, True, "white")
                                sample_text_rect = sample_name_text.get_rect(center=(width*0.5, height*0.5))
                                
                                screen.blit(sample_name_text, (sample_text_rect))

                                all_sounds.append(sound.play())
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
            background_sound = pygame.mixer.Sound(background_sample.path)
            background_sound.set_volume(background_sample.volume)

            background_sound.play(-1)  # loop indefinitely

            background_started = True
            

        pygame.display.update()
        pygame.time.Clock().tick(60)
