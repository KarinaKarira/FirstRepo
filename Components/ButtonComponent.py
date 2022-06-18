from tkinter import *


class WhiteButton(Button):
    def __init__(self,parent, text,command, **kwargs):
        super().__init__(parent, text=text,command=command, width=20, height=2,activebackground='gray',font=('',10,'bold'),activeforeground='white',relief=RAISED,borderwidth=5)
        self.configure(**kwargs)

class GrayButton(Button):
    def __init__(self,parent, text,command, **kwargs):
        super().__init__(parent, text=text,command=command, width=20, height=2,bg='light gray',font=('',10,'bold'),activebackground='white',relief=RAISED,borderwidth=5, activeforeground='black')
        self.configure(**kwargs)

