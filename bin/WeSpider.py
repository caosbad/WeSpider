#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Caos'


from tkFileDialog import *

from Tkinter import *

from tkMessageBox import *

import re

# 显示信息提示框
def show_messagebox(icon, title, message):
    Message().show(icon=icon, title=title, message=message)


_RE_URL = r'^http://weibo.com/\S.'
_RE_URL_WITH_ID = r'^http://weibo.com/u/\d{10}'
_RE_URL_WITH_NAME = r'http://weibo.com/\w{3,}'

# 链接面板
class LinkPanel:

    def __init__(self, master):
        # 初始化链接面板
        linkPanel = Frame(master, bd=2, width=300, padx=20, pady=0, bg=None)

        # 链接面板渲染
        linkPanel.pack()
        # 内部组件的渲染
        self.label = Label(linkPanel, text="输入抓取链接")

        self.label.pack()
        # 设置文档的输入框
        self.textArea = Text(linkPanel, padx=5, pady=5, bd=1, width=80, height=7, wrap=WORD, highlightbackground="gray")
        # 文本全选，暂时屏蔽
        # self.textArea.bind("<Control-Key-a>", self.selectText)
        # self.textArea.bind("<Control-Key-A>", self.selectText)

        self.textArea.pack()

        self.cleanBtn = Button(linkPanel, text="清除链接", padx=50, pady=15, command=self.clean_text_value)

        self.cleanBtn.pack(side=LEFT, padx=50)

        self.checkBtn = Button(linkPanel, text="校验链接", padx=50, pady=15, command=self.check_text_value)

        self.checkBtn.pack(side=RIGHT, padx=50)

        self.urlChecked = FALSE

    # 检查输入的链接地址是否符合规范，包括排重，校验HTTP链接，格式化
    def check_text_value(self):

        urlStr = self.textArea.get(1.0, END)
        if urlStr == u'\n':
            show_messagebox(ERROR, '提示', '链接不允许为空')
            # 动态设置字体颜色
            # self.textArea.tag_add("red", "1.0", END)
            # self.textArea.tag_config("red", background="white", foreground="red")
            return
        else:
            # self.textArea.tag_add("red", "1.0", END)
            # self.textArea.tag_config("red", background="white", foreground="black")
            pass

        rawUrls = urlStr.strip().replace('\n', '').split(';')
        urls = []
        for url in rawUrls:

            # 带有路径u标识的链接，e: weibo.com/u/\d{10}
            idFlag = re.match(_RE_URL_WITH_ID, url)
            nameFlag = re.match(_RE_URL_WITH_NAME, url)
            if idFlag:
                url = idFlag.group()
                urls.append(url+';')
            elif nameFlag:
                url = nameFlag.group()
                urls.append(url+';')
            else:
                pass

        if len(urls)==0:
            show_messagebox(WARNING, '警告', '输入链接不符合规则')

        else:
            # 去重
            urls = reduce(lambda x, y: x if y in x else x+[y], [[],]+urls)
            # 格式化链接
            self.textArea.delete(1.0, END)
            # 保存抓取链接
            self.urls = urls
            # 设置checked字段
            self.urlChecked = TRUE
            self.textArea.insert(INSERT, '\n'.join(urls))

    # 清除文本框中的链接
    def clean_text_value(self):
        self.textArea.delete(0.0, END)
        self.urlChecked = FALSE




# 选择文件保存位置的面板
class FileSelectPanel:


    def __init__(self, master):
        exportPanel = Frame(master)

        exportPanel.pack()

        self.fileEntry = Entry(exportPanel, width=50 )

        self.fileEntry.pack(side=LEFT, padx=0)


        self.selectDirBtn = Button(exportPanel, command=self.select_dir, text="选择保存位置", padx=20, pady=20)

        self.selectDirBtn.pack(side=RIGHT, padx=50)

    # 路径选择面板
    def select_dir(self):
        pass
        self.fileEntry.delete(0, END)

        self.filePath = askdirectory()

        if self.filePath:
            self.fileEntry.insert(0, self.filePath)

    def check_dir(self):
        pass
        # TODO

# 抓取配置面板
class ConfigPanel:
    def __init__(self, master):

        configPanel = Frame(master, bd=2, width=300, padx=20, pady=0, bg=None)

        configPanel.pack()


        self.imageCheckVar = IntVar()
        self.imageCheck = Checkbutton(configPanel, text = "抓取图片", variable = self.imageCheckVar, onvalue = 1, offvalue = 0, height=5, width = 10)
        self.imageCheck.pack(side=RIGHT, padx=130)

        numPanel = Frame(configPanel)
        numPanel.pack(side=LEFT, padx=70)

        self.numLabel = Label(numPanel, text="抓取数量")
        self.numLabel.pack(side=LEFT, padx=10)

        self.numEntry = Entry(numPanel, width=10 )
        self.numEntry.pack(side=LEFT, padx=0)



class LaunchPanel:
    def __init__(self, master):
        launchPanel = Frame(master, bd=2, width=300, padx=20, pady=0, bg=None)

        launchPanel.pack()

        self.launchButton = Button(launchPanel, command=self.check_all_config, text="开始抓取", padx=20, pady=20)

        self.launchButton.pack()


    def check_all_config(self):
        pass

# 初始化主应用面板
mainPanel = Tk(className=" WeSpider ", baseName="WeSpider")


linkPanel = LinkPanel(mainPanel)

configPanel = ConfigPanel(mainPanel)

filePanel = FileSelectPanel(mainPanel)

launchPanel = LaunchPanel(mainPanel)

mainPanel.mainloop()
