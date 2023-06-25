import tkinter

class Program:
    def  __init__(self,title,icon,size,is_resizable = False):
        self.title = title
        self.is_resizable = is_resizable
        self.icon = icon
        self.size = size

    def create_window(self):
        window = tkinter.Tk()


        window.mainloop()

        