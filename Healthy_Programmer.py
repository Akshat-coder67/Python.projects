# Importing Required Modules
import pyttsx3
import speech_recognition
import time
import datetime

newVoiceRate = 180

# Important Settings Before The Loop
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[4].id)
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', newVoiceRate)

# Defining Audio Speaking Function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop


def log_now(msg):
    with open("mylogs", "a") as f:
        f.write(f"{msg} {datetime.datetime.now()}\n\n")


init_water = time.time()
init_eyes = time.time()
eyes_secs = 30*60
water_secs = 40*60
while True:
    if time.time() - init_water > water_secs:
        speak(f"Please Drink Water sir, It's {water_secs} seconds, Since you Had drank Water.")
        init_water = time.time()
        log_now("Drank Water at")

    if time.time() - init_eyes > eyes_secs:
        speak(f"Please Exercise Your Eyes sir, It's {eyes_secs} seconds, Since you Had Exercised Your Eyes.")
        init_eyes = time.time()
        log_now("Eyes Exercised at")
