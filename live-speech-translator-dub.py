# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:57:33 2021

@author: Andrew Cao
"""

import speech_recognition as sr
from translate import Translator
import gtts
from playsound import playsound

r = sr.Recognizer()
print("You get 10 seconds to speak.")
mic = sr.Microphone(device_index=0)

print("Starting Now...")
with mic as source:
   audio = r.listen(source, 10)

result = r.recognize_google(audio)

print("English Input: " + result)

l = "es"

translator= Translator(to_lang=l)

translation = translator.translate(result)

print("Spanish Translation: " + translation)

tts = gtts.gTTS(translation, lang=l)
tts.save("test.mp3")
playsound("test.mp3")
