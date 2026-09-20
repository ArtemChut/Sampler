from .sample import Sample
from packages import height
from .instructions_menu import Instruction

def scroll_through_catalogue(direction, type):
    global height

    margin = 0 if direction == 1 else height//20 # for some reason they appear differently depending on whether you scroll up or down

    if type == "side samples":

        for side_sample in Sample.samples:
            # make a sample name disappear if it goes out of bounds
            if side_sample.y <= height*0.26+margin:
                side_sample.visible = False
            else:
                side_sample.visible = True


            side_sample.y += 20*direction
            
    else:

        for instruction in Instruction.all_instructions:
            if (instruction.y <= height*0.11+16+margin-32) or (instruction.y >= height*0.8-16+margin-32): # 32 is a constant
                instruction.visible = False
            else:
                instruction.visible = True

            instruction.y += 20*direction
