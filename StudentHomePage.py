from tkinter import *
from BackgroundPage import *
from Components.MessageComponent import *
from Components.ButtonComponent import *
from Queries.Student import *
from DatabaseHelper import *
from Components.Table import *
class StudentHomePage(BackgroundPage):
       def __init__(self,root,stud_details):
              super().__init__(root)
              self.details=stud_details
              self.root=root
              print(self.details)
              self.add_widgets()

       def add_widgets(self):
              self.wel_mess = GrayMessage(self.img_lab, text="welcome "+self.details["stud_name"])
              self.wel_mess.pack(side=TOP)

              self.view_marks_b=GrayButton(self.img_lab,text='View marks',command=self.view_marks)
              # self.view_marks_b.place(row=0,column=0,padx=430,pady=330)
              self.view_marks_b.place(x=430, y=350)
              # self.view_marks_b.pack(side=TOP,pady=30)

              self.view_att_b = GrayButton(self.img_lab, text='View attendance', command=self.view_att)
              # self.view_att_b.grid(row=1, column=0,pady=50)
              self.view_att_b.place(x=430,y=500)
              # self.view_marks_b.pack(side=TOP, pady=5)

              # self.img_lab.pack_propagate(0)

              self.log_out_b = GrayButton(self.img_lab, text='LOGOUT', command=self.log_out)
              self.log_out_b.place(x=700, y=50)

       def view_marks(self):
             self.f.destroy()
             import ViewMarks as v
             v.ViewMarks(self.root,self.details)

       def view_att(self):
              self.f.destroy()
              import ViewAttendance as va
              va.ViewAttendance(self.root,self.details)
       def log_out(self):
           self.f.destroy()
           import MainPage as m
           m.MainPage(self.root)


if __name__ == '__main__':
    root=Tk()
    details={'roll_no': 101, 'stud_name': 'Karina', 'emailid': 'karina@123', 'stud_pwd': '8cb2237d0679ca88db6464eac60da96345513964', 'fac_incharge': 1}
    StudentHomePage(root,details)
    root.mainloop()



