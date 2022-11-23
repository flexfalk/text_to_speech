#string_to_mp3.py
#this an attempt to do text to speech
#by FlexWizard


from gtts import gTTS
import os

class text_to_speech():

    def __init__(self):
        self.language = 'en'

    def text_to_speech(self, mytext : str, filename : str):

        mytext = mytext

        myobj = gTTS(text=mytext, lang=self.language, slow=False)
        myobj.save(filename)


    def read_out_filename(self, fname : str):

        os.system("start " + fname)