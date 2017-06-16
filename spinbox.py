# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
def printSpin():
    # 使用get()方法来得到当前的显示值
    print sb.get()
sb = Spinbox(root,
             from_ = 0,         #最小值
             to = 10,           #最大值
             command = printSpin#回调函数
             )

sb.pack()
root.mainloop()
#每次点击Spinbox按钮时就会调用printSpin函数，打印出Spinbox的当前值。