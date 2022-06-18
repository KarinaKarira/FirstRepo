create table STUDENT
(
roll_no int PRIMARY KEY,
stud_name varchar(20),
emailid varchar(20),
stud_pwd varchar(200),
fac_incharge int,
FOREIGN KEY(Fac_incharge) REFERENCES FACULTY(FAC_ID)
);

insert into student values
(101,'Karina','karina@123',SHA('12345'),1);