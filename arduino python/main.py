from gtts import gTTS
import speech_recognition as sr #pip install speechRecognition
import datetime
import pyaudio
import pyttsx3
import engineio #to avoid sapi5 error generally faced by pyttsx3
import pyfirmata

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
#print(voices[1].id)

engineio.setProperty('voice', voices[0].id)


def speak(audio):
   engineio.say(audio)
   engineio.runAndWait()

def wishMe():
    speak("Good day sir!")
    speak("I am Chiko. How can I help You?!") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='Us-En')
        speak(f" {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
   wishMe()
   
  
   while True:
    if 1:
 
        query = takeCommand().lower()

        # Logic for executing tasks based on query
    if 6:
       if 'blink' in query:
          board = pyfirmata.Arduino('COM3')
          while True:
            board.digital[13].write(1)
            time.sleep(1)
            board.digital[13].write(0)
            time.sleep(1)
    if 7:
       if 'on or off' in query:
          board = pyfirmata.Arduino('COM3')
          #it = pyfirmata.util.Iterator(board)
          #it.start()

          while True:
            a = board.digital[13].read()
            
            if a == 1:
              board.digital[13].write(0)
              #time.sleep(1)
            else:
              board.digital[13].write(1)
              os.system("pause")
              os.system("CLS")
              #time.sleep(1)
          #board.exit()     