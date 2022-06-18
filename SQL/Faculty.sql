create table FACULTY
(
Fac_id int auto_increment KEY,
Fac_name varchar(20),
Password varchar(200),
designation varchar(20)
);

INSERT INTO FACULTY(Fac_name,password,designation) VALUES('Meena','Meena123','Lecturer');
select * from faculty;
