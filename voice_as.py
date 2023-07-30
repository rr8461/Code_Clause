import pyttsx3
import wikipedia
voice=pyttsx3.init()
input_1 = input("Search here: ")
result=wikipedia.summary(input_1,sentences=3)
print(result)
voice.say(result)
voice.runAndWait()