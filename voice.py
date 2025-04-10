import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(0) as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    print(r.recognize_google(audio, language='ru-RU'))
