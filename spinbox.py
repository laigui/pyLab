# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
def printSpin():
    # ʹ��get()�������õ���ǰ����ʾֵ
    print sb.get()
sb = Spinbox(root,
             from_ = 0,         #��Сֵ
             to = 10,           #���ֵ
             command = printSpin#�ص�����
             )

sb.pack()
root.mainloop()
#ÿ�ε��Spinbox��ťʱ�ͻ����printSpin��������ӡ��Spinbox�ĵ�ǰֵ��