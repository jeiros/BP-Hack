import lex
import polly
import voice
import audio
import time

class copilot_obj:

    def __init__(self):
        self.active = False
        lex.stop()

    def CP_listen(self):
        voice_record = voice.record_to_file('./audio_file')
        audio.play_mp3('./audio_file', 1.0)

    def CP_speak(self, message):
        if message is not None:
            print(message)
            polly.polly_play(message)
        time.sleep(0.1)

    def start(self):
        self.active = True
        self.CP_speak("Hello, I'm your personal copilot. I will be checking your status during the whole driving session. Enjoy your travel.")

    def run(self):
        if(self.active):
            r0 = lex.eyes_closed()
            self.CP_speak(r0)
            # yes
            r1 = lex.yes()
            self.CP_speak(r1)
            # call the police
            r2 = lex.call_police()
            self.CP_speak(r2)
        else:
            pass