import speech_recognition as sr 
import pyttsx3
import os

speech = sr.Recognizer()

try : 
    engine = pyttsx3.init()
except ImportError : 
    print("Requested driver is not found")
except RuntimeError : 
    print("Driver fails to initialize")

voices = engine.getProperty("voices")

for voice in voices : # delete until line 37
    print(voice.id)   # delete until line 37
engine.setProperty("Voice","")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate)
def speak_test_cmd(cmd) : 
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd() : 
    voice_test = ""
    print("Listening...")
    with sr.Microphone() as source : 
        audio = speech.listen(source)
    try :
        voice_test = speech.recognize_google(audio)
    except sr.UnknownValueError : 
        pass
    except sr.RequestError as e : 
        print("Network Error")
    return voice_test

if __name__ == "__main__" : 
    speak_test_cmd("Hello Mr. Long. This is Friday as your assistant")

    while True : 

        voice_note = read_voice_cmd()
        print("cmd : {}".format(voice_note))
        if "hello" in voice_note : 
            speak_test_cmd("Hello Sir. How can I help you")
            continue
        elif "open" in voice_note : 
            os.system("explore C:\\ {}".format(voice_note.replace("Open","")))
            continue  
        elif "bye" in voice_note : 
            speak_test_cmd("Bye Mr. Long. Happy to help you. Have a good day.")
            exit()  
