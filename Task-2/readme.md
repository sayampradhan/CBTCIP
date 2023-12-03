# Audio Recorder using Python
This Python script allows you to record audio using your computer's microphone and save it as a .wav file.

## Prerequisites
- Python 3.x
- Required Python packages: sounddevice, scipy

## Setup
Install the required packages using pip:
```pip install sounddevice scipy```

Clone this repository or download the main.py file.

## Usage
- Run the main.py script in your terminal or preferred Python environment.
- Follow the on-screen instructions.
- Press Ctrl+C to stop recording.
- The recorded audio will be saved in the same directory with a filename based on the timestamp of when the recording started (YYYY-MM-DD_HH-MM-SS.wav).

## Customization
- You can modify the frequency variable to change the recording frequency (currently set to 44100 Hz).
- Adjust the channels and dtype parameters in sd.InputStream() to change the number of audio channels and the data type respectively.

Feel free to explore and modify the code according to your requirements!
