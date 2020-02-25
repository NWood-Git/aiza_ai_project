import sqlite3


def schema(dbpath = 'mydb.db'):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()


        # Create Cohort Table
        DROP_SQL = "DROP TABLE IF EXISTS cohort;"
        cur.execute(DROP_SQL)
        SQL = """CREATE TABLE cohort (
                    cohort_id     INT AUTO_INCREMENT PRIMARY KEY, 
                    name          VARCHAR(255)
                    );"""
        cur.execute(SQL)

        DROP_SQL = "DROP TABLE IF EXISTS students;"
        cur.execute(DROP_SQL)
        SQL = """CREATE TABLE students(
                stud_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cohort_id INT NOT NULL,
                name VARCHAR(255),
                FOREIGN KEY (cohort_id)
                    REFERENCES cohort (cohort_id)
                );"""
        cur.execute(SQL)

        # #Module 1 - Section 1
        DROP_SQL = "DROP TABLE IF EXISTS grades_intro_to_cs;"
        cur.execute(DROP_SQL)
        SQL = """CREATE TABLE grades_intro_to_cs(
                    stud_id   INTEGER PRIMARY KEY,
                    easy_e1   INTEGER,
                    easy_e2   INTEGER,
                    easy_e3   INTEGER,
                    easy_e4   INTEGER,
                    easy_e5   INTEGER,
                    easy_e6   INTEGER,
                    easy_e7   INTEGER,
                    med_e1    INTEGER,
                    med_e2    INTEGER,
                    med_e3    INTEGER,
                    hard_e1   INTEGER,
                    hard_e2   INTEGER,
                    FOREIGN KEY (stud_id) REFERENCES  students(stud_id) 
                    );"""
        cur.execute(SQL)

        # #Module 1 - Section 2
        DROP_SQL = "DROP TABLE IF EXISTS grades_IDEs;"
        cur.execute(DROP_SQL)
        SQL = """CREATE TABLE grades_IDEs(
                    stud_id   INTEGER PRIMARY KEY,
                    easy_e1   INTEGER,
                    easy_e2   INTEGER,
                    easy_e3   INTEGER,
                    easy_e4   INTEGER,
                    easy_e5   INTEGER,
                    easy_e6   INTEGER,
                    easy_e7   INTEGER,
                    med_e1    INTEGER,
                    med_e2    INTEGER,
                    med_e3    INTEGER,
                    hard_e1   INTEGER,
                    hard_e2   INTEGER,
                    FOREIGN KEY (stud_id) REFERENCES students(stud_id) 
                    );"""
        cur.execute(SQL)


def insert_student_test(dbpath = 'mydb.db'):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        SQL = "INSERT INTO students(cohort_id, name) VALUES(1,'Bart Simpson');"
        cur.execute(SQL)
        SQL = "INSERT INTO students(cohort_id, name) VALUES(1,'Lisa Simpson');"
        cur.execute(SQL)
        SQL = "INSERT INTO students(cohort_id,name) VALUES(1,'Maggie Simpson');"
        cur.execute(SQL)

def insert_student_grades_test(dbpath = 'mydb.db'):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        SQL = """INSERT INTO  grades_intro_to_cs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(1,1,0,1,1,0,0,0,1,1,0,1,1)"""
        cur.execute(SQL)
        SQL = """INSERT INTO  grades_intro_to_cs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(2,1,1,1,1,1,1,1,1,1,1,1,1)"""
        cur.execute(SQL)
        SQL = """INSERT INTO  grades_intro_to_cs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(3,1,1,1,1,1,0,0,1,0,0,1,0)"""
        cur.execute(SQL)
        SQL = """INSERT INTO  grades_IDEs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(1,1,0,1,1,0,0,0,1,1,0,1,1)"""
        cur.execute(SQL)
        SQL = """INSERT INTO  grades_IDEs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(2,1,1,1,1,1,1,1,1,1,1,1,1)"""
        cur.execute(SQL)
        SQL = """INSERT INTO  grades_IDEs(stud_id, easy_e1, easy_e2, easy_e3, easy_e4, easy_e5, easy_e6, easy_e7,
                med_e1, med_e2, med_e3, hard_e1, hard_e2) VALUES(3,1,1,1,1,1,0,0,1,0,0,1,0)"""
        cur.execute(SQL)

if __name__ == "__main__":
    schema()
    insert_student_test()
    insert_student_grades_test()
    pass