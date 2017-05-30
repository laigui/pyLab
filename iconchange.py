#  -*- coding:utf-8 -*-

import sys, os
try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk

from ImageTk import PhotoImage





root = tk.Tk()
w = tk.Label(root, text="Hello, world!")
w.pack()
root.title("My Application")
root.geometry('800x600')
root.wm_title("智能路灯集控 V1.1       扬州天恒出品")
img = PhotoImage(file='logo_32x32.ico')
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()
