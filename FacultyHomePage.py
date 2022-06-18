from tkinter import *
from BackgroundPage import *
from Components.MessageComponent import *
from Components.ButtonComponent import *



class FacultyHomePage(BackgroundPage):
    def __init__(self, root, fac_details):
        super().__init__(root)
        self.details = fac_details #store the details of the faculty fetched from the database
        self.root=root
        print(self.details)
        self.add_widgets()

    def add_widgets(self):
        self.wel_mess = GrayMessage(self.img_lab, text="welcome " + self.details['Fac_name'])
        self.wel_mess.pack(side=TOP)

        self.add_b = GrayButton(self.img_lab, text='Add a student', command=self.add_student)
        # self.add_b.grid(row=0, column=0, padx=430, pady=330)
        self.add_b.place(x=430,y=330)
        # self.add_b.pack(side=TOP,pady=15)

        self.update_b = GrayButton(self.img_lab, text='Update details', command=self.update_details)
        # self.update_b.grid(row=1, column=0,pady=10)
        self.update_b.place(x=430, y=390)
        # self.update_b.pack(side=TOP,pady=15)

        self.mark_att_b = GrayButton(self.img_lab, text='Mark Attendance', command=self.mark_attendance)
        # self.mark_att_b.grid(row=2, column=0,pady=10)
        self.mark_att_b.place(x=430, y=450)
        # self.mark_att_b.pack(side=TOP,pady=15)

        self.add_marks_b = GrayButton(self.img_lab, text='Add marks', command=self.add_marks)
        # self.add_marks_b.grid(row=3, column=0, pady=10)
        self.add_marks_b.place(x=430, y=510)
        # self.add_marks_b.pack(side=TOP,pady=15)

        self.view_details_b = GrayButton(self.img_lab, text='View Details', command=self.view_details)
        # self.view_details_b.grid(row=4, column=0, pady=10)
        self.view_details_b.place(x=430, y=570)
        # self.view_details_b.pack(side=TOP,pady=15)

        self.log_out_b=GrayButton(self.img_lab,text='LOGOUT',command=self.log_out)
        self.log_out_b.place(x=700,y=50)

        # self.img_lab.place_propagate(0)
    def add_student(self):
        import AddStudent as a
        a.AddStudent()

    def log_out(self):
        import MainPage as m
        self.f.destroy()
        m.MainPage(self.root)

    def update_details(self):
        import UpdateDetails as u
        u.UpdateDetails()

    def mark_attendance(self):
        self.f.destroy()
        import MarkAttendance as m
        m.MarkAttendance(self.root,self.details)

    def add_marks(self):
        self.f.destroy()
        import AddMarks as a
        a.AddMarks(self.root,self.details)

    def view_details(self):
        import ViewDetails as v
        v.ViewDetails()
if __name__ == '__main__':
    root=Tk()
    f=FacultyHomePage(root)
    root.mainloop()