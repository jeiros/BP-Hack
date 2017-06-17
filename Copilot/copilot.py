import lex
import polly
import voice
import audio
import time
import speech_recognition as sr
from text_friend import text_friend
from make_call import make_call

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



    def Bot_Process(self):
        r, type = lex.eyes_closed()
        print(r)
        print(type)
        self.CP_speak(r)
        self.finish = False
        while(not self.finish):
            self.CP_listen()
            r, type = lex.lex_txrx(self.mess_text)
            if(type == 1):
                self.CP_speak(r)
            elif(type == 2):
                self.CP_speak("I can play music for you.")
                self.CP_speak("I can send an automatic message.")
                self.CP_speak("I can call the emergency services.")
                self.CP_speak("What would you like me to do?.")
            elif(type == 0):
                self.CP_speak(r)
                self.finish = 1
            elif(type == 3):
                pass
                #make_call()
            else:
                pass
            lex.stop()

    def run(self):
        if(self.active):
            self.Bot_Process()
        else:
            pass
