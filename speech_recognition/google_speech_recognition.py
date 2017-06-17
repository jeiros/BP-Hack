import speech_recognition as sr
from os import path
def recognize_speech(audio_file)
    r = sr.Recognizer()
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio_file)
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
    return text
