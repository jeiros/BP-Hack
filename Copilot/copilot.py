import lex
import polly
import voice
import audio
import time
import speech_recognition as sr
from text_friend import text_friend
from make_call import make_call
from find_closest_gas_station import get_closest_gas_station


class copilot_obj:

    def __init__(self):
        self.active = False
        self.trials = 0
        lex.stop()

    def CP_listen(self):
        print("trials {}".format(self.trials))
        try:
            self.voice_record = voice.record_to_file('trial1.wav')
            self.mess_text = lex.recognize_speech(self.voice_record)
        except:
            self.trials += 1
            self.CP_speak("Could not understand you.")

    def CP_speak(self, message):
        if message is not None:
            print(message)
            polly.polly_play(message)
        time.sleep(0.1)

    def start(self):
        self.active = True
        #self.CP_speak("Hello, I'm your personal copilot. I will be checking your status during the whole driving session. Enjoy your travel.")

    def Bot_Process(self):
        r, type, _ = lex.eyes_closed()
        self.CP_speak(r)
        self.finish = False
        while not self.finish:
            self.CP_listen()
            r, type, slot = lex.lex_txrx(self.mess_text)
            if type == 1:
                # HABLA CON POLLY EL MENSAJE
                self.CP_speak(r)
            elif type == 2:
                # READY FOR FULFILMENT
                self.CP_speak("I can play music for you.")
                self.CP_speak("I can send an automatic message.")
                self.CP_speak("I can call the emergency services.")
                self.CP_speak("What would you like me to do?.")
            elif type == 0:
                # ACABA SESION
                self.CP_speak(r)
                lex.stop()
                self.finish = True
            elif type == 3:
                # LLAMA A LA POLI
                make_call()
                self.CP_speak("Called the police. Drive safe, bye.")
                lex.stop()
                self.finish = True
            elif type == 4:
                # MANDA UN MENSAJE
                self.CP_speak(r)
                text_friend(slot)
                self.CP_speak("Text sent to %s" % slot)
                lex.stop()
                self.finish = True
            elif type == 5:
                # GAS STATION ROUTER
                self.CP_speak(r)
                # call al codi de routing
                destination, address_name = get_closest_gas_station()
                self.CP_speak("The nearest gast station is %s." % address_name)
                self.CP_speak("Routing you to %s " % destination)
                self.CP_speak("Drive safe, bye.")
                lex.stop()
                self.finish = True
            elif self.trials > 3:
                # SI MAS DE TRES INTENTOS, SALIR
                self.CP_speak("I could not understand you for three attempts. Drive safe, bye.")
                lex.stop()
                self.finish = True
            else:
                pass
        lex.stop()

    def run(self):
        if(self.active):
            self.Bot_Process()
        else:
            pass
