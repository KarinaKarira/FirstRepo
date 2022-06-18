from tkinter import *
from BackgroundPage import BackgroundPage
from Queries.Faculty import *
from DatabaseHelper import *
from Components.Table import *
from Components.ButtonComponent import *
class MarkAttendance(BackgroundPage):
    def __init__(self,root,details):
        super().__init__(root)
        self.root=root
        self.fac_details=details
        self.details_b = GrayButton(self.img_lab, text='Enter details', command=self.enter_att_details)
        self.details_b.pack(pady=5)
        self.img_lab.pack_propagate(0)

    def enter_att_details(self):
        self.temp_root = Toplevel()
        self.temp_root.title("Attendance")
        self.fr = Frame(self.temp_root, height=300, width=400, bg='light gray')
        self.fr.pack()
        self.l_sub = Label(self.fr, text="Enter subject", font=('Times new roman', 13), width=15)
        self.l_sub.grid(row=0, column=0, padx=20, pady=50)
        self.e_sub = Entry(self.fr, width=20)
        self.e_sub.grid(row=0, column=1)
        self.e_sub.focus_set()
        self.l_date = Label(self.fr, text="Enter date", font=('Times new roman', 13), width=15)
        self.l_date.grid(row=1, column=0)
        self.e_date = Entry(self.fr, width=20)
        self.e_date.grid(row=1, column=1)
        self.sub_b = WhiteButton(self.fr,'Proceed',command=self.add_table)
        # we need to add a table to mark the attendance
        self.sub_b.grid(row=2, column=0, pady=50, padx=10)
        self.reset_b = WhiteButton(self.fr,'Reset', command=lambda: self.reset())
        self.reset_b.grid(row=2, column=1, padx=10)
        self.fr.grid_propagate(0)


    def add_table(self):
        #details that we need to show in the table are:student_roll_no,name,checkbutton(not from database)
        self.sub=self.e_sub.get()
        self.date=self.e_date.get()
        self.temp_root.destroy()
        query=Query.FETCH_DETAILS
        self.stu_details=DatabaseHelper.get_all_data(query)
        # self.stu_details=(('roll_no', 'stud_name'), (101, 'Karina'), (102, 'Simran'), (103, 'Jessica'))
        r_=len(self.stu_details)
        c_=len(self.stu_details[0])+1
        self.att_table = SimpleTable(self.f, rows=r_, columns=c_,height=500,width=800)
        print(self.stu_details)
        self.att_table.place(x=100,y=100)
        #(('roll_no', 'stud_name','attendance status';)
        #(101, 'Karina','cb'))
        # self.att_table.grid_propogate(0)
        self.dct_IntVar={}
        #store roll_no as key and IsPresent checkbutton as value
        for i in range(1,len(self.stu_details)):
            self.dct_IntVar[self.stu_details[i][0]]=IntVar()
        #here we are starting the variable i from 1 since 0th row of self.details contains the column names
        #and we don't want them to be stored in the dictionary

        for r in range(r_):
            for c in range(c_):
                if (c==c_-1 and r!=0):
                    check_b = Checkbutton(self.att_table, variable=self.dct_IntVar[self.stu_details[r][0]])
                    self.att_table.set(row=r, column=c, value='', widget=check_b,font=('calibri',10,'bold'))
                     # put checkbutton in all last column apart from first row
                elif (c==c_-1 and r==0):
                    self.att_table.set(row=r, column=c, value='Attendance status',font=('calibri',10,'bold'))
                else:
                    self.att_table.set(row=r, column=c, value=self.stu_details[r][c], font=('calibri', 10, 'bold'))

        self.enter_b = WhiteButton(self.img_lab, text='ENTER', command=self.add_attendance,borderwidth=3)
        self.enter_b.pack(side=BOTTOM,pady=30)
        self.enter_b.pack_propagate(0)



    def add_attendance(self):
        for i in range(1,len(self.stu_details)):
            query=Query.ADD_ATT_QUERY
            print(query)
            if self.dct_IntVar[self.stu_details[i][0]].get()==1:
                self.status='P'
            else:
                self.status='A'
            print('add_attendance called')
            print(self.dct_IntVar)
            print(self.status)
            parameters = (self.stu_details[i][0], self.date,self.sub, self.status)
            print(parameters)
            DatabaseHelper.execute_query(query,parameters)
        self.f.destroy()
        import FacultyHomePage as fhp
        fhp.FacultyHomePage(self.root, self.fac_details)


    def reset(self):
        self.e_sub.delete(0,END)
        self.e_date.delete(0,END)

if __name__ == '__main__':
    root=Tk()
    details={'Fac_id': 2, 'Fac_name': 'RITESH', 'Password': 'SGT', 'designation': 'HOD'}
    m=MarkAttendance(root,details)
    root.mainloop()