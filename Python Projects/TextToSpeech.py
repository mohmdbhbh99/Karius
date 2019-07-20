import pyttsx3

engine = pyttsx3.init()

x = str(input())
if x == "hello":
    engine.say('Hello mr Karius....')
elif x == "how are you" :
    engine.say('I am fine ..... thank you for your caring about me')

engine.runAndWait()
