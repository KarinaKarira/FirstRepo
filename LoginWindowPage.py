from tkinter import *
from Components.ButtonComponent import WhiteButton
from tkinter import messagebox
from DatabaseHelper import *
from PIL import Image,ImageTk

class Login:
    def __init__(self,login_type,main_page):
        self.login_type=login_type
        self.main_page=main_page
        # 2 enteries
        # 2 labels
        # 2 buttons
        self.temp_root = Toplevel()
        self.temp_root.title(self.login_type)
        self.fr = Frame(self.temp_root, height=300, width=400,bg='light gray')
        self.fr.pack()

        # self.raw_image = Image.open('Images\Login_image6.jpg')
        # self.raw_image = self.raw_image.resize((300,400))
        # self.img=ImageTk.PhotoImage(self.raw_image)
        # self.img_lab=Label(self.fr,image=self.img)
        # self.img_lab.ref=self.img
        # self.img_lab.pack()
        # self.img_lab.pack_propagate(0)


        self.l_user = Label(self.fr, text="Enter ID",font=('Times new roman',13),width=15)
        self.l_user.grid(row=0, column=0,padx=20,pady=50)
        self.e_user = Entry(self.fr, width=20)
        self.e_user.grid(row=0,column=1)
        self.e_user.focus_set()
        self.l_pass = Label(self.fr, text="Enter password", font=('Times new roman',13),width=15)
        self.l_pass.grid(row=1, column=0)
        self.e_pass = Entry(self.fr, width=20,show='*')
        self.e_pass.grid(row=1, column=1)
        self.sub_b=WhiteButton(self.fr,'Submit',self.validate)
        self.sub_b.grid(row=2,column=0,pady=50,padx=10)
        self.reset_b = WhiteButton(self.fr, 'Reset', lambda: self.reset())
        self.reset_b.grid(row=2, column=1,padx=10)
        self.fr.grid_propagate(0)

    def validate(self):
        user=self.e_user.get()
        pwd=self.e_pass.get()
        if (self.login_type=='faculty'):
            query='select * from karina.faculty where fac_id=%s and password=%s'
        else:
            query = 'select * from karina.student where roll_no=%s and stud_pwd=SHA(%s)'
        parameters=(user,pwd)
        result=DatabaseHelper.get_data(query,parameters)
        print(user)
        print(pwd)
        if result is None:
            messagebox.showerror('Login Failed','Incorrect credentials')
            self.temp_root.tkraise()
            self.reset()
            self.e_user.focus_set()
        else:
            messagebox.showinfo('Login Successful','Authentification succeded')
            # destroying the temporary window created for login and redirecting to the main page
            self.fr.destroy()
            self.temp_root.destroy()
            self.main_page.redirect_to_page(result, self.login_type)

    def reset(self):
        self.e_user.delete(0,END)
        self.e_pass.delete(0,END)

if __name__ == '__main__':
    root = Tk()
    l = Login()
    root.mainloop()
