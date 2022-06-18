from tkinter import *
from Queries.Faculty import *
from DatabaseHelper import *
class ViewDetails:
    def __init__(self):
        self.temp_root = Toplevel()
        self.temp_root.title("Viewing Details")
        self.f = Frame(self.temp_root, width=400, height=300, bg='light gray')
        self.f.pack()
        self.mes = Message(self.f, text='Details', font=('Times new roman', 13), width=200)
        self.mes.grid(row=0, column=0, columnspan=2)
        self.f.grid_propagate(0)

        self.l_roll = Label(self.f, text="Enter roll_no", font=('Times new roman', 13), width=15)
        self.l_roll.grid(row=1, column=0, padx=20, pady=20)
        self.e_roll = Entry(self.f, width=20)
        self.e_roll.grid(row=1, column=1, padx=20)
        self.e_roll.bind('<Tab>', lambda event: self.tab_pressed(event))
        self.e_roll.bind('<Return>', lambda event: self.tab_pressed(event))  # can press enter or tab to get the details
        # never pass instance variables inside instance methods
        self.e_roll.focus_set()

    def tab_pressed(self,event):
        query=Query.VIEW_QUERY
        parameters=self.e_roll.get()
        self.result=DatabaseHelper.get_data(query, parameters)
        # self.result={'roll_no': 101, 'stud_name': 'Karina', 'emailid': 'karina@123',
        #  'stud_pwd': '8cb2237d0679ca88db6464eac60da96345513964', 'fac_incharge': 1}
        print(self.result)
        self.l_name = Label(self.f, text="Name", font=('Times new roman', 13), width=15)
        self.l_name.grid(row=2, column=0, pady=10)
        self.le_name = Label(self.f, text=self.result['stud_name'],font=('Times new roman', 13), width=15)
        self.le_name.grid(row=2, column=1)

        self.l_email = Label(self.f, text="Email-id", font=('Times new roman', 13), width=15)
        self.l_email.grid(row=3, column=0, pady=10)
        self.le_email = Label(self.f,text=self.result['emailid'],font=('Times new roman', 13), width=15)
        self.le_email.grid(row=3, column=1)

        self.l_fac = Label(self.f, text='Faculty-id', font=('Times new roman', 13), width=15)
        self.l_fac.grid(row=5, column=0, pady=10)
        self.le_fac = Label(self.f,text=self.result['fac_incharge'],font=('Times new roman', 13), width=15)
        self.le_fac.grid(row=5, column=1)

        self.f.grid_propagate(0)

if __name__ == '__main__':
    root=Tk()
    v=ViewDetails(root)
    root.mainloop()

