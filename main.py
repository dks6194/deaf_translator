import speech_recognition as sr


R = sr.Recognizer()
with sr.Microphone() as source:
    print("listening...")
    R.pause_threshold = 0.5
    audio = R.listen(source)

try:

    print("recognizing...")
    query = R.recognize_google(audio, language='en-in')
    print(f"User said: {query}\n")
except Exception as e:
    print("say that again please...")

