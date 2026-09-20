from packages import screen, pygame, width, height, background_colour, medium_font, small_font
from . import scroll
from pygame.locals import *
import sys


class Instruction:
    all_instructions = []

    def __init__(self, text, key, index, visible=True):
        self.text = text
        self.key = key
        self.index = index
        self.visible = visible

        text_height = height*0.1+10
        self.y = height*0.11+self.index*text_height+16

        if self.y >= height*0.8: # don't allow to g out of bounds
            self.visible = False

        Instruction.all_instructions.append(self)


    def display_instruction(self):

        if self.visible:
            # description
            pygame.draw.rect(screen, "magenta", (width*0.11,self.y, width*0.78,height*0.1),0, 8)
            sample_description = medium_font.render(self.text, False, "black")
            screen.blit(sample_description, (width*0.115, self.y+6))

            # icon
            centered_rect = pygame.Rect(width*0.81, self.y+8, 60,60)

            pygame.draw.rect(screen, "linen", (width*0.81, self.y+8, 60,60),0, 4)
            icon_text = small_font.render(self.key, False, "black")
            screen.blit(icon_text, icon_text.get_rect(center=centered_rect.center)) # centering text
        


instructions = (("Press Esc when in an instructions/ready \nmenu to go back to the main menu", "Esc"),
                ("Scroll through all the instructions by \nusing a mousewheel", " Mouse \n wheel"),
                ("Press spacebar after clicking on any \nsample name to play it", "Space\nbar"),
                ("If clicked a spacebar, click it again to \nstop it from playing", "Space\nbar"),
                ("Scroll through the side samples list by \nusing a mousewheel", " Mouse \n wheel"),
                ("Change fade-in length by pressing Ctrl+\nf+i after clicking on any loaded sample", "Ctrl\n f\n i"),
                ("Change fade-out length by pressing Ctrl+\nf+i after clicking on any loaded sample", "Ctrl\n f\n o"),
                ("Re-start everything when in a ready menu \nby clicking on a spacebar", "Space \nbar"))

i = 0
for instr, icon in instructions:
    Instruction(instr, icon, i).display_instruction()
    i += 1

def display_instructions():
    global instructions

    pygame.draw.rect(screen, "maroon", (width*0.1,height*0.1, width*0.8,height*0.8),0, 24)

    for instruction in Instruction.all_instructions:
        instruction.display_instruction()




def main():
    while True:
        screen.fill(background_colour)

        display_instructions()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    import main
                    main.main()
                    return

            elif event.type == MOUSEWHEEL:
                scroll.scroll_through_catalogue(event.y, "instructions")

        
        pygame.display.update()
        pygame.time.Clock().tick(60)
    