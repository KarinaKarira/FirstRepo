create table MARKS
(
marks_id int auto_increment key,
roll_no int,
subject varchar(20),
marks_scored int default 35,
FOREIGN KEY (roll_no) REFERENCES STUDENT(roll_no)
);
INSERT INTO Marks(roll_no,subject) values(101,'MP');