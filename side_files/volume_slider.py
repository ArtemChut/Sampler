from packages import pygame, screen, medium_font, width, height

slider_pos = width*0.12+width*0.275//2
def display_slider(sample, slider_type="volume"):
    global slider_pos

    if slider_type == "fade in" or slider_type == "fade out": 
        length_seconds = pygame.mixer.Sound(sample.path).get_length()

        if slider_type == "fade in":
            slider_pos = width*0.15+20 + sample.fade_in*(1020*0.215-40)/length_seconds
        else:
            slider_pos = width*0.15+20 + sample.fade_out*(1020*0.215-40)/length_seconds


    if slider_type == "volume":
        display_type = "Change volume"
        measure = f"{round(sample.volume*100)}%"
    elif slider_type == "fade in":
        display_type = "Change fade-in len"
        measure = f"{round(sample.fade_in, 1)}s"
    elif slider_type == "fade out":
        display_type = "Change fade-out len"
        measure = f"{round(sample.fade_out, 1)}s"

    change_voume_text = medium_font.render(display_type, False, "black")
    screen.blit(change_voume_text, (width*0.15, height*0.575))
    pygame.draw.rect(screen, "yellow", (width*0.15,height*0.63, width*0.215,height*0.008),0, 8)

    pygame.draw.circle(screen, "green", (slider_pos,height*0.63+2), 10)

    # displaying current volume/fade in/out
    volume_text = medium_font.render(measure, False, "black")
    screen.blit(volume_text, (width*0.24, height*0.65))


orig_x = width*0.12+width*0.275//2-10
def interact_slider(sample, type="volume"):
    global slider_pos
    x,y = pygame.mouse.get_pos()

    if type == "volume":
        orig_x = width*0.12+width*0.275//2*sample.volume
        if 0 <= sample.volume-(orig_x-x)*0.01 <= 2:
            sample.volume -= (orig_x-x)*0.01
            
            slider_pos -= (orig_x-x)*0.9

    elif type == "fade in" or type == "fade out":
        orig_x = width*0.15+20

        length_seconds = pygame.mixer.Sound(sample.path).get_length()

        if type == "fade in":
            if 0 <= (x-orig_x)*0.1 <= length_seconds-sample.fade_out:
                sample.fade_in = (x-orig_x)*0.1
        else:
            if 0 <= (x-orig_x)*0.1 <= length_seconds-sample.fade_in:
                sample.fade_out = (x-orig_x)*0.1

