#Making python speak your desired text
import pyttsx3
node = pyttsx3.init()#invoke function
value=input("Enter your text here")
try:
    node.say(value)
    node.runAndWait()
    node.stop()
    print("Successful")
except:
    print("something went wrong")

#saving the voice to file

import pyttsx3    
def savevoice():
    node=pyttsx3.init()#invoke function
    value=input("Enter your text here")
    try:
        node.say(value)
        node.runAndWait()
        name=input("Enter the name for the voice file")
        node.save_to_file(value,name+".mp3")
        node.stop()
        print("Successful")
    except:
        print("something went wrong")
        
savevoice()

