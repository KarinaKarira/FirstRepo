from tkinter import *
class GrayMessage(Message):
    def __init__(self,parent,text,**kwargs):
        super().__init__(parent,text=text,width=300,relief=SOLID,font=('Algerian',20),bg='light gray',borderwidth=2)
        self.configure(**kwargs)
if __name__ == '__main__':
    root=Tk()
    w=GrayMessage(root,'hello')
    root.mainloop()