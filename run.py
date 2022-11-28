from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import wikipedia
import datetime
import random


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir i am virtual assistent era")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir i am virtual assistent era")
    else:
        speak("good night sir i am virtual assistent era")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if "wikipedia" in self.query:
                speak("searching details....Wait")
                self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                print(results)
                speak(results)
            elif 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")
            elif 'open github' in self.query:
                webbrowser.open("https://www.github.com")
                speak("opening github")
            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")
            elif 'open instagram' in self.query:
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram")
            elif 'open yahoo' in self.query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")

            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail")

            elif 'open snapdeal' in self.query:
                webbrowser.open("https://www.snapdeal.com")
                speak("opening snapdeal")

            elif 'open amazon' in self.query or 'shop online' in self.query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            elif 'open flipkart' in self.query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")
            elif 'open ebay' in self.query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")

            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir ="./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            elif "shutdown" in self.query:
                speak("shutting down")
                os.system('shutdown -s')
            elif "what\'s up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                          'i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)
                ans_take_from_user_how_are_you = self.STT()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                    speak('okey..')
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " For your information archi garg Created me ! I give Lot of Thannks to Her "
                print(ans_m)
                speak(ans_m)
            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am era an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
                print(about)
                speak(about)
            elif "hello" in self.query or "hello era" in self.query:
                hel = "Hello Sir ! How May i Help you.."
                print(hel)
                speak(hel)
            elif "your name" in self.query or "sweat name" in self.query:
                na_me = "Thanks for Asking my name my self ! era"
                print(na_me)
                speak(na_me)
            elif "you feeling" in self.query:
                print("feeling Very sweet after meeting with you")
                speak("feeling Very sweet after meeting with you")
            elif self.query == 'none':
                continue
            elif 'exit' in self.query or 'abort' in self.query or 'stop' in self.query or 'bye' in self.query or 'quit' in self.query:
                ex_exit = 'I feeling very sweet after meeting with you '
                speak(ex_exit)
                exit()
            else:
                temp = self.query.replace(' ', '+')
                g_url = "https://www.google.com/search?q="
                res_g = 'okay'
                print(res_g)
                speak(res_g)
                webbrowser.open(g_url + temp)











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())