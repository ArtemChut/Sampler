import pygame
from pygame.locals import *
from packages import width, height, screen, medium_font
import packages.variables as variables
from packages.variables import background_colour
from .sample import Sample
from .volume_slider import interact_slider, display_slider

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

    changing_volume = False

    while True:
        from .volume_slider import slider_pos # updates every tick inside volume_slider

        waiting_input_display()

        pygame.draw.rect(screen, background_colour, (width*0.12,height*0.63-20, width*0.275,height*0.08)) # covering up the slider instead of filling the whole screen

        display_slider(sample)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # allow to see what a sample sounds like by clicking on a spacebar
                if event.key == pygame.K_SPACE:
                    variables.current_sound = pygame.mixer.Sound(sample.path)
                    variables.current_sound.play()

                    return

                # allow to delete a sample if a user wants to
                elif event.key == pygame.K_DELETE:
                    remove_sample(sample)
                    return

                # close the attack_key tab
                elif event.key == pygame.K_ESCAPE: return 
                elif event.key == pygame.K_RETURN: return


                if sample.type == "background":
                    # if attaching a sample to a specific key - check that its a letter, not e.g. Enter key
                    try: 
                        if chr(event.key).isalpha():
                            sample.key = chr(event.key)
                        return
                    except: return


            elif event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                # a 20 is the width of a circle inside the slider
                slider_width = (slider_pos-20, slider_pos+20)
                slider_height = (height*0.63-10, height*0.63+10) 

                # if starting to drag a slider
                if slider_height[0] <= y <= slider_height[1] and slider_width[0] <= x <= slider_width[1]:
                    changing_volume = True

            elif event.type == MOUSEBUTTONUP and changing_volume:
                changing_volume = False



        if changing_volume: # if interacting with a volume slider
            interact_slider(sample)
                