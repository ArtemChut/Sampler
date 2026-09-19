from packages import pygame, screen, medium_font, width, height

slider_pos = width*0.12+width*0.275//2
def display_slider(sample):
    global slider_pos

    change_voume_text = medium_font.render("Change volume", False, "black")
    screen.blit(change_voume_text, (width*0.15, height*0.575))
    pygame.draw.rect(screen, "yellow", (width*0.15,height*0.63, width*0.215,height*0.008),0, 8)

    pygame.draw.circle(screen, "green", (slider_pos,height*0.63+2), 10)

    # displaying current volume
    volume_text = medium_font.render(f"{round(sample.volume*100)}%", False, "black")
    screen.blit(volume_text, (width*0.24, height*0.65))


orig_center_x = width*0.12+width*0.275//2-10
def interact_slider(sample):
    global slider_pos
    x,y = pygame.mouse.get_pos()

    orig_x = width*0.12+width*0.275//2*sample.volume
    if 0 <= sample.volume-(orig_x-x)*0.01 <= 2:
        sample.volume -= (orig_x-x)*0.01

        slider_pos -= (orig_x-x)*0.9