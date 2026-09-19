class BackgroundSample:
    def __init__(self, path="", volume=1.0, name=""):
        self.path = path
        self.volume = volume
        self.type = "background"

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
