import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import numpy as np

# Constants
frequency = 44100


def record_audio():
    frames = []

    print("Recording...")
    try:
        with sd.InputStream(samplerate=frequency, channels=2, dtype='int16') as stream:
            while True:
                recording = stream.read(1024)[0]
                frames.append(recording)
    except KeyboardInterrupt:
        sd.stop()
        print("Recoding Stopped!!")

    # Concatenate recorded frames
    recording = np.concatenate(frames, axis=0)

    # Save recording to file
    date_time = datetime.now()
    file_name = date_time.strftime("%Y-%m-%d_%H-%M-%S")
    write(file_name + ".wav", frequency, recording)

# Call the function
record_audio()
