class Query:
    INSERT_QUERY = 'Insert into Student values(%s,%s,%s,SHA(%s),%s)'
    VIEW_QUERY = 'select * from Student where roll_no=%s'
    UPDATE_QUERY= 'Update Student set stud_name=%s,emailid=%s,fac_incharge=%s where roll_no=%s'
    FETCH_DETAILS='Select roll_no,stud_name from Student'
    ADD_ATT_QUERY='Insert into attendance(roll_no,att_date,subject,IsPresent) values(%s,%s,%s,%s)'
    ADD_MARKS='Insert into marks(roll_no,subject,marks_scored) values(%s,%s,%s)'
    FETCH_QUERY='select stud_name,emailid,fac_incharge from student where roll_no=%s'
    # ATT_QUERY = 'Select attendance.roll_no,student.stud_name,attendance.IsPresent from Student natural join attendance'
