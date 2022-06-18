from BackgroundPage import *
from Components.ButtonComponent import GrayButton,WhiteButton
from Queries.Faculty import *
from DatabaseHelper import *
from Components.Table import *
class AddMarks(BackgroundPage):
    def __init__(self,root,details):
        super().__init__(root)
        self.fac_details=details
        self.root=root
        self.details_b=GrayButton(self.img_lab,'Enter details',self.add_details)
        self.details_b.pack(pady=5)
        self.img_lab.pack_propagate(0)
    def add_details(self):
        self.temp_root = Toplevel()
        self.temp_root.title("Marks")
        self.fr = Frame(self.temp_root, height=300, width=400, bg='light gray')
        self.fr.pack()
        self.l_sub = Label(self.fr, text="Enter subject", font=('Times new roman', 13), width=15)
        self.l_sub.grid(row=0, column=0, padx=20, pady=50)
        self.e_sub = Entry(self.fr, width=20)
        self.e_sub.grid(row=0, column=1)
        self.e_sub.focus_set()
        self.l_marks_out_of = Label(self.fr, text="Marks out of", font=('Times new roman', 13), width=15)
        self.l_marks_out_of.grid(row=1, column=0)
        self.e_marks_out_of = Entry(self.fr, width=20)
        self.e_marks_out_of.grid(row=1, column=1)
        self.sub_b = WhiteButton(self.fr, 'Proceed', command=self.add_table)
        # we need to add a table to mark the attendance
        self.sub_b.grid(row=2, column=0, pady=50, padx=10)
        self.reset_b = WhiteButton(self.fr, 'Reset', command=lambda: self.reset())
        self.reset_b.grid(row=2, column=1, padx=10)
        self.fr.grid_propagate(0)

    def reset(self):
        self.e_marks_out_of.delete(0,END)
        self.e_sub.delete(0,END)
    def add_table(self):
        self.sub=self.e_sub.get()
        self.marks_out_of=self.e_marks_out_of.get()
        self.temp_root.destroy()
        query=Query.FETCH_DETAILS
        self.stu_details=DatabaseHelper.get_all_data(query)
        r_=len(self.stu_details)
        c_=len(self.stu_details[0])+1
        self.marks_table=SimpleTable(self.f,rows=r_,columns=c_,width=800,height=500)
        self.marks_table.place(x=100,y=100)

        self.dct={}
        for i in range(1,len(self.stu_details)):
            self.e_marks = Entry(self.marks_table, width=5)
            self.dct[i]=self.e_marks
        for r in range(r_):
            for c in range(c_):
                if c==c_-1 and r==0:    #this row would be for giving the heading
                    self.marks_table.set(row=r,column=c,value='Marks',font=('calibri',10,'bold'))
                elif c==c_-1 and r!=0:
                    # check_b = Checkbutton(self.att_table, variable=self.dct_IntVar[self.stu_details[r][0]])
                    # self.att_table.set(row=r, column=c, value='', widget=check_b, font=('calibri', 10, 'bold'))
                    # self.e_marks=Entry(self.marks_table,width=5)
                    self.marks_table.set(row=r,column=c,value='',widget=self.dct[r])
                else:
                    self.marks_table.set(row=r,column=c,value=self.stu_details[r][c],font=('calibri',10,'bold'))

        self.enter_b = WhiteButton(self.img_lab, text='ENTER', command=self.add_marks, borderwidth=3)
        self.enter_b.pack(side=BOTTOM, pady=30)
        self.enter_b.pack_propagate(0)

    def add_marks(self):
        for i in range(1,len(self.stu_details)):
            query=Query.ADD_MARKS
            #roll_no,subject,marks_scored
            # print(self.stu_details[i][0],self.e_sub.get(),self.e_marks.get())
            # print(self.dct[i].get())
            parameters=(self.stu_details[i][0],self.sub,self.dct[i].get())
            DatabaseHelper.execute_query(query,parameters)
        self.f.destroy()
        import FacultyHomePage as fhp
        fhp.FacultyHomePage(self.root,self.fac_details)


