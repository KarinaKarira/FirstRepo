from tkinter import *
from Components.ButtonComponent import *
from Queries.Faculty import Query
from DatabaseHelper import *
from tkinter import messagebox
class AddStudent:
    def __init__(self):
        self.temp_root=Toplevel()
        self.temp_root.title("Student Details")
        self.f=Frame(self.temp_root,width=400,height=400,bg='light gray')
        self.f.pack()
        self.mes=Message(self.f,text='Enter details of the student',font=('Times new roman', 13),width=200)
        self.mes.grid(row=0,column=0,columnspan=2)

        self.l_roll=Label(self.f,text="Enter roll_no",font=('Times new roman', 13),width=15)
        self.l_roll.grid(row=1,column=0,padx=20,pady=20)
        self.e_roll=Entry(self.f,width=20)
        self.e_roll.grid(row=1,column=1,padx=20)

        self.l_name = Label(self.f, text="Enter name", font=('Times new roman', 13), width=15)
        self.l_name.grid(row=2, column=0,pady=10)
        self.e_name = Entry(self.f, width=20)
        self.e_name.grid(row=2, column=1)

        self.l_email = Label(self.f, text="Enter email-id", font=('Times new roman', 13), width=15)
        self.l_email.grid(row=3, column=0,pady=10)
        self.e_email = Entry(self.f, width=20)
        self.e_email.grid(row=3, column=1)

        self.l_pass = Label(self.f, text="Enter password", font=('Times new roman', 13), width=15)
        self.l_pass.grid(row=4, column=0,pady=10)
        self.e_pass = Entry(self.f, width=20)
        self.e_pass.grid(row=4, column=1)

        self.l_fac = Label(self.f, text='Faculty-id', font=('Times new roman', 13), width=15)
        self.l_fac.grid(row=5, column=0,pady=10)
        self.e_fac = Entry(self.f, width=20)
        self.e_fac.grid(row=5, column=1)

        self.f.grid_propagate(0)

        self.commit_b=GrayButton(self.f,text='Enter',command=self.add_details)
        self.commit_b.grid(row=6,column=0,columnspan=2,pady=10)

    def add_details(self):
        parameters=(self.e_roll.get(),self.e_name.get(),self.e_email.get(),self.e_pass.get(),self.e_fac.get())
        print(parameters)
        query=Query.INSERT_QUERY
        result = DatabaseHelper.execute_query(query, parameters)
        print(result)
        messagebox.showinfo('Insertion successfully','Details of the student are entered successfully')
        self.f.destroy()
        self.temp_root.destroy()


if __name__ == '__main__':
    root=Tk()
    a=AddStudent()
    root.mainloop()