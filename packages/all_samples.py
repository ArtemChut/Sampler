# stores ALL the side samples that have been played by a user when pressing a key attached to it

class AllSamples:
    all_played_sample = []

    def __init__(self, path="", volume=1.0, fade_in=0, fade_out=0, length_secs=None, started_at=None, time_passed=None):
        self.path = path
        self.volume = volume
        self.fade_in = fade_in
        self.fade_out = fade_out


        self.length_secs = length_secs
        self.started_at = started_at
        self.time_passed = time_passed

        AllSamples.all_played_sample.append(self)
