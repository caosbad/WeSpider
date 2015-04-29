#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Caos'


from tkFileDialog import *

from Tkinter import *




# 链接面板
class LinkPanel:

    def __init__(self, master):
        # 初始化链接面板
        linkPanel = Frame(master, bd=2, width=300, padx=20, pady=15, bg=None)

        # 链接面板渲染
        linkPanel.pack()

        self.lable = Label(linkPanel, text="抓取链接")

        self.lable.pack()

        self.textArea = Text(linkPanel, padx=5, pady=5, bd=1, width=80, height=7, wrap=WORD )

        self.textArea.pack()

        self.cleanBtn = Button(linkPanel, text="清除链接")

        self.cleanBtn.pack(side=LEFT, )

        self.checkBtn = Button(linkPanel, text="校验链接" )

        self.checkBtn.pack(side=RIGHT)


    def check_text_value(self):
        pass


    def clean_text_value(self):
        pass




class FileSelectPanel:


    def __init__(self, master):
        exportPanel = Frame(master)

        exportPanel.pack()

        self.fileEntry = Entry(exportPanel, width=40)

        self.fileEntry.pack(side=LEFT)



        self.selectDirBtn = Button(exportPanel, command=self.select_dir, text="选择保存位置", padx=10, pady=10)

        self.selectDirBtn.pack(side=RIGHT)


    def select_dir(self):
        pass
        self.fileEntry.delete(0, END)

        self.filePath = askdirectory()

        if self.filePath:
            self.fileEntry.insert(0, self.filePath)

    def check_dir(self):
        pass
        # TODO


# 初始化主应用面板
mainPanel = Tk(className=" WeSpider ", baseName="WeSpider")


linkPanel = LinkPanel(mainPanel)

filePanel = FileSelectPanel(mainPanel)

mainPanel.mainloop()
