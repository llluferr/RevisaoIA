import speech_recognition as sr
microfone = sr.Microphone()
reconhecedor = sr.Recognizer()

with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    audio = reconhecedor.listen(mic)
    print("Fale algo...")
    audio = reconhecedor.listen(mic)
    print("Aguarde... efetuando reconhecimento...")
    texto = reconhecedor.recognize_google(audio, language='pt')