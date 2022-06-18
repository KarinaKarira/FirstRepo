from tkinter import *
from BackgroundPage import *
from Components.ButtonComponent import WhiteButton
from LoginWindowPage import *


class MainPage(BackgroundPage):
    def __init__(self, root):
        super().__init__(root)
        # self.root.geometry('1000x700')
        self.root.state('normal')
        self.add_widgets()

    def add_widgets(self):
        # add 2 buttons
        # 1st button for faculty
        # 2nd for student
        self.fac_button = WhiteButton(self.img_lab,'FACULTY',lambda :Login("faculty", self))
        # self.fac_button.grid(row=0,column=0,padx=300,pady=120)
        self.fac_button.grid(row=0,column=0,padx=230,pady=120)
        self.stud_button = WhiteButton(self.img_lab,'STUDENT',lambda :Login("student", self))
        self.stud_button.grid(row=0,column=1,padx=10)
        self.img_lab.grid_propagate(0)

    def redirect_to_page(self,result,login_type):
        self.f.destroy()
        if login_type=='faculty':
            import FacultyHomePage as fhp
            fhp.FacultyHomePage(self.root,result)
        elif login_type=='student':
            import StudentHomePage as shp
            shp.StudentHomePage(self.root,result)

if __name__ == '__main__':
    root = Tk()
    m = MainPage(root)
    root.mainloop()
