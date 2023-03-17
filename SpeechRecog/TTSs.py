from gtts import gTTS
from pygame import mixer

mixer.init()
import os
  
mytext = input("Say Something : ")
  
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")

mixer.music.load("welcome.mp3")
mixer.music.play()