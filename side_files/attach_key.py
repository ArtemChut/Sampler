import pygame
from pygame.locals import *
from packages import width, height, screen, medium_font
import packages.variables as variables
from packages import background_colour
from .sample import Sample
from .volume_slider import interact_slider, display_slider

pygame.mixer.init()


def waiting_input_display():
    global width, height, screen

    pygame.draw.rect(screen, "lightBlue", (width*0.25, height*0.425, width*0.5,height*0.15),0, 8)
    waiting_input_display = medium_font.render(f"Waiting for a key input..", False, "black")
    screen.blit(waiting_input_display, (width*0.29, height*0.48))

    pygame.display.update()

def remove_sample(sample_chosen):
    found = False
    move_by = 1

    margin = height//20

    if sample_chosen.type == "background":
        variables.background_sample = variables.BackgroundSample()
    else:
        for sample in Sample.samples[:]:
            if sample == sample_chosen:
                Sample.samples.remove(sample_chosen)
                found = True

            if found:
                sample.index -= move_by
                sample.y -= margin

                move_by += 1




def attach_key(sample):

    changing_volume = False
    fade_in = False
    fade_out = False
    slider_type = ""

    started_at = None
    length_seconds = pygame.mixer.Sound(sample.path).get_length()

    while True:
        from .volume_slider import slider_pos # updates every tick inside volume_slider

        if started_at is None: # if fade out hasnt ended
            waiting_input_display()

        pygame.draw.rect(screen, background_colour, (width*0.12,height*0.63-40, width*0.345,height*0.11)) # covering up the slider instead of filling the whole screen

        if started_at is None: # if fade out hasn't ended
            if fade_in:
                display_slider(sample, "fade in")
            elif fade_out:
                display_slider(sample, "fade out")
            else:
                display_slider(sample)


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # allow to see what a sample sounds like by clicking on a spacebar
                if event.key == pygame.K_SPACE:
                    started_at = pygame.time.get_ticks()
                    
                    variables.current_sound = pygame.mixer.Sound(sample.path)
                    variables.current_sound.set_volume(sample.volume)
                    channel = variables.current_sound.play(fade_ms=int(sample.fade_in*1000))

                    return # exit



                keys = pygame.key.get_pressed()
                ctrl_held = keys[pygame.K_LCTRL]

                if ctrl_held and keys[pygame.K_f] and keys[pygame.K_i]:
                    fade_in = True
                    continue
                elif ctrl_held and keys[pygame.K_f] and keys[pygame.K_o]:
                    fade_out = True
                    continue

                if ctrl_held: # wait for whether user also presses "i" or "o"
                    continue
                

                # allow to delete a sample if a user wants to
                elif event.key == pygame.K_DELETE:
                    remove_sample(sample)
                    return

                # close the attack_key tab
                elif event.key == pygame.K_ESCAPE: return 
                elif event.key == pygame.K_RETURN: return


                # don't allow to bind a key to a background sample + don't exit if the fade out affect is still happening
                if sample.type != "background" and started_at is None:
                    # if attaching a sample to a specific key - check that its a letter, not e.g. Enter key
                    try: 
                        if chr(event.key).isalpha():
                            sample.key = chr(event.key)
                        return
                    except: return


            elif event.type == MOUSEBUTTONDOWN: # if let go of a slider
                x,y = pygame.mouse.get_pos()

                # a 20 is the width of a circle inside the slider
                slider_width = (slider_pos-20, slider_pos+20)
                slider_height = (height*0.63-10, height*0.63+10) 

                # if starting to drag a slider
                if slider_height[0] <= y <= slider_height[1] and slider_width[0] <= x <= slider_width[1]:
                    if fade_in: slider_type = "fade in"
                    elif fade_out: slider_type = "fade out"
                    else: slider_type = "volume"


            elif event.type == MOUSEBUTTONUP:
                # resetting the type of slider interaction
                if changing_volume:
                    changing_volume = False
                elif fade_in:
                    fade_in = False
                elif fade_out:
                    fade_out = False
                slider_type = ""

                from side_files import volume_slider as v_s
                v_s.slider_pos = width*0.12+width*0.275//2



        # fade out part
        if started_at is not None:
            seconds_played = (pygame.time.get_ticks() - started_at) / 1000
            
            if length_seconds - seconds_played <= sample.fade_out: # if reached a point when fade-out should start
                channel.fadeout(int(sample.fade_out*1000))
                return



        if started_at is None:
            if slider_type == "volume": # if interacting with a volume slider
                interact_slider(sample)
            elif slider_type == "fade in":
                interact_slider(sample, slider_type)
            elif slider_type == "fade out":
                interact_slider(sample, slider_type)
                