import lex
import polly

class copilot_obj:

    def __init__(self):
        self.active = False

    def CP_speak(self, message):
        polly.polly_play(message)

    def start(self):
        self.active = True
        #self.CP_speak("Hello, I'm your personal copilot. I will be checking your status during the whole driving session. Enjoy your travel.")

    def run(self):
        if(self.active):
            lex.trigger()
        else:
            pass