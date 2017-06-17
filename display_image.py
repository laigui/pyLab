#python tkinter image

from tkinter import *

def main():
    filename = 'logo.gif'
    root = Tk()
    img = PhotoImage(file=filename)
    #img = img.zoom(25)  # with 250, I ended up running out of memory
    img = img.subsample(3)  # mechanically, here it is adjusted to 32 instead of 320
    label = Label(image=img)
    label.image = img  # keep a reference!
    label.pack()
    root.mainloop()

main()