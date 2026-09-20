import pygame
from pygame.locals import * 
import sys
from .sample import Sample
from packages import screen, big_font, width, height
from packages.variables import background_sample


pygame.init()
pygame.mixer.init()


pygame.mixer.set_num_channels(120) # allow to play up to 120 samples at a time


class Sound:
    all_sounds = []

    def __init__(self, channel, started_at, length, fade_out, type="side sample"):
        self.channel = channel
        self.started_at = started_at
        self.length = length
        self.fade_out = fade_out

        self.type = type

        self.fading_out = False

        Sound.all_sounds.append(self)



def ready():
    global screen

    start_time = pygame.time.get_ticks()
    countdown_length = 3  # seconds
    background_started = False
    started_at = None


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

                    for playing_sample in Sound.all_sounds:
                        if playing_sample.channel is not None:
                            playing_sample.channel.stop()

                    import main
                    main.main()
                    return # exit

                try:
                    if chr(event.key).isalpha():
                        for sample in Sample.samples:
                            if sample.key == chr(event.key):
                                started_at = pygame.time.get_ticks()
                                length_seconds = pygame.mixer.Sound(sample.path).get_length()

                                sound = pygame.mixer.Sound(sample.path)
                                sound.set_volume(sample.volume)

                                channel = sound.play(fade_ms=int(sample.fade_in*1000))

                                Sound(channel, started_at, length_seconds, sample.fade_out)


                                sample_name_text = big_font.render(sample.name, True, "white")
                                sample_text_rect = sample_name_text.get_rect(center=(width*0.5, height*0.5))
                                
                                screen.blit(sample_name_text, (sample_text_rect))
                except: pass

                if event.key == pygame.K_SPACE:
                    background_started = False
                    background_sound.stop()
                    start_time = pygame.time.get_ticks()



        # fade out part
        for sound_obj in Sound.all_sounds[:]:
            if not sound_obj.channel.get_busy(): # if the sample has finished
                if sound_obj.type != "side sample":
                    background_started = False # allow to re-add it back in later

                Sound.all_sounds.remove(sound_obj)
                continue

            seconds_played = (pygame.time.get_ticks() - sound_obj.started_at) / 1000
            
            if sound_obj.length - seconds_played <= sound_obj.fade_out and not sound_obj.fading_out: # if reached a point when fade-out should start
                sound_obj.channel.fadeout(int(sound_obj.fade_out*1000))
                sound_obj.fading_out = True 



        elapsed = (pygame.time.get_ticks() - start_time) / 1000
        remaining = countdown_length - elapsed

        if remaining > 0:
            time = int(remaining) + 1

            remaining_text = big_font.render(str(time), False, "white")
            screen.blit(remaining_text, (width*0.48, height*0.48))

        elif not background_started: # play infinitely after it stops
            started_at = pygame.time.get_ticks()
            length_seconds = pygame.mixer.Sound(background_sample.path).get_length()

            background_sound = pygame.mixer.Sound(background_sample.path)
            background_sound.set_volume(background_sample.volume)

            channel = background_sound.play(fade_ms=int(background_sample.fade_in * 1000))  # loop forever

            Sound(channel, started_at, length_seconds, background_sample.fade_out, "background")


            background_started = True
            

        pygame.display.update()
        pygame.time.Clock().tick(60)
