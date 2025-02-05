use mysql;
SELECT user,authentication_string,plugin,host FROM mysql.user;

show grants for root@localhost;

create user dcluser@localhost identified by 'Muz@mit1';

use AcademicRecords;
GRANT SELECT ON AcademicRecords.Courses TO dcluser@localhost;
GRANT SELECT, INSERT ON w3schools.categories TO dcluser@localhost;
REVOKE INSERT ON w3schools.categories FROM dcluser@localhost;