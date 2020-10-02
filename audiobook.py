import pyttsx3
import PyPDF2
import time
book=open('The Flight Of The Eagle.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
numOfPages=pdfReader.numPages
print ('Total Pages : '+ str(numOfPages))

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('rate : ' + str(rate))                       #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('Vol : ' +str(volume))                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#engine.say("Hello World!")
#engine.say('My current speaking rate is ' + str(rate))
#engine.runAndWait()
#engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
#engine.save_to_file('Hello World', 'test.mp3')




st=int(input('Enter the start page : '))
stop=int(input('Enter the stop page : '))
engine.say("I will speak this text")
time.sleep(.1)
for i in range(st-1,stop):

    time.sleep(.1)
    page=pdfReader.getPage(i)
    text=page.extractText()
    engine.say(text)
    engine.runAndWait()
    time.sleep(.3)
