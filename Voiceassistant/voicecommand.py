import pyttsx3  

""" ---------------------Function To Speak------------------ """
def say(text):
    engine.runAndWait()
    engine.say(text)
    print(text,end='')
    engine.runAndWait()
""" ------------------------Callback---------------------------- """

def CallbackMethod(name):
    say("\nHello "+name+"! Im A Voice Assistant")
def method1(operation,callback):
    say("Performing Operation" + operation)
    callback(name)
def help():
    say()

engine = pyttsx3.init()   

say("What is Your Name : ",)
name = input()

method1("\nAnalyzing",CallbackMethod )