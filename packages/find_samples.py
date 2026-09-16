import pygame

from .Sample import Sample
from . import width, height
from .attach_key import attach_key

def find_samples(x,y, type):
    
    text_height = 40

    if width*0.525 <= x <= width*0.95:
        for sample in Sample.samples:
            if sample.y <= y <= sample.y+text_height and sample.draw:
                if type != "hover":
                    attach_key(sample)
                    break
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    break

