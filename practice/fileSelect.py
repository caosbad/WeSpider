#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Caos'


from FileDialog import *

from Tkinter import *


root = Tk()
# 指定master就可以了。
# title属性用来指定标题
fd = SaveFileDialog(root)
# go方法的返回值即为选中的文本路径，如果选择取返回值则为None
print fd.go()
root.mainloop()
# 返回选中的文件名称