#-*- coding:utf-8 -*-

"""
Text    文本框样例
实现功能有：Ctrl+a全选文本， 竖向滚动条，横向滚动条（不自动换行） 自动缩放

有谁知道全选文本的方法为会要 return 'break' 吗？
http://blog.csdn.net/xxb2008
"""

import Tkinter


class MainFrame(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky="nsew")
        self.createFrame()

    def createFrame(self):
        label_frame_top = Tkinter.LabelFrame(self)
        #label_frame_top.pack()

        label_frame_center = Tkinter.LabelFrame(self)
        label_frame_center.pack(fill="x")

        lfc_field_1 = Tkinter.LabelFrame(label_frame_center)
        lfc_field_1.pack(fill="x")

        self.lfc_field_1_l = Tkinter.Label(lfc_field_1, text="文件路径：", width=10)
        self.lfc_field_1_l.pack(fill="y", expand=0, side=Tkinter.LEFT)

        self.lfc_field_1_b = Tkinter.Button(lfc_field_1, text="清除：", width=10, height=1, command=self.clearText)
        self.lfc_field_1_b.pack(fill="none", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.SE)

        ##########文本框与滚动条
        self.lfc_field_1_t_sv = Tkinter.Scrollbar(lfc_field_1, orient=Tkinter.VERTICAL)  #文本框-竖向滚动条
        self.lfc_field_1_t_sh = Tkinter.Scrollbar(lfc_field_1, orient=Tkinter.HORIZONTAL)  #文本框-横向滚动条

        self.lfc_field_1_t = Tkinter.Text(lfc_field_1, height=15, yscrollcommand=self.lfc_field_1_t_sv.set,
                                          xscrollcommand=self.lfc_field_1_t_sh.set, wrap='none')  #设置滚动条-不换行
        #滚动事件
        self.lfc_field_1_t_sv.config(command=self.lfc_field_1_t.yview)
        self.lfc_field_1_t_sh.config(command=self.lfc_field_1_t.xview)

        #布局
        self.lfc_field_1_t_sv.pack(fill="y", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.N)
        self.lfc_field_1_t_sh.pack(fill="x", expand=0, side=Tkinter.BOTTOM, anchor=Tkinter.N)
        self.lfc_field_1_t.pack(fill="x", expand=1, side=Tkinter.LEFT)

        #绑定事件
        self.lfc_field_1_t.bind("<Control-Key-a>", self.selectText)
        self.lfc_field_1_t.bind("<Control-Key-A>", self.selectText)


        ##########文本框与滚动条end



        label_frame_bottom = Tkinter.LabelFrame(self)
        #label_frame_bottom.pack()

        pass

    #文本全选
    def selectText(self, event):
        self.lfc_field_1_t.tag_add(Tkinter.SEL, "1.0", Tkinter.END)
        #self.lfc_field_1_t.mark_set(Tkinter.INSERT, "1.0")
        #self.lfc_field_1_t.see(Tkinter.INSERT)
        return 'break'  #为什么要return 'break'

    #文本清空
    def clearText(self):
        self.lfc_field_1_t.delete(0.0, Tkinter.END)


def main():
    root = Tkinter.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry('640x360')  #设置了主窗口的初始大小960x540 800x450 640x360

    main_frame = MainFrame(root)
    main_frame.mainloop()


if __name__ == "__main__":
    main()
    pass