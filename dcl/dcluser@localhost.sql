use mysql;
SELECT user,authentication_string,plugin,host FROM mysql.user;

show grants for dcluser@localhost;

SELECT * FROM AcademicRecords.Courses;
SELECT * FROM w3schools.categories;
INSERT INTO w3schools.categories (CategoryName, Description) values ('IceCream', 'Vanilla');