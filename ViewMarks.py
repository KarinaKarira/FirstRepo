from BackgroundPage import *
from BackgroundPage import *
from Components.ButtonComponent import *
from Queries.Student import *
from Components.Table import *
from DatabaseHelper import *

class ViewMarks(BackgroundPage):
    def __init__(self,root,details):
        super().__init__(root)
        self.stu_details=details
        self.show_marks_b = GrayButton(self.img_lab, text='Show marks', command=self.show_marks)
        self.show_marks_b.pack(pady=5)
        self.img_lab.pack_propagate(0)

    def show_marks(self):
        self.show_marks_b.destroy()
        query = Query.GET_MARKS
        parameters = (self.stu_details['roll_no'])
        self.result = DatabaseHelper.get_all_data(query, parameters)
        # (('subject','marks_scored'),(sub,marks),(sub,marks))
        print(self.result)
        r_ = len(self.result)
        c_ = len(self.result[0])
        self.marks_table = SimpleTable(self.f, rows=r_, columns=c_, height=500, width=600)
        self.marks_table.place(x=120,y=100)
        for r in range(r_):
            for c in range(c_):
                self.marks_table.set(row=r, column=c, value=self.result[r][c],font=('calibri',11,'bold'))


