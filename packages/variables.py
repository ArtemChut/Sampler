class BackgroundSample:
    def __init__(self, path="", volume=1.0, name="", fade_in=0, fade_out=0, length_secs=None, started_at=None, time_passed=None):
        self.path = path
        self.volume = volume
        self.type = "background"
        self.fade_in = fade_in
        self.fade_out = fade_out


        # used later for exporting a file
        self.length_secs = length_secs
        self.started_at = started_at
        self.time_passed = time_passed


        name = ""
        path = self.path[::-1]
        for letter in path:
            if letter != "/":
                name += letter
            else:
                break

        self.name = name[::-1][:-4]
        if len(name) > 21:
            self.name = f"{name[:21]}.."

background_sample = BackgroundSample()

current_sound = None
