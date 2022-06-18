create table ATTENDANCE
(
att_id int auto_increment key,
roll_no int,
Att_date varchar(20),
subject varchar(20),
IsPresent char,
FOREIGN KEY (roll_no) REFERENCES STUDENT(roll_no)
);