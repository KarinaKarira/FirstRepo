from BackgroundPage import *
from Components.ButtonComponent import *
from Queries.Student import *
from DatabaseHelper import *
from Components.Table import *
class ViewAttendance(BackgroundPage):
    def __init__(self,root,details):
        super().__init__(root)
        self.root=root
        self.stu_details=details
        self.att_l=Label(self.img_lab,text="Show attendance by",font=('Times new roman', 15),width=15,height=1)
        self.att_l.place(y=150,x=300)
        self.v1=StringVar()
        values=('Date','Subject')
        self.opt=OptionMenu(self.img_lab,self.v1,*values)
        self.opt.configure(width=8,font=('Times new roman', 12),height=1)
        self.opt.place(x=480,y=150)
        self.e_opt=Entry(self.img_lab,width=15,font=('Times new roman', 12),)
        self.e_opt.place(x=600,y=150)
        self.e_opt.bind('<Return>', lambda event: self.show_att(event))
    def show_att(self,e):
        self.sel_opt=self.e_opt.get()
        self.att_l.destroy()
        self.e_opt.destroy()
        self.opt.destroy()
        val=self.v1.get()
        print(val)
        if(val=='Subject'):
            query=Query.ATT_SUB
            self.lb = Label(self.img_lab, text='Subject:' + self.sel_opt, font=('Algerian', 15), width=15,bg='lightgray',fg='black',
                            height=1)
        else:
            query=Query.ATT_DATE
            self.lb = Label(self.img_lab, text='Date:' + self.sel_opt, font=('Algerian', 15), width=15,bg='lightgray',fg='black',
                            height=1)
        self.lb.place(y=70, x=100)
        parameters = (self.stu_details['roll_no'], self.sel_opt)
        self.result=DatabaseHelper.get_all_data(query,parameters)
        r_=len(self.result)
        c_=len(self.result[0])
        self.att_table=SimpleTable(self.f,rows=r_,columns=c_,width=600,height=500)
        self.att_table.place(x=120,y=100)
        for r in range(r_):
            for c in range(c_):
                if(c==c_-1 and r==0): #this is for setting the column name of first row
                    self.att_table.set(row=r,column=c,value='Status',font=('calibri',11,'bold'))
                else:
                    self.att_table.set(row=r, column=c, value=self.result[r][c], font=('calibri', 11, 'bold'))


