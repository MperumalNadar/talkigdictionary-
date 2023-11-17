from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox

import pyttsx3

engine=pyttsx3.init()# creating instance of engine class
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

# get_close_matches("apple",['app','peach','puppy'],n=3,cutoff=0.6)  example of Syntex
def search():
    data=json.load(open('data.json'))
    word=enderwordentry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        # textarea.insert(END,meaning)
        textarea.delete(1.0,END)
        for item in meaning:
           textarea.insert(END,u'\u2022'+item+'\n\n')
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno('confirm',f'Did you mean {close_match} instead ?')
        if res ==True:
            enderwordentry.delete(0,END)
            enderwordentry.insert(END,close_match)

            meaning=data[close_match]
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

        else:
            messagebox.showerror('Error','The word doest exist ,please double check it.')
            enderwordentry.delete(0,END)
            textarea.delete(1.0,END)
    else:
        messagebox.showinfo('Information ','The Word doest exists')
        enderwordentry.delete(0,END)
        textarea.delete(1.0,END)

def clear():
    enderwordentry.delete(0,END)
    textarea.delete(1.0,END)


def exit():
    res=messagebox.askyesno('confirm','Do you want to exit ?')
    if res==True:
        root.destroy()
    else:
        pass


def wordaudio():
    engine.say(enderwordentry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

# GUI part
# create tk windows
root=Tk()# create tk windows
root.geometry('1000x626+100+30')
root.title('Talking Dictionary created by mPerumal') #title

bgimage=PhotoImage(file='bg.png')
bglable=Label(root,image=bgimage)#window root
bglable.place(x=0,y=0)
root.resizable(False,False)

enderwordlabel=Label(root,text='Enter word',font=('castellar',29,'bold'),foreground='red3',background='whitesmoke')
enderwordlabel.place(x=530,y=20)


enderwordentry=Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=10,relief=GROOVE)
enderwordentry.place(x=510,y=80)


searchimage=PhotoImage(file='search.png')
searchbutton=Button(root,image=searchimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke'
                    ,command=search)
searchbutton.place(x=620,y=150)


micimage=PhotoImage(file='mic.png')
micbutton=Button(root,image=micimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',
                 command=wordaudio)
micbutton.place(x=710,y=153)


meaninglabel=Label(root,text='Meaning',font=('castellar',29,'bold'),foreground='red3',background='whitesmoke')
meaninglabel.place(x=580,y=240)


textarea=Text(root,width=43,height=8,font=('arial',16,'bold'),bd=6,relief=GROOVE)
textarea.place(x=400,y=300)


audiimage=PhotoImage(file='microphone.png')
audiobutton=Button(root,image=audiimage,bd=0,cursor='hand2',bg='whitesmoke',activebackground='whitesmoke',
                   command=meaningaudio)
audiobutton.place(x=530,y=555)


clearimage=PhotoImage(file='clear.png')
clearbutton=Button(root,image=clearimage,bd=0,cursor='hand2',bg='whitesmoke',activebackground='whitesmoke',
                   command=clear)
clearbutton.place(x=660,y=555)

exitimage=PhotoImage(file='exit.png')
exitbutton=Button(root,image=exitimage,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',
                  command=exit)
exitbutton.place(x=800,y=555)

def enter_function(even):  #enter Function
    searchbutton.invoke()

root.bind('<Return>',enter_function )# enter Keybord use panna


root.mainloop() #window wil show loop (ithukullatha yethunalum annanum illana antha windows la theriyathu)
