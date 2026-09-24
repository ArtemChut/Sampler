from pydub import AudioSegment
import math


def volume_to_db(volume):
    if volume <= 0:
        return -120

    return 20 * math.log10(volume)


from tkinter import Tk, filedialog

def pick_location():
    root = Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(
        title="Save your recording",
        defaultextension=".wav",
        filetypes=[("WAV files", "*.wav")]
    )

    root.destroy()
    return file_path


def export_recording():
    from packages.all_samples import AllSamples
    from packages.variables import background_sample

    background = AudioSegment.from_file(background_sample.path)
    background += volume_to_db(background_sample.volume)

    loops_needed = math.ceil(background_sample.time_passed / len(background))

    final_audio = (background * loops_needed)[:background_sample.time_passed]

    fade_in_ms = int((background_sample.fade_in or 0) * 1000)
    fade_out_ms = int((background_sample.fade_out or 0) * 1000)

    if fade_in_ms > 0:
        final_audio = final_audio.fade_in(fade_in_ms)

    if fade_out_ms > 0:
        final_audio = final_audio.fade_out(fade_out_ms)

    for sample in AllSamples.all_played_sample:
        sample_audio = AudioSegment.from_file(sample.path)
        sample_audio += volume_to_db(sample.volume)

        fade_in_ms = int((sample.fade_in or 0) * 1000)
        fade_out_ms = int((sample.fade_out or 0) * 1000)

        if fade_in_ms > 0:
            sample_audio = sample_audio.fade_in(fade_in_ms)

        if fade_out_ms > 0:
            sample_audio = sample_audio.fade_out(fade_out_ms)

        final_audio = final_audio.overlay(sample_audio,position=sample.time_passed)

    save_to_path = pick_location()

    if save_to_path: # if location was actually chosen
        final_audio.export(save_to_path, format="wav")