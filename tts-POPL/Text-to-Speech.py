#import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

#Initialized window
root = Tk()
root.geometry('300x300')
root.resizable(0,0)
root.config(bg = 'white smoke')
root.title('Text To Speech')

##heading
Label(root, text = 'Text To Speech' , font='arial 20 bold' , bg ='white smoke').place(x=20,y=10)
#Label(root, text ='D' , font ='arial 15 bold', bg = 'white smoke').pack(side = BOTTOM)

#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

##text variable
Msg = StringVar()

#Entry
entry_field = Entry(root,textvariable =Msg, width ='40')
entry_field.place(x=20 , y=100)

#define function

def txt_to_speech():
    os.remove('TTS.mp3')
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('TTS.mp3')
    playsound('TTS.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Buttons
Button(root, text = "Play" , font = 'arial 15 bold', command = txt_to_speech, width =5).place(x=25, y=150)
Button(root,text = 'Exit',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1', width =5).place(x=200,y=250)
Button(root, text = 'Clear', font='arial 15 bold', command = Reset, width =5).place(x= 200, y =150)

#infinite loop to run program
root.mainloop()
