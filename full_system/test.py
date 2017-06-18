from blinks import *

import cv2
import dlib
if conf.is_raspi:
    import picamera
from utils import *
from train_face import *
import Copilot.copilot as copi
alicia = copi.copilot_obj()
alicia.start('TUputamadre')
alicia.run()

import pyaudio
import wave
import sys

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "./output.wav"

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk, input_device_index=7)

print "* recording"
all = []
for i in range(0, RATE / chunk * RECORD_SECONDS):
    data = stream.read(chunk)
    all.append(data)
print "* done recording"

stream.close()
p.terminate()

 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(all))
waveFile.close()