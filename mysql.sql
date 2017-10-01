CREATE DATABASE gradesystem;

use gradesystem;

CREATE TABLE student
(
	sid		int(4) PRIMARY KEY,
	sname	char(20),
	gender	char(10) DEFAULT 'female'
	);

CREATE TABLE course
(
	cid		int(4) PRIMARY KEY,
	cname	char(20)
	);

CREATE TABLE mark
(
	mid		int(4) PRIMARY KEY,
	sid		int(4), 
	cid		int(4),
	score	int(4),
	CONSTRAINT m_sid FOREIGN KEY (sid) REFERENCES student(sid),
	CONSTRAINT m_cid FOREIGN KEY (cid) REFERENCES course(cid),
	UNIQUE	(mid)
	);

INSERT INTO student VALUES(1,'Tom','male');
INSERT INTO student VALUES(2,'Jack','male');
INSERT INTO student(sid,sname) VALUES(3,'Rose');

INSERT INTO course VALUES(1,'math');
INSERT INTO course VALUES(2,'physics');
INSERT INTO course VALUES(3,'chemistry');

INSERT INTO mark VALUES(1,1,1,80);
INSERT INTO mark VALUES(2,2,1,85);
INSERT INTO mark VALUES(3,3,1,90);
INSERT INTO mark VALUES(4,1,2,60);
INSERT INTO mark VALUES(5,2,2,90);
INSERT INTO mark VALUES(6,3,2,75);
INSERT INTO mark VALUES(7,1,3,95);
INSERT INTO mark VALUES(8,2,3,75);
INSERT INTO mark VALUES(9,3,3,85);
