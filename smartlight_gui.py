# -*- coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog


LARGE_FONT = ("Verdana", 16)


class Application(tk.Tk):
    '''
    多页面测试程序
        界面与逻辑分离
    '''

    def __init__(self):
        super().__init__()

        self.wm_title("智能路灯集控 V1.1       扬州天恒出品")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


class StartPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)

        style = ttk.Style()
        style.configure("BIG.TButton", foreground="black", background="white", font=LARGE_FONT, width=10, padding=18)

        button1 = ttk.Button(self, text="灯具全部开", style="BIG.TButton").grid(row=0, column=0, padx=30, pady=30)
        button2 = ttk.Button(self, text="灯具全部关", style="BIG.TButton").grid(row=0, column=1, padx=30, pady=30)
        button3 = ttk.Button(self, text="灯具状态查询", style="BIG.TButton", command=lambda: root.show_frame(PageOne)).grid(row=0, column=2, padx=30, pady=30)
        button4 = ttk.Button(self, text="节能模式一", style="BIG.TButton").grid(row=1, column=0, padx=30, pady=30)
        button5 = ttk.Button(self, text="节能模式二", style="BIG.TButton").grid(row=1, column=1, padx=30, pady=30)
        button6 = ttk.Button(self, text="节能模式三", style="BIG.TButton").grid(row=1, column=2, padx=30, pady=30)
        button7 = ttk.Button(self, text="环境数据检测", style="BIG.TButton", command=lambda: root.show_frame(PageTwo)).grid(row=2, column=0, padx=30, pady=30)
        button8 = ttk.Button(self, text="系统网络设定", style="BIG.TButton", command=lambda: root.show_frame(PageFour)).grid(row=2, column=1, padx=30, pady=30)
        button9 = ttk.Button(self, text="维修模式", style="BIG.TButton", command=lambda: root.show_frame(PageThree)).grid(row=2, column=2, padx=30, pady=30)


class PageOne(tk.Frame):
    '''灯具状态查询页面'''

    def __init__(self, parent, root):
        super().__init__(parent)

        style = ttk.Style()
        style.configure("Lamp.TButton", foreground="black", background="white", width=6, padding=6)

        button1 = ttk.Button(self, text="灯具1", style="Lamp.TButton").grid(row=0, column=0, padx=10, pady=10)
        progbar1 = ttk.Progressbar(self, orient="horizontal").grid(row=0, column=1)
        button2 = ttk.Button(self, text="灯具2", style="Lamp.TButton").grid(row=1, column=0, padx=10, pady=10)
        progbar2 = ttk.Progressbar(self, orient="horizontal").grid(row=1, column=1)
        button3 = ttk.Button(self, text="灯具3", style="Lamp.TButton").grid(row=2, column=0, padx=10, pady=10)
        progbar3 = ttk.Progressbar(self, orient="horizontal").grid(row=2, column=1)
        button4 = ttk.Button(self, text="灯具4", style="Lamp.TButton").grid(row=3, column=0, padx=10, pady=10)
        progbar4 = ttk.Progressbar(self, orient="horizontal").grid(row=3, column=1)
        button5 = ttk.Button(self, text="灯具5", style="Lamp.TButton").grid(row=4, column=0, padx=10, pady=10)
        progbar5 = ttk.Progressbar(self, orient="horizontal").grid(row=4, column=1)
        button6 = ttk.Button(self, text="灯具6", style="Lamp.TButton").grid(row=5, column=0, padx=10, pady=10)
        progbar6 = ttk.Progressbar(self, orient="horizontal").grid(row=5, column=1)
        button7 = ttk.Button(self, text="灯具7", style="Lamp.TButton").grid(row=6, column=0, padx=10, pady=10)
        progbar7 = ttk.Progressbar(self, orient="horizontal").grid(row=6, column=1)
        button8 = ttk.Button(self, text="灯具8", style="Lamp.TButton").grid(row=7, column=0, padx=10, pady=10)
        progbar8 = ttk.Progressbar(self, orient="horizontal").grid(row=7, column=1)

        button0 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=10)


