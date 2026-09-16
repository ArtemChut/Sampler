from packages import height, width, screen, medium_font

class Sample:
    samples = []

    def __init__(self, path, index, key=""):
        self.path = path
        self.index = index
        self.name = ""
        margin = height//20
        self.y = height*0.26 + margin*self.index
        self.draw = True
        self.key = key

        # saving only thr name of the sample, not the whole directory
        for letter in self.path[::-1]:
            if letter != "/": self.name += letter
            else: break
        self.name = self.name[::-1][:-4]

        # make the name shorter so that it doesn't go out of bounds
        if len(self.name) > 16:
            self.name = f"{self.name[:17]}.."


        inside = False # checking if the same directory already has been added
        for sample in Sample.samples:
            if self.path == sample.path:
                inside = True
                break
        if not inside:
            Sample.samples.append(self)


    def display(self):
        if self.draw:
            sample_display = medium_font.render(self.name, False, "black")
            screen.blit(sample_display, (width*0.526, self.y))



def find_samples(x,y, type):
    import pygame
    from .attach_key import attach_key
    
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


