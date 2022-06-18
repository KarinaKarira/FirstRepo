from tkinter import *
from Components import *
from PIL import Image,ImageTk

class BackgroundPage:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('Images\studentopedia_3.ico')
        self.root.title("Studentopedia")
        self.f=Frame(self.root,width=1000,height=700,bg='light gray')
        #width=1600,height=900
        self.f.pack()

        self.raw_image=Image.open('Images\Student_info.png')
        self.raw_image=self.raw_image.resize((1000,700))
        #(1600,900)
        self.img=ImageTk.PhotoImage(self.raw_image)
        self.img_lab=Label(self.f,image=self.img)
        # self.login_label.image = self.login_img
        self.img_lab.ref=self.img
        self.img_lab.pack()
        self.img_lab.pack_propagate(0)

        self.msg=Message(self.img_lab,text='VESIT CMPN',bg='light gray',width=300,font=('Algerian',20),relief=SOLID,borderwidth=2)
        self.msg.pack(side=TOP,pady=50)
        # self.msg.place(x=370,y=100)
        self.footer=Label(self.img_lab,text="Studentopedia-one stop for all management queries!!",bg='gray',height=1)

        #***footer not covering the entire screen***

        self.footer.pack(side=BOTTOM,fill=X)
        # self.footer.grid(x=0,y=0)
        self.footer.tkraise()
        self.f.pack_propagate(0)

if __name__ == '__main__':
    root = Tk()
    b = BackgroundPage(root)
    root.mainloop()