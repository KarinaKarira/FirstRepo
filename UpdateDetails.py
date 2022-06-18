from tkinter import *
from Components.ButtonComponent import *
from Queries.Faculty import *
from DatabaseHelper import *
from tkinter import messagebox
class UpdateDetails:
    def __init__(self):
        self.temp_root = Toplevel()
        self.temp_root.title("Updating Details")
        self.f = Frame(self.temp_root, width=400, height=400, bg='light gray')
        self.f.pack()
        self.mes = Message(self.f, text='Enter the updated details', font=('Times new roman', 13), width=200)
        self.mes.grid(row=0, column=0, columnspan=2)

        self.l_roll = Label(self.f, text="Enter roll_no", font=('Times new roman', 13), width=15)
        self.l_roll.grid(row=1, column=0, padx=20, pady=20)
        self.e_roll = Entry(self.f, width=20)
        self.e_roll.grid(row=1, column=1, padx=20)
        self.e_roll.bind('<Tab>',lambda event:self.tab_pressed(event))
        self.e_roll.bind('<Return>', lambda event: self.tab_pressed(event)) #can press enter or tab to get the details
        #never pass instance variables inside instance methods
        self.e_roll.focus_set()

        self.l_name = Label(self.f, text="Name", font=('Times new roman', 13), width=15)
        self.l_name.grid(row=2, column=0, pady=10)
        self.e_name = Entry(self.f, width=20)
        self.e_name.grid(row=2, column=1)

        self.l_email = Label(self.f, text="Email-id", font=('Times new roman', 13), width=15)
        self.l_email.grid(row=3, column=0, pady=10)
        self.e_email = Entry(self.f, width=20)
        self.e_email.grid(row=3, column=1)

        self.l_fac = Label(self.f, text='Faculty-id', font=('Times new roman', 13), width=15)
        self.l_fac.grid(row=5, column=0, pady=10)
        self.e_fac = Entry(self.f, width=20)
        self.e_fac.grid(row=5, column=1)

        self.f.grid_propagate(0)

        self.commit_b = GrayButton(self.f, text='Enter', command=self.update_details)
        self.commit_b.grid(row=6, column=0, columnspan=2, pady=10)

    def update_details(self):
        self.updated_name=self.e_name.get()
        self.updated_emailid=self.e_email.get()
        self.updated_fac_incharge=self.e_fac.get()
        parameters=(self.updated_name,self.updated_emailid,self.updated_fac_incharge,self.e_roll.get())
        query=Query.UPDATE_QUERY
        result=DatabaseHelper.execute_query(query,parameters)

    def tab_pressed(self,event):
        # fetching the details of the student whose data is to be updated with the help of the roll_no entered
        query = Query.FETCH_QUERY
        parameter = self.e_roll.get()
        result = DatabaseHelper.get_data(query, parameter)
        print(result)
        # here result is a dictionary returned from the database
        self.e_name.insert(0, result['stud_name'])
        self.e_email.insert(0, result['emailid'])
        self.e_fac.insert(0, result['fac_incharge'])
