# # -*- coding: utf-8 -*-
# # @Time    : 12/16/2021 10:39 PM
# # @Author  : taltalasuka
# # @File    : test.py
# # @Software: PyCharm
# from tkinter import *
#
# root = Tk()
# root.geometry("300x300")
# s = StringVar()
# a = Entry(root,textvariable=s)
# a.pack()
# i = 0
# s.set(i)
#
# def refresh_data():
#     global i
#     a.delete(0, END)
#     s.set(i)
#     i = i + 1
#     a.update()
#     root.after(1000, refresh_data)
#
# root.after(1000, refresh_data)
# mainloop()






from tkinter import *
from tkinter import messagebox


class Application(Frame):
    '''GUI程序经典写法'''
    def __init__(self,master = None):
        super().__init__(master)
        # super() 表示父类的定义,父类使用 master 参数
        self.master = master
        # 子类定义一个属性接收传递过来的 master 参数
        self.pack()
        # .pack 设置布局管理器
        self.createWidget()
        # 在初始化时,将按钮也实现
        # master传递给父类 Frame 使用后,子类中再定义一个 master 对象

    def createWidget(self):
        '''创建组件'''
        self.btn1 = Button(self)
        # self 为组件容器
        self.btn1["text"] = "Hany love Python."
        # 按钮的内容为 btn1["text"]定义的内容
        self.btn1.pack()
        # 最佳位置
        self.btn1["command"] = self.kuaJiang
        # 响应函数

        self.btnQuit = Button(self,text = "退出",command = root.destroy)
        # 设置退出操作
        self.btnQuit.pack()

    def kuaJiang(self):
        messagebox.showinfo("人艰不拆","继续努力,你是最棒的!")

if __name__ == '__main__':
    root = Tk()
    # 定义主窗口对象
    root.geometry("200x200+200+300")
    # 创建大小
    root.title("GUI 经典写法")

    app = Application(master = root)
    # 传递 master 参数为 主窗口对象
    root.mainloop()

