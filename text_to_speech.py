from gtts import gTTS 
import os  
mytext = 'messi is better than ronaldo'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("mpg321 sound.mp3") 