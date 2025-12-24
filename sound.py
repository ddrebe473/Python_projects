from playsound import playsound as play
import time
import os
import tkinter as tk
# creating window
window = tk.Tk()

# setting attribute
window.attributes('-fullscreen', True)
window.title("Trolled")


# creating text label to display on window screen
label = tk.Label(window, text="Hello Tkinter!")
label.pack()

window.mainloop()
play('sound.mp3')
        