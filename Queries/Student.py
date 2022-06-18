class Query:
    GET_MARKS='select subject,marks_scored from marks where roll_no=%s'
    ATT_SUB='select att_date,IsPresent from attendance where roll_no=%s and subject=%s'
    ATT_DATE='select subject,Ispresent from attendance where roll_no=%s and att_date=%s'
