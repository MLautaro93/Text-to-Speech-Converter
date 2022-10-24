import tkinter as tk
from gtts import gTTS
from playsound import playsound
import os

# Initializing window
root = tk.Tk()
root.geometry('384x256')
root.resizable(False, False)
root.title('Text to speech converter')
root.config(bg = 'green')

# The Message
message = tk.StringVar()

# Labels and entries
header = tk.Label(text = 'Text to speech converter', font = 'arial 15 bold', fg = 'white', bg = 'black')
header.pack()
enter_text_label = tk.Label(text = 'Enter text:', bg = 'green')
enter_text_label.place(x = 50, y = 75)
text_entry = tk.Entry(width = 35, textvariable = message)
text_entry.place(x = 125, y = 75)

# Functions
def convert(*args):
    speech = gTTS(message.get())
    speech.save('speech.mp3')
    playsound('speech.mp3')
    os.remove('speech.mp3')

def reset():
    message.set('')

def exit():
    root.destroy()

# Buttons
convert_button = tk.Button(text = 'Convert', fg = 'white', bg = 'black', command = convert)
convert_button.place(x = 175, y = 125)
reset_button = tk.Button(text = 'Reset', command = reset)
reset_button.place(x = 150, y = 175)
exit_button = tk.Button(text = 'Exit', command = exit)
exit_button.place(x = 225, y = 175)
root.bind('<Return>', convert)

root.mainloop()