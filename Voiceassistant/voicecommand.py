import pyttsx3  
import speech_recognition as sr

""" ---------------------Function To Speak------------------ """
def SpeakText(text):
    engine = pyttsx3.init() 
    engine.say(text)
    print(text,end='')
    engine.runAndWait()
""" ------------------------Callback---------------------------- """

def CallbackMethod(name):
    SpeakText("\nHello "+name+"! Im A Voice Assistant")
def method1(operation,callback):
    SpeakText("Performing Operation" + operation)
    callback(name)
def help(name):
    SpeakText("Hello"+name+"!, How Can I Help You")
    print("[1]. $Introduction/n[2]. $Search <about> [3].To Learn")
  
SpeakText("What is Your Name : ",)
name = input()

method1("\nAnalyzing",CallbackMethod )
r = sr.Recognizer()
while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            print("listening....................")
            print("Talking....................")
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ",MyText)
            SpeakText(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Something Went Wrong")