class PageTwo(tk.Frame):
    '''环境数据检测页面'''

    def __init__(self, parent, root):
        super().__init__(parent)

        button1 = ttk.Button(self, text="灯具1", style="Lamp.TButton").grid(row=0, column=0, padx=10, pady=10)
        button2 = ttk.Button(self, text="灯具2", style="Lamp.TButton").grid(row=1, column=0, padx=10, pady=10)
        button3 = ttk.Button(self, text="灯具3", style="Lamp.TButton").grid(row=2, column=0, padx=10, pady=10)
        button4 = ttk.Button(self, text="灯具4", style="Lamp.TButton").grid(row=3, column=0, padx=10, pady=10)
        button5 = ttk.Button(self, text="灯具5", style="Lamp.TButton").grid(row=4, column=0, padx=10, pady=10)
        button6 = ttk.Button(self, text="灯具6", style="Lamp.TButton").grid(row=5, column=0, padx=10, pady=10)
        button7 = ttk.Button(self, text="灯具7", style="Lamp.TButton").grid(row=6, column=0, padx=10, pady=10)
        button8 = ttk.Button(self, text="灯具8", style="Lamp.TButton").grid(row=7, column=0, padx=10, pady=10)

        button0 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=10)


class PageThree(tk.Frame):
    '''维修模式'''

    def __init__(self, parent, root):
        super().__init__(parent)

        button1 = ttk.Button(self, text="灯具1", style="Lamp.TButton").grid(row=0, column=0, padx=10, pady=10)
        progbar1 = ttk.Scale(self, orient="horizontal").grid(row=0, column=1)
        button2 = ttk.Button(self, text="灯具2", style="Lamp.TButton").grid(row=1, column=0, padx=10, pady=10)
        progbar2 = ttk.Scale(self, orient="horizontal").grid(row=1, column=1)
        button3 = ttk.Button(self, text="灯具3", style="Lamp.TButton").grid(row=2, column=0, padx=10, pady=10)
        progbar3 = ttk.Scale(self, orient="horizontal").grid(row=2, column=1)
        button4 = ttk.Button(self, text="灯具4", style="Lamp.TButton").grid(row=3, column=0, padx=10, pady=10)
        progbar4 = ttk.Scale(self, orient="horizontal").grid(row=3, column=1)
        button5 = ttk.Button(self, text="灯具5", style="Lamp.TButton").grid(row=4, column=0, padx=10, pady=10)
        progbar5 = ttk.Scale(self, orient="horizontal").grid(row=4, column=1)
        button6 = ttk.Button(self, text="灯具6", style="Lamp.TButton").grid(row=5, column=0, padx=10, pady=10)
        progbar6 = ttk.Scale(self, orient="horizontal").grid(row=5, column=1)
        button7 = ttk.Button(self, text="灯具7", style="Lamp.TButton").grid(row=6, column=0, padx=10, pady=10)
        progbar7 = ttk.Scale(self, orient="horizontal").grid(row=6, column=1)
        button8 = ttk.Button(self, text="灯具8", style="Lamp.TButton").grid(row=7, column=0, padx=10, pady=10)
        progbar8 = ttk.Scale(self, orient="horizontal").grid(row=7, column=1)

        button0 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).grid(row=10)


class PageFour(tk.Frame):
    '''系统网络设定'''

    def __init__(self, parent, root):
        super().__init__(parent)

        entry = ttk.Entry(self, width=40)
        entry.pack(side="top", anchor="nw")

        def callback():
            entry.delete(0, "end")  # 清空entry里面的内容
            # 调用filedialog模块的askdirectory()函数去打开文件夹
            filename = filedialog.askopenfilename()
            if filename:
                entry.insert(0, filename)  # 将选择好的文件加入到entry里面

        button1 = ttk.Button(self, text="Open", command=callback)
        button1.pack(side="top", anchor="nw")

        button2 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).pack()


if __name__ == '__main__':
    # 实例化Application
    app = Application()
    app.geometry('800x600')

    # 主消息循环:
    app.mainloop()