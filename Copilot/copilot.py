import lex
import polly
import voice
import audio
import time
import speech_recognition as sr

class copilot_obj:

    def __init__(self):
        self.active = False
        lex.stop()

    def CP_listen(self):
        self.voice_record = voice.record_to_file('trial1.wav')
        self.mess_text = lex.recognize_speech(self.voice_record)

    def CP_speak(self, message):
        if message is not None:
            print(message)
            polly.polly_play(message)
        time.sleep(0.1)

    def start(self):
        self.active = True
        #self.CP_speak("Hello, I'm your personal copilot. I will be checking your status during the whole driving session. Enjoy your travel.")

    def run(self):
        if(self.active):
            r0 = lex.eyes_closed()
            self.CP_speak(r0)

            self.CP_listen()
            r1 = lex.lex_txrx(self.mess_text)
            self.CP_speak(r1)

            self.CP_listen()
            r1 = lex.lex_txrx(self.mess_text)
            self.CP_speak(r1)

        else:
            pass