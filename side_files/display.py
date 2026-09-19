from packages import pygame, screen, width, height, big_font, medium_font, small_font
import packages.variables as variables
from .sample import Sample

def display_all_samples():
        
    # button that allows a user to upload files
    pygame.draw.rect(screen, "purple", (width*0.15,height*0.05, width*0.7,height*0.15))
    choose_file_text = "Select a background sample" if variables.background_sample.path == "" else "Select samples for the keyboard"
    choose_file_display = big_font.render(choose_file_text, False, "black")
    screen.blit(choose_file_display, (width*0.175, height*0.095))

    # the name of a background sample added
    pygame.draw.rect(screen, "red", (width*0.05,height*0.25, width*0.425,height*0.3))
    background_sample_display = medium_font.render(f"Background sample is:\n\n{variables.background_sample.name}", False, "black")
    screen.blit(background_sample_display, (width*0.06, height*0.26))

    # the names of all the side samples added + their keybinds
    pygame.draw.rect(screen, "red", (width*0.525,height*0.25, width*0.425,height*0.06+40*len(Sample.samples)))
    side_samples_display = medium_font.render(f"Side samples are:", False, "black")
    screen.blit(side_samples_display, (width*0.526, height*0.26))


    if Sample.samples:
        for sample in Sample.samples:
            sample.display()
            if sample.key != "" and sample.draw:
                sample_keybind = small_font.render(f"keybind={sample.key}", False, "black")
                screen.blit(sample_keybind, (width*0.85, sample.y+12))


    pygame.draw.rect(screen, "green", (width*0.05,height*0.7, width*0.425,height*0.2),0, 16)
    ready_button = big_font.render("Ready", False, "black")
    screen.blit(ready_button, (width*0.2,height*0.77))
