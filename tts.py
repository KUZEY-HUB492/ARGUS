import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 175)

def konus(metin):
    engine.say(metin)
    engine.runAndWait()