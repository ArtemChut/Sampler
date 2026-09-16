from .Sample import Sample
from packages import height

def scroll_through_catalogue(direction):
    global height


    margin = 0 if direction == 1 else height//20 # for some reason they appear differently depending on whether you scroll up or down

    for side_sample in Sample.samples:
        # make a sample name disappear if it goes out of bounds
        if side_sample.y <= height*0.26+margin:
            side_sample.draw = False
        else:
            side_sample.draw = True


        side_sample.y += 20*direction

    
