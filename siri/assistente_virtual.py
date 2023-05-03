import os

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

microfone = sr.Microphone()
reconhecedor = sr.Recognizer()
with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    audio = gTTS("Deseja ouvir uma musica?", lang='pt')
    audio.save('msg.mp3')
    playsound('msg.mp3')
    print("Deseja ouvir uma musica?")
    reconhecedor.listen(mic)
    print("reconhecendo...")
    texto= reconhecedor.recognize_google(audio, language='pt')
    print(texto)
    lista = ['OK', 'PODE SER', 'SIM', 'TUDO BEM', 'QUERO']
    if texto.upper() in lista:
        audio = gTTS("Ok, abrindo a musica...", lang='pt')
        audio.save('msg.mp3')
        playsound('msg.mp3')
        print("Ok, abrindo a musica...")
        os.system('musicaboa.mp3')
    else:
        audio = gTTS("Tudo bem, ate logo!")
        audio.save('msg.mp3')
        playsound('msg.mp3')
        print("Tudo, ate logo")