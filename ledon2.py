from Tkinter import *

class pyvcp_led(Canvas):
    " (indicator) a LED "
    " color is on_color when halpin is 1, off_color when halpin is 0 "

    def __init__(self, master,
                 halpin="led", off_color="red", on_color="green", size=20, **kw):
        Canvas.__init__(self, master, width=size, height=size, bd=0)
        self.off_color = off_color
        self.on_color = on_color
        self.oh = self.create_oval(1, 1, size, size)
        self.itemconfig(self.oh, fill=off_color)
        self.halpin = halpin

    def update(self, status):
        if status == 1:
            self.itemconfig(self.oh, fill=self.on_color)
        else:
            self.itemconfig(self.oh, fill=self.off_color)

app = Tk()
d = pyvcp_led(app)
d.pack()
d.update(1)
app.mainloop()
